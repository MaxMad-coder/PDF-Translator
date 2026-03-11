# 📄 PDF Translator

A **Flask-based backend** application that translates PDF documents into any target language. It extracts both text and images from PDFs, uses **Google Cloud Translate API** for translation, **Tesseract OCR** to extract text from images, and generates a fully translated PDF as output.

---

## 🖥️ Features

- 📤 Upload any PDF file via REST API
- 🌍 Translate PDF text to any target language
- 🖼️ Extract images from PDF automatically
- 🔍 OCR support — extracts and translates text inside images
- 📥 Returns a new translated PDF with original images preserved
- ⚡ Built with Flask — lightweight and fast

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| Flask | Web framework / REST API |
| PyPDF2 | Extract text from PDF |
| PyMuPDF (fitz) | Extract images from PDF |
| Google Cloud Translate API | Translate extracted text |
| Tesseract OCR (pytesseract) | Extract text from images |
| Pillow (PIL) | Image handling |
| ReportLab | Generate translated PDF output |

---

## 📁 Project Structure

```
pdf-translator/
│
├── backend.py                  # Main Flask application
├── translated_with_images.pdf  # Output file (auto-generated)
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/pdf-translator.git
cd pdf-translator
```

### 2. Create a Virtual Environment (Recommended)
```bash
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install flask PyPDF2 pymupdf pytesseract Pillow reportlab google-cloud-translate
```

Or use requirements.txt:
```bash
pip install -r requirements.txt
```

### 4. Install Tesseract OCR Engine

Windows:
```
Download from https://github.com/UB-Mannheim/tesseract/wiki
Add to PATH after installation
```

Linux:
```bash
sudo apt install tesseract-ocr
```

Mac:
```bash
brew install tesseract
```

### 5. Set Up Google Cloud Translate API

```
1. Go to https://console.cloud.google.com
2. Create a new project
3. Enable Cloud Translation API
4. Create Service Account credentials
5. Download the JSON key file
6. Set the environment variable:
```

Windows:
```bash
set GOOGLE_APPLICATION_CREDENTIALS=path\to\your-key.json
```

Mac/Linux:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your-key.json"
```

### 6. Run the Application
```bash
python backend.py
```

Server starts at:
```
http://localhost:5000
```

---

## 🚀 API Usage

### Endpoint
```
POST /translate
```

### Request (multipart/form-data)

| Field | Type | Description |
|---|---|---|
| file | File | PDF file to translate |
| lang | String | Target language code (e.g. es, fr, hi) |

### Example using cURL
```bash
curl -X POST http://localhost:5000/translate \
  -F "file=@document.pdf" \
  -F "lang=es" \
  --output translated.pdf
```

### Example using Python requests
```python
import requests

url = "http://localhost:5000/translate"
files = {"file": open("document.pdf", "rb")}
data = {"lang": "es"}

response = requests.post(url, files=files, data=data)

with open("translated.pdf", "wb") as f:
    f.write(response.content)

print("Translation complete!")
```

---

## 🌍 Supported Language Codes

| Language | Code |
|---|---|
| Spanish | es |
| French | fr |
| Hindi | hi |
| German | de |
| Chinese | zh |
| Arabic | ar |
| Japanese | ja |
| Portuguese | pt |
| Russian | ru |
| Tamil | ta |

Full list at https://cloud.google.com/translate/docs/languages

---

## 📌 requirements.txt

```
flask
PyPDF2
pymupdf
pytesseract
Pillow
reportlab
google-cloud-translate
```

---

## 📄 License

This project is open-source and free to use under the MIT License.

---

## 🙋 Author

**Your Name**
- GitHub: [@MaxMad-coder](https://github.com/MaxMad-coder)
- Email: manash212005@gmail.com
