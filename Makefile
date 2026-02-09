# Proje kurulumu için yardımcı komutlar

# Sanal ortamı oluştur ve kütüphaneleri yükle
setup:
	python3 -m venv .venv
	./.venv/bin/pip install --upgrade pip
	./.venv/bin/pip install -r requirements.txt

# Gereksiz dosyaları temizle
clean:
	rm -rf .venv
	find . -type d -name "__pycache__" -exec rm -rf {} +

# Veri işleme scriptini çalıştır (yarın yazacağız)
ingest:
	./.venv/bin/python3 src/ingestion.py