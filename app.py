import streamlit as st
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from legal_splitter import LegalSemanticSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# .env dosyasını yükle
load_dotenv()

# Sayfa yapılandırması
st.set_page_config(page_title="Legal-RAG: Kat Mülkiyeti Asistanı", layout="wide")
st.title("🏢 Kat Mülkiyeti Mevzuatı Akıllı Asistanı")

# Sabitler
DATA_PATH = "data/raw/kat-mulkiyeti-kanunu.pdf"
DB_DIR = "data/vector_db"

def initialize_rag():
    """RAG boru hattını ilklendirir."""
    
    # 1. PDF Yükleme
    if not os.path.exists(DATA_PATH):
        st.error(f"Hata: {DATA_PATH} bulunamadı!")
        return None

    loader = PyPDFLoader(DATA_PATH)
    documents = loader.load()

    # 2. Özel Hukuki Metin Parçalama (Madde bazlı)
    text_splitter = LegalSemanticSplitter(chunk_size=1500, chunk_overlap=200)
    splits = text_splitter.split_documents(documents)

    # 3. Embedding Modeli
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # 4. Vektör Veritabanı (ChromaDB)
    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=embeddings,
        persist_directory=DB_DIR
    )
    vectorstore.persist()
    
    return vectorstore

# Sidebar - Yapılandırma ve Bilgi
with st.sidebar:
    st.header("Sistem Durumu")
    if st.button("Veritabanını Yeniden Oluştur"):
        with st.spinner("Veriler işleniyor..."):
            st.session_state.vectorstore = initialize_rag()
            st.success("Veritabanı güncellendi!")
    
    st.markdown("""
    ### Hakkında
    Bu asistan, Kat Mülkiyeti Kanunu çerçevesinde sorularınızı yanıtlar.
    
    **Kullanılan Teknolojiler:**
    - LangChain
    - ChromaDB
    - Gemini Pro
    - Sentence Transformers
    """)

# RAG Kurulumu
if 'vectorstore' not in st.session_state:
    with st.spinner("Sistem hazırlanıyor..."):
        st.session_state.vectorstore = initialize_rag()

# Soru-Cevap Arayüzü
if st.session_state.vectorstore:
    # LLM Kurulumu (Gemini)
    llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)

    # Prompt Şablonu
    template = """Aşağıdaki bağlamı (context) kullanarak kullanıcının sorusuna cevap ver. 
    Eğer cevabı bağlam içerisinde bulamıyorsan, bilmediğini söyle, uydurma.
    Cevabını her zaman ilgili kanun maddesine atıfta bulunarak (Örn: KMK Madde 12'ye göre...) ver.

    Bağlam:
    {context}

    Soru: {question}
    
    Cevap:"""
    
    QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

    # QA Chain
    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=st.session_state.vectorstore.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=True,
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
    )

    # Chat Arayüzü
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Sorunuzu buraya yazın..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Düşünüyorum..."):
                result = qa_chain({"query": prompt})
                response = result["result"]
                sources = result["source_documents"]
                
                st.markdown(response)
                
                with st.expander("Kaynak Dokümanlar"):
                    for i, doc in enumerate(sources):
                        st.write(f"**Kaynak {i+1}:**")
                        st.write(doc.page_content)
                        st.write("---")
                
                st.session_state.messages.append({"role": "assistant", "content": response})
else:
    st.warning("Lütfen veritabanını oluşturmak için PDF dosyasının mevcut olduğundan emin olun.")
