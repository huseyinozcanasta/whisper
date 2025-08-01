FROM python:3.10-slim

# ffmpeg yükle
RUN apt-get update && apt-get install -y ffmpeg

# çalışma dizini oluştur
WORKDIR /main

# dosyaları kopyala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Flask uygulamasını başlat
CMD ["python", "main.py"]
