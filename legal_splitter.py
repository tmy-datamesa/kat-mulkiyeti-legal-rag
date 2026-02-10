import re
from typing import List
from langchain.schema import Document

class LegalSemanticSplitter:
    """
    Türk hukuk metinlerini (özellikle KMK) madde, ek madde ve geçici madde 
    yapılarına göre bölen özel splitter.
    """
    def __init__(self, chunk_size: int = 1500, chunk_overlap: int = 200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        # Madde başlıklarını yakalayan regex (Örn: Madde 1 -, EK MADDE 2 -, GEÇİCİ MADDE 5 -)
        self.article_pattern = re.compile(
            r'(?m)^(Madde\s+\d+\s*[-–:]|EK\s+MADDE\s+\d+\s*[-–:]|GEÇİCİ\s+MADDE\s+\d+\s*[-–:])', 
            re.IGNORECASE
        )

    def split_documents(self, documents: List[Document]) -> List[Document]:
        final_chunks = []
        
        for doc in documents:
            text = doc.page_content
            # Metni madde başlıklarına göre böl
            parts = self.article_pattern.split(text)
            
            current_chunk_text = ""
            if parts[0]: # İlk madde öncesi metin (başlık vs.)
                current_chunk_text = parts[0]

            # parts listesi [öncesi, madde_başlığı_1, madde_içeriği_1, madde_başlığı_2, ...] şeklinde ilerler
            for i in range(1, len(parts), 2):
                article_title = parts[i]
                article_content = parts[i+1] if i+1 < len(parts) else ""
                
                full_article = article_title + article_content
                
                # Eğer mevcut chunk + yeni madde sınırı aşıyorsa, mevcut chunk'ı kaydet
                if len(current_chunk_text) + len(full_article) > self.chunk_size and current_chunk_text:
                    final_chunks.append(Document(
                        page_content=current_chunk_text.strip(),
                        metadata=doc.metadata.copy()
                    ))
                    current_chunk_text = full_article
                else:
                    current_chunk_text += "\n\n" + full_article
            
            # Kalan son parçayı ekle
            if current_chunk_text:
                final_chunks.append(Document(
                    page_content=current_chunk_text.strip(),
                    metadata=doc.metadata.copy()
                ))
                
        return final_chunks
