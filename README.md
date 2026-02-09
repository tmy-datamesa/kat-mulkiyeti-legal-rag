# Legal-RAG: Kat Mülkiyeti Mevzuatı ve Apartman Yönetimi Akıllı Asistanı

Bu proje, **Kat Mülkiyeti Kanunu** ve apartman yönetimiyle ilgili mevzuat sorularına,  
**yalnızca resmi dokümanlara dayanarak** ve **kaynak göstererek** cevap veren  
RAG (Retrieval-Augmented Generation) tabanlı bir soru–cevap prototipidir.

> ⚠️ **Önemli Not:**  
> Bu sistem hukuki tavsiye üretmez.  
> Yalnızca mevzuat metinlerine dayalı bilgilendirme amacıyla tasarlanmıştır.

---

## 🎯 Projenin Amacı

Genel amaçlı büyük dil modelleri, hukuki metinlerde:
- Kaynaksız cevap üretme,
- Yanlış veya eksik yorum yapma,
- Halüsinasyon riski

gibi problemler barındırmaktadır.

Bu projenin amacı, **RAG mimarisi** kullanarak:
- Dil modelini yalnızca ilgili mevzuat metniyle sınırlamak,
- Üretilen cevapların kanun maddelerine sadık kalmasını sağlamak,
- Hukuki metinlerde LLM kullanımının sınırlarını ve risklerini anlamaktır.

---

## 🧩 Çözüm Yaklaşımı (RAG)

Sistem aşağıdaki adımlarla çalışır:

Kullanıcı Sorusu
↓
İlgili Kanun Maddelerinin Getirilmesi (Retrieval)
↓
LLM ile Cevap Üretimi (Sadece Getirilen Metin Üzerinden)
↓
Kaynak Gösterilerek Cevabın Sunulması


Bu yaklaşım sayesinde modelin serbest bilgi üretmesi engellenir.

---

## 📚 Veri Seti

### Birincil Kaynak
- **634 Sayılı Kat Mülkiyeti Kanunu** (Resmi Gazete metni)

### İkincil Kaynaklar (opsiyonel)
- Standart apartman yönetim planları  
- Örnek Yargıtay emsal kararları

---

## 🛠 Veri Hazırlığı

Hukuki metinlerde bağlam kaybını önlemek için özel bir veri hazırlama süreci izlenir:

- **Parsing:** PDF/Text formatındaki metinlerin temizlenmesi  
- **Semantic Chunking:** Metinlerin madde ve fıkra bütünlüğü korunarak bölünmesi  
- **Embedding:** Metinlerin anlamsal vektör temsiline dönüştürülmesi  
- **Depolama:** Vektörlerin yerel bir vektör veritabanında indekslenmesi  

---

## 🧪 Başarı Metrikleri

Proje başarısı aşağıdaki ölçütlerle değerlendirilir:

- **Faithfulness:** Üretilen cevabın kanun maddesine sadık kalma oranı  
- **Answer Relevance:** Cevabın kullanıcının sorusuna ne kadar hitap ettiği  
- **Context Precision:** Doğru kanun maddesinin getirilebilme oranı  

---

## ⚠️ Karşılaşılması Beklenen Zorluklar

- Hukuki metinlerde bağlam kaybı riski  
- Yanlış madde üzerinden cevap üretilmesi  
- Yerel LLM’lerde donanım kaynaklı bellek (OOM) sorunları  
- Türkçe dil performansının modele göre değişkenlik göstermesi  
- Kütüphane ve sürüm uyumsuzlukları  

---

## 🧱 Teknoloji Yığını (Tech Stack)

- **Python**
- **LangChain** (RAG orkestrasyonu)
- **Streamlit** (kullanıcı arayüzü)
- **Vektör Veritabanı:** ChromaDB
- **Dil Modelleri:**  
  - Bulut tabanlı LLM’ler (teorik değerlendirme)  
  - Yerel çalışabilen açık kaynak LLM’ler (opsiyonel)

> Model seçimi; gizlilik, maliyet ve donanım kısıtlarına göre değerlendirilmektedir.

---

## 🔄 Proje Yönetimi & MLOps Yaklaşımı

- **Versiyonlama:** Git / GitHub  
- **Deney Takibi:** Farklı chunk ve model yapılarını karşılaştırma  
- **Reprodüktibilite:** Ortam bağımlılıklarının standartlaştırılması  

---

## 🚀 Nihai Çıktı

- Yerel ortamda çalışabilen  
- Doküman yükleme yeteneğine sahip  
- Mevzuat sorularına **kaynak göstererek** cevap veren  
- Web tabanlı bir RAG uygulaması

---

## 👥 Takım

- Atakan Can  
- Berkay Turhan  
- Tümay Turhan  

---

## 📌 Not

Bu proje, kusursuz bir hukuk asistanı geliştirmeyi değil;  
**LLM’lerin hukuki metinlerde hangi koşullarda güvenilir hale geldiğini anlamayı** hedefleyen bir öğrenme projesidir.