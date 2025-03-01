import streamlit as st
import pdfplumber
from transformers import pipeline
import torch

# ✅ Check if GPU is available
device = 0 if torch.cuda.is_available() else -1

# ✅ Load the QA model (Use text-generation or switch to a better QA model)
qa_pipeline = pipeline(
    "text-generation",
    model="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
    device=device
)

# ✅ Extract text from PDF
def extract_text_from_pdf(pdf_path):
    text_chunks = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                text_chunks.append(text)
    return text_chunks

# ✅ Answer user question based on extracted text
def answer_question_from_chunk(chunk, question):
    prompt = f"question: {question} context: {chunk}"  
    result = qa_pipeline(prompt)

    return result[0]['generated_text'] if result else "I couldn't find an answer."

# ✅ Streamlit Chatbot UI
st.title("📄 AI Chatbot for PDF Question Answering")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

# ✅ Load and extract text when a PDF is uploaded
if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Extract text
    document_chunks = extract_text_from_pdf("temp.pdf")
    st.success("✅ PDF uploaded and processed successfully!")

    # Chat interface
    st.subheader("💬 Ask questions about the document:")
    user_question = st.text_input("Type your question here...")

    if user_question:
        answer = None
        for chunk in document_chunks:
            answer = answer_question_from_chunk(chunk, user_question)
            if answer:  # Stop after finding an answer
                break

        st.write(f"**Answer:** {answer}")

