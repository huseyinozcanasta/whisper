from flask import Flask, request, jsonify
import whisper
import os

app = Flask(__name__)
model = whisper.load_model("small")  # İstersen "small", "medium", "large" seçebilirsin

@app.route("/transcribe", methods=["POST"])
def transcribe():
    if "audio" not in request.files:
        return jsonify({"error": "No audio file uploaded"}), 400

    audio = request.files["audio"]
    path = "temp.wav"
    audio.save(path)

    result = model.transcribe(path, language="tr")
    os.remove(path)

    return jsonify(result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)

