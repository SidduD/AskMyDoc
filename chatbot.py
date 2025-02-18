import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from dotenv import load_dotenv
 
import os

# Load environment variables
load_dotenv()
 
# Google API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") 
 


#Upload PDF files
st.header("My first Chatbot")
 
 
with  st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader(" Upload a PDf file and start asking questions", type="pdf")
 
 
#Extract the text
if file is not None:
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
        #st.write(text)
 
 
#Break it into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators="\n",
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    #st.write(chunks)
 
 
    # generating embedding - Changed to GoogleGenerativeAiEmbeddings
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")  # You can specify the model
 
    # creating vector store - FAISS
    vector_store = FAISS.from_texts(chunks, embeddings)
 
    # get user question
    user_question = st.text_input("Type Your question here")
 
    # do similarity search
    if user_question:
        match = vector_store.similarity_search(user_question)
        #st.write(match)
 
        #define the LLM - Changed to ChatGoogleGenerativeAI
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.0)  # Specify the Gemini model
 
        #output results
        #chain -> take the question, get relevant document, pass it to the LLM, generate the output
        chain = load_qa_chain(llm, chain_type="stuff")
        response = chain.run(input_documents = match, question = user_question)
        st.write(response)