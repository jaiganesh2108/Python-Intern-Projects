from flask import Flask, render_template, request, send_file
import fitz  # PyMuPDF
from gtts import gTTS
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_pdf_to_audio():
    if 'pdf' not in request.files:
        return "No PDF uploaded", 400

    pdf_file = request.files['pdf']
    filepath = os.path.join(UPLOAD_FOLDER, pdf_file.filename)
    pdf_file.save(filepath)

    doc = fitz.open(filepath)
    text = ""
    for page in doc:
        content = page.get_text().strip()
        if content:
            text += content + "\n"

    if not text.strip():
        return "PDF is empty or unreadable", 400

    tts = gTTS(text)
    audio_path = os.path.join(OUTPUT_FOLDER, "audio.mp3")
    tts.save(audio_path)

    return send_file(audio_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
