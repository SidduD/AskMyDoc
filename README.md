# Chatbot AI - GeminiAI

This project is a Streamlit-based chatbot that allows users to upload PDF files, extract text, and interact through a question-answering interface powered by Google Cloud's generative AI models. The chatbot uses advanced text processing techniques to break down the document, generate embeddings, and provide accurate responses to user queries based on the uploaded content.

## Tools & Technologies Used

### 1. Streamlit
Streamlit is used to build the web interface for the chatbot. The app allows users to upload PDF files and interact with the chatbot through a simple and intuitive interface.

### 2. PyPDF2
PyPDF2 is used for extracting text from uploaded PDF files. It processes each page and converts it into readable text for further analysis.

### 3. Langchain
Langchain is a framework for building applications with LLMs (Large Language Models). It integrates with Google Generative AI for embeddings and question answering.

#### Components Used:
- **RecursiveCharacterTextSplitter**: Splits the extracted text from the PDF into manageable chunks for more efficient processing.
- **GoogleGenerativeAIEmbeddings**: Generates embeddings for text chunks, enabling the chatbot to process and understand the content.
- **FAISS**: A vector store used for storing and querying embeddings for similarity searches.
- **ChatGoogleGenerativeAI**: Leverages Google Cloud's Gemini models to generate AI-based responses based on the query and the context of the uploaded document.
- **load_qa_chain**: Integrates the question-answering logic to match the user's query with the relevant document chunks.

### 4. Google Cloud AI (Gemini)
Google Generative AI, specifically the gemini-1.5-flash model, is used to provide intelligent responses to user queries based on the context of the uploaded document.

### 5. FAISS (Facebook AI Similarity Search)
FAISS is a library used for efficient similarity search in high-dimensional spaces. It stores the embeddings generated from the document text and enables fast similarity searches when a user asks a question.

### 6. dotenv
The dotenv library is used to load environment variables, such as the Google API key, from a `.env` file. This keeps sensitive credentials secure and separate from the source code.

## How to Use

### Clone the Repository:

```bash
git clone https://github.com/yourusername/chatbot-ai-geminiAI.git
cd chatbot-ai-geminiAI

# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install the required dependencies
pip install -r requirements.txt

```
### Set Up Google Cloud API Key

To use the Google Cloud AI models, you need to set up an API key:

Visit the [Google AI Studio](https://aistudio.google.com/welcome)
Next, you need to create a `.env` file to securely store your API key:

1. In the root of your project directory, create a `.env` file.
2. Inside the `.env` file, add the following line with your actual API key:

```plaintext
GOOGLE_API_KEY="your-google-api-key-here"
```

### Run the Streamlit App
```bash
streamlit run chatbot.py
  
