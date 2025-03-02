🤖 RAG-Based Question Answering System with LLaMA-2 & Mistral-7B



An advanced Retrieval-Augmented Generation (RAG) system using Hybrid Search, Conversational Memory, and Generative LLMs for high-accuracy question-answering. 🚀

📌 Features

✅ Conversational Memory (Multi-Turn Chat)✅ Hybrid Search (BM25 + FAISS) for Improved Retrieval✅ Adaptive Chunking (1000 tokens + 200 overlap)✅ ReRanker for Better Answer Selection✅ Instruction-Tuned Models for Higher Accuracy✅ Cloud Deployment (Streamlit, Hugging Face Spaces, AWS)✅ Fine-Tuning LLaMA-2 for Domain-Specific Q&A (Optional)

⚙️ Installation

# Clone this repository
git clone https://github.com/yourusername/RAG-QA-System.git
cd RAG-QA-System

# Install dependencies
pip install -r requirements.txt

🚀 Usage

Run the interactive chatbot:

python app.py

Or use the system in a Python script:

from your_rag_module import question_answer
user_query = "What is deep learning?"
response = question_answer({'question': user_query, 'context': retrieved_docs})
print(response['answer'])

📸 Screenshots



📚 How It Works

Retrieval 🔍: The system fetches relevant documents using BM25 + FAISS Hybrid Search.

ReRanking 📊: Uses a ReRanker to select the best passages.

Generation ✨: Passes context + question to Mistral-7B or LLaMA-2-13B.

Response 📝: Returns a human-like, context-aware answer.

🛠 Technologies Used

LLMs: LLaMA-2-13B, Mistral-7B

Retrieval: FAISS, BM25, LangChain

Search Ranking: ReRanker

Backend: Python, Hugging Face Transformers

Deployment: Streamlit, Hugging Face Spaces, AWS

🌟 Contributing

Want to improve this project? Feel free to submit a pull request!

📜 License

This project is licensed under the MIT License.

🌍 Connect with Me!



🚀 Star this repository if you like it! ⭐

