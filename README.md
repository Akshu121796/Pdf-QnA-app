# Pdf-QnA-app

# 📄 PDF Document Question Answering LLM System

A Streamlit-based app that lets you **chat with PDFs**. Upload a PDF document, and the app uses **Google Gemini API** + **LangChain** + **FAISS** to generate embeddings, retrieve relevant chunks, and answer your questions.

## 🚀 Features

* 📂 Upload one or multiple PDF documents
* 🤖 Ask natural language questions about the content
* 🔎 Uses **vector search (FAISS)** for retrieval
* ⚡ Powered by **Gemini 1.5 Flash/Pro** or custom embeddings
* 🖥️ Simple **Streamlit UI**

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create virtual environment (recommended)

```bash
python -m venv .venv
.venv\Scripts\activate   # On Windows
source .venv/bin/activate  # On Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up API Key

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_api_key_here
```
(If deploying on Streamlit Cloud, add this under **App → Settings → Secrets**.)

## ▶️ Run locally

```bash
streamlit run app.py
```

The app will be available at:
👉 [https://pdf-qna-app.streamlit.app/]

---

## 🌍 Deploy on Streamlit Cloud

1. Push your project to **GitHub**
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Select your repo and set `app.py` as the entry point
4. Add your `GOOGLE_API_KEY` in **Secrets**
5. Deploy 🎉

## 📦 Requirements

Dependencies are listed in `requirements.txt`, including:

* `streamlit`
* `python-dotenv`
* `google-generativeai`
* `langchain`
* `langchain-community`
* `faiss-cpu`
* `PyPDF2`
* `tiktoken`
* `numpy`
* `pandas`


## 🙌 Acknowledgements

* [Google Gemini API](https://ai.google.dev/)
* [LangChain](https://www.langchain.com/)
* [FAISS](https://github.com/facebookresearch/faiss)
* [Streamlit](https://streamlit.io/)
