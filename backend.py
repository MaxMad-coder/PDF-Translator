from flask import Flask, request, send_file
from PyPDF2 import PdfReader
from google.cloud import translate_v2 as translate
import fitz  # PyMuPDF for image extraction
import io
import pytesseract
from PIL import Image
from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image as PDFImage, Spacer
from reportlab.lib.styles import getSampleStyleSheet

app = Flask(__name__)

# Translation Function
def translate_text(text, target_lang="es"):
    client = translate.Client()
    result = client.translate(text, target_language=target_lang)
    return result['translatedText']

# Extract Images from PDF
def extract_images(pdf_file):
    images = []
    pdf_document = fitz.open(stream=pdf_file.read(), filetype="pdf")

    for page_number in range(len(pdf_document)):
        page = pdf_document.load_page(page_number)
        images += page.get_images(full=True)

    image_list = []
    for img in images:
        xref = img[0]
        base_image = pdf_document.extract_image(xref)
        image_bytes = base_image["image"]
        image_list.append(io.BytesIO(image_bytes))

    return image_list

# Extract Text from Images using Tesseract OCR
def extract_text_from_images(image_list):
    extracted_text = ""
    
    for img_data in image_list:
        img_data.seek(0)
        img = Image.open(img_data)

        # Use OCR to extract text
        text = pytesseract.image_to_string(img)
        extracted_text += text + "\n"

    return extracted_text

# PDF Upload and Translation
@app.route('/translate', methods=['POST'])
def translate_pdf():
    file = request.files['file']
    target_lang = request.form['lang']

    # Extract text and images
    reader = PdfReader(file)
    images = extract_images(file)

    translated_text = ""
    
    # Translate regular PDF text
    for page in reader.pages:
        text = page.extract_text()
        translated_text += translate_text(text, target_lang) + "\n"

    # Extract and translate image text
    image_text = extract_text_from_images(images)
    translated_text += translate_text(image_text, target_lang)

    # Generate translated PDF
    output = "translated_with_images.pdf"
    doc = SimpleDocTemplate(output, pagesize=LETTER)
    styles = getSampleStyleSheet()
    content = []

    # Add translated text
    content.append(Paragraph(translated_text, styles['Normal']))
    content.append(Spacer(1, 12))

    # Add images to the PDF
    for img in images:
        img.seek(0)
        img_data = PDFImage(img, width=400, height=300)
        content.append(img_data)
        content.append(Spacer(1, 12))

    doc.build(content)

    return send_file(output, as_attachment=True)

if __name__ == '__main__':
    app.run(port=5000)
