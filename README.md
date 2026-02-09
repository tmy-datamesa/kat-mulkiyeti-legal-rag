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

