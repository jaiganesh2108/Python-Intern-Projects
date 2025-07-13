<h1>🧠 AI Code Reviewer</h1>

An interactive web application to **analyze, format, and evaluate Python code quality** using:

- 🧹 `flake8` for linting
- 🎨 `black` for formatting
- 📊 `radon` for complexity analysis
- 🌐 `Streamlit` for the web UI

---

## 📸 Demo

![AI Code Reviewer Screenshot](https://user-images.githubusercontent.com/your-demo-image.png)

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
