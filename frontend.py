import streamlit as st
from main1 import extract_text_from_pdf, extract_text_from_image, summarize_text


st.title("Text Summarizer")
st.write("This is a simple text summarizer that uses AI to summarize text from PDFs and images.")

def main():
    with st.sidebar:
        st.subheader("Select File")
        uploaded_file = st.file_uploader("Upload your file", type=['pdf', 'png', 'jpg', 'jpeg', 'txt', 'jfif'])
        extracted_text = ""
        button = False
        
        if uploaded_file is not None:
            uploaded_file_type = uploaded_file.name.split('.')[-1].lower()
            
            button = st.button("Summarize") 
            if uploaded_file_type in ['png', 'jpg', 'jpeg'] and button:
                image_bytes = uploaded_file.read()
                extracted_text = extract_text_from_image(image_bytes)
            elif uploaded_file_type == 'pdf'and button:
                extracted_text = extract_text_from_pdf(uploaded_file)
    if button:
        if uploaded_file_type == "pdf":
            with st.spinner("Summarizing PDF..."):
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("Original Text")
                    st.write(extracted_text)
                with col2:
                    st.subheader("Summarized Text From PDF")
                    summarized_text = summarize_text(extracted_text, "pdf")
                    st.write(summarized_text)
        else:
            with st.spinner("Summarizing Image..."):
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("Original Text")
                    st.write(extracted_text)
                with col2:
                    st.subheader("Summarized Text From Image")
                    summarized_text = summarize_text(extracted_text, "image")
                    st.write(summarized_text)


if __name__ == "__main__":
    main()