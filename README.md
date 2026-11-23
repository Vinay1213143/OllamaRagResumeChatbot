# 🤖 Resume Chatbot – AI-Powered RAG Application

An AI-powered Resume Chatbot built using **Python, Streamlit, LangChain, Ollama, and ChromaDB**. This application uses **Retrieval-Augmented Generation (RAG)** to answer questions based on indexed resume documents using locally running Large Language Models (LLMs).

Users can ask questions about skills, education, projects, experience, and other information available in the resume.

## 🚀 Features

- 💬 Interactive chatbot interface using Streamlit.
- 🧠 Retrieval-Augmented Generation (RAG) architecture.
- 🔍 Semantic document search using ChromaDB.
- 🤖 Local LLM integration using Ollama.
- 📄 Resume-based question answering.
- 📚 Displays retrieved document sources and page numbers.
- 🔒 Runs locally without requiring cloud-based LLM APIs.
- 🎯 Context-based responses to reduce hallucinations.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core Programming Language |
| Streamlit | Web Application Interface |
| LangChain | RAG Pipeline |
| Ollama | Local LLM Integration |
| Llama 3.2 | Text Generation |
| ChromaDB | Vector Database |
| Nomic Embed Text | Text Embeddings |

## 🏗️ Project Architecture

```text
          Resume Document
                 |
                 v
        Document Processing
                 |
                 v
          Text Chunking
                 |
                 v
       Nomic Text Embeddings
                 |
                 v
             ChromaDB
                 |
                 |
User Question --> Streamlit UI
                 |
                 v
          LangChain Retriever
                 |
                 v
       Retrieve Relevant Chunks
                 |
                 v
          Prompt Template
                 |
                 v
          Ollama LLM
           (Llama 3.2)
                 |
                 v
          Generated Answer
                 |
                 v
          Display in Streamlit
```


## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Vinay1213143/Resume-RAG-Chatbot.git
```

### 2. Navigate to the Project Folder

```bash
cd Resume-RAG-Chatbot
```

### 3. Install Dependencies

```bash
pip install streamlit langchain-ollama langchain-chroma langchain-core
```

### 4. Install Ollama

Download Ollama from:

https://ollama.com/

### 5. Pull Required Models

Download the Llama 3.2 model:

```bash
ollama pull llama3.2
```

Download the embedding model:

```bash
ollama pull nomic-embed-text
```

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## 💡 Example Questions

You can ask questions such as:

- Which programming languages are mentioned in the resume?
- What are the technical skills?
- Which projects are mentioned?
- What is the candidate's educational qualification?
- Which frameworks and technologies are used?
- Does the resume mention internship experience?

## 🔍 How It Works

1. Resume documents are processed and converted into text chunks.
2. Text chunks are converted into vector embeddings using Nomic Embed Text.
3. Embeddings are stored in ChromaDB.
4. When a user asks a question, the retriever searches for the three most relevant document chunks.
5. Retrieved information is passed to the Llama 3.2 model through a LangChain prompt template.
6. The LLM generates an answer based only on the retrieved context.
7. The application displays the answer along with retrieved source documents.

## 🔐 Important Note

This application uses a locally running LLM through Ollama. The ChromaDB database must be populated with indexed resume documents before asking questions.

If the requested information is unavailable in the retrieved context, the chatbot responds:

"I could not find this information in the provided documents."

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Generative AI and Large Language Models (LLMs).
- Retrieval-Augmented Generation (RAG).
- Vector databases and semantic search.
- LangChain integration.
- Local AI model deployment using Ollama.
- Building interactive applications using Streamlit.

## 👨‍💻 Author

**Vinay Awari**

Computer Science Engineering Graduate | Python Developer | Generative AI Enthusiast

- GitHub: https://github.com/Vinay1213143

---

⭐ If you find this project useful, don't forget to star the repository!
