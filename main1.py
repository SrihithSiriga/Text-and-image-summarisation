import google.generativeai as genai
import PyPDF2
import easyocr
import io


genai.configure(api_key="AIzaSyAqXz92Peh33tJS0jbiI0qqzb3u_fQksDE")#Add your API key here
model = genai.GenerativeModel('gemini-1.5-flash')
reader = easyocr.Reader(['en'])
PROMPT="You are a summarizer AI. You are given a Text. You need to summarize the given text. The given text is :"


def extract_text_from_pdf(pdf_file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    for page_num in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page_num].extract_text()
    return text

def extract_text_from_image(image_bytes):
    result = reader.readtext(image_bytes)
    text = ' '.join([res[1] for res in result])
    return text

def summarize_text(text, type):
    response = model.generate_content(f'{PROMPT}{text}')
    return response.text