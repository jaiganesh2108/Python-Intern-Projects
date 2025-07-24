<h1>Python Internship Projects</h1>

<h2> 1. AI Code Reviewer</h2>
<h2> 2. PDF to Audiobook Converter</h2>

---

# 🧠 AI Code Reviewer
An interactive web application to **analyze, format, and evaluate Python code quality** using:

- 🧹 `flake8` for linting
- 🎨 `black` for formatting
- 📊 `radon` for complexity analysis
- 🌐 `Streamlit` for the web UI

---

## 🚀 Features

✅ Paste or upload `.py` files  
✅ Lint code using `flake8` (PEP8 checks)  
✅ Format code with `black` (auto cleanups)  
✅ Analyze code complexity with `radon`  
✅ Download the formatted version  
✅ Simple, intuitive Streamlit GUI  

---

## 📦 Requirements

Install the dependencies:

```bash
pip install -r requirements.txt
```

## 🛠️ How to Run

Run the Streamlit app locally:
```bash
streamlit run app.py
```
Then open your browser at http://localhost:8501
```bash
.
├── app.py            # Streamlit frontend
├── utils.py          # Backend logic (linting, formatting, analysis)
├── requirements.txt  # Dependencies
└── README.md         # Project overview
```
## 🧠 Why This Project?

This tool is perfect for:

- Students learning clean code practices
- Developers reviewing Python code quality
- Teams integrating static analysis into review pipelines

---

# 🔊 PDF to Audiobook Converter

A simple and powerful **web-based tool** to convert any PDF document into **spoken audio (MP3)** using **Python + Flask + gTTS**. Upload your PDF, convert it into speech, and download the audiobook—all from your browser!

---

## 📌 Features

✅ Upload any `.pdf` file  
✅ Extract and clean text from the PDF  
✅ Convert the text into speech using `gTTS`  
✅ Download the result as an `.mp3` file  
✅ Beautiful HTML frontend (no Tkinter!)

---

## 🌐 Tech Stack

| Layer      | Tool        |
|------------|-------------|
| **Frontend** | HTML, CSS |
| **Backend**  | Flask (Python) |
| **PDF Extraction** | PyMuPDF (`fitz`) |
| **Text-to-Speech** | gTTS |
| **Audio Handling** | pydub |
| **Audio Playback** | HTML5 or download |

---

## 📁 Folder Structure

```
pdf-to-audiobook-converter/
│
├── app.py # Flask backend
├── requirements.txt # All dependencies
├── templates/
│ └── index.html # HTML frontend
├── static/
│ └── style.css # Optional CSS styles
├── uploads/ # Temporarily stores uploaded PDFs
└── output/ # Stores generated MP3 files
```
---

## 🔧 Installation

Install all required packages:
```bash
pip install flask PyMuPDF gTTS pydub
```

---
 
🚀 Run the App

## Start the Flask server:

```bash

python app.py
```

## Visit in browser:

```
http://localhost:5000
```
## 🧠 How It Works
- Upload a .pdf file via the browser.
- PyMuPDF extracts and cleans text from the pages.
- gTTS converts the text to speech.
- The user downloads the resulting .mp3 file.

---

## 📣 Credits
Created by Jai Ganesh H!
Inspired by the idea of accessibility and learning through listening.

