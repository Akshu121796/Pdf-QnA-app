# To run use: streamlit run app.py If not working then use: Python -m streamlit run app.py

import streamlit as st
import os
from google.generativeai import configure
configure(api_key=os.getenv("GOOGLE_API_KEY"))

from dotenv import load_dotenv
import pdfplumber
from langchain.text_splitter import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template
import asyncio
import nest_asyncio


nest_asyncio.apply()

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        try:
            with pdfplumber.open(pdf) as pdf_file:
                for page in pdf_file.pages:
                    text += page.extract_text() or ""
        except Exception as e:
            st.warning(f"Could not read {pdf.name} with pdfplumber: {str(e)}. Trying fallback method...")
            try:
                from PyPDF2 import PdfReader
                pdf_reader = PdfReader(pdf)
                for page in pdf_reader.pages:
                    text += page.extract_text() or ""
            except Exception as e:
                st.error(f"Failed to read {pdf.name}: {str(e)}")
                continue
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)
    memory = ConversationBufferMemory(
        memory_key='chat_history', 
        return_messages=True
    )
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory,
        get_chat_history=lambda h: h,
        verbose=True
    )
    return conversation_chain

def handle_userinput(user_question):
    if st.session_state.conversation is None:
        st.warning("Please process PDFs first before asking questions.")
        return
    
    try:
        response = st.session_state.conversation({'question': user_question})
        st.session_state.chat_history = response['chat_history']

        for i, message in enumerate(st.session_state.chat_history):
            if i % 2 == 0:
                st.write(user_template.replace(
                    "{{MSG}}", message.content), unsafe_allow_html=True)
            else:
                st.write(bot_template.replace(
                    "{{MSG}}", message.content), unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error getting response: {str(e)}")

def main():
    # Ensure event loop exists
    try:
        asyncio.get_event_loop()
    except RuntimeError:
        asyncio.set_event_loop(asyncio.new_event_loop())

    load_dotenv()
    st.set_page_config(page_title="Chat with PDFs and SkillUp",
                     page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Chat with PDFs and SkillUp  📝📚")
    st.header("Chat with our DocuBOT💡 | who will help you to skillup your knowledge \n He likes to eat lot of PDF and in return he will satisfies your query 😊")
    user_question = st.text_input("Ask a question about your documents:")
    if user_question:
        handle_userinput(user_question)

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader(
            "Upload your PDFs here and click on 'Process'", 
            accept_multiple_files=True,
            type=["pdf"])
            
        if st.button("Process"):
            if not pdf_docs:
                st.warning("Please upload at least one PDF file")
                return
                
            with st.spinner("Processing"):
                try:
                    raw_text = get_pdf_text(pdf_docs)
                    
                    if not raw_text.strip():
                        st.error("Could not extract any text from the PDFs. They may be scanned images or corrupted.")
                        return

                    text_chunks = get_text_chunks(raw_text)
                    vectorstore = get_vectorstore(text_chunks)
                    st.session_state.conversation = get_conversation_chain(vectorstore)
                    st.success("PDFs processed successfully with Gemini!")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    main()