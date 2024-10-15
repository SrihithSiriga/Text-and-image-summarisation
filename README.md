This project is a simple web application that uses AI to summarize text from PDF files and images. The app is built using Streamlit for the front-end interface and Google's Generative AI along with EasyOCR and PyPDF2 for processing the text.

Features
Summarizes text from PDF files and images.
Extracts text from PDFs using PyPDF2.
Extracts text from images (PNG, JPG, JPEG) using EasyOCR.
Uses Google's Gemini-1.5-flash AI model to generate summaries of the extracted text.
Files
1. frontend.py
This file contains the code for the Streamlit front-end interface. Users can upload files (PDFs or images) and click a button to summarize the text. The app displays both the original text and the summarized text in two columns.

2. main1.py
This file contains the logic for extracting text and generating summaries:

extract_text_from_pdf: Extracts text from PDF files.
extract_text_from_image: Uses EasyOCR to extract text from images.
summarize_text: Summarizes the extracted text using Google Generative AI.
How to Run
Clone the repository.
Install the required libraries:
pip install streamlit PyPDF2 easyocr google-generativeai
Add your Google Generative AI API key in the main1.py file.
Run the Streamlit app:
streamlit run frontend.py
Upload a PDF or image to get the summarized text.
Libraries Used
Streamlit
PyPDF2
EasyOCR
Google Generative AI
