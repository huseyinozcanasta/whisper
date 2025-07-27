from fastapi import FastAPI, UploadFile, File
import whisper

app = FastAPI()
model = whisper.load_model("base")

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    audio = await file.read()
    # Dosyayı diske kaydet
    with open("temp_audio.mp3", "wb") as f:
        f.write(audio)
    # Transkription işlemi
    result = model.transcribe("temp_audio.mp3")
    return {"text": result["text"]}
