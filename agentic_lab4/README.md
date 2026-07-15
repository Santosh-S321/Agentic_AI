# 📄 Lab Program 4 – Ask Questions About a PDF (RAG)

## 📌 Overview

This project demonstrates **Retrieval-Augmented Generation (RAG)** using **LangChain**, **ChromaDB**, **Hugging Face Embeddings**, and **Groq LLM**.

Instead of relying only on the language model's knowledge, the application first retrieves the most relevant information from a PDF document and then generates an answer based on that retrieved content.

This implementation is designed to run in **Google Colab** using free resources.

---

## 🎯 Aim

To build a Retrieval-Augmented Generation (RAG) system that:

- Loads a local PDF document
- Splits it into smaller chunks
- Converts chunks into vector embeddings
- Stores embeddings in ChromaDB
- Retrieves relevant chunks for a user's question
- Uses Groq LLM to generate accurate answers based on the retrieved content

---

## 🛠 Technologies Used

- Python 3
- Google Colab
- LangChain
- LangChain Community
- LangChain Groq
- ChromaDB
- Hugging Face Sentence Transformers
- PyPDF
- Groq API

---

## 📚 Python Libraries

Install the required packages:

```bash
pip install langchain langchain-community langchain-groq chromadb sentence-transformers pypdf
```

---

## 📂 Project Workflow

```
PDF Document
      │
      ▼
Load PDF
      │
      ▼
Split into Chunks
      │
      ▼
Generate Embeddings
(Hugging Face)
      │
      ▼
Store in ChromaDB
      │
      ▼
User Question
      │
      ▼
Retrieve Relevant Chunks
      │
      ▼
Groq LLM
      │
      ▼
Final Answer
```

---

## 📁 Project Structure

```
Lab4_PDF_RAG/
│
├── Lab4_PDF_RAG.ipynb
├── sample.pdf
├── README.md
```

---

## ⚙️ Program Steps

### Step 1 – Install Libraries

Install all required Python packages.

---

### Step 2 – Upload PDF

Upload any PDF document from your local computer.

---

### Step 3 – Load PDF

Use **PyPDFLoader** to read the document.

---

### Step 4 – Split Document

Split the PDF into overlapping chunks using:

- Chunk Size = 500
- Chunk Overlap = 50

This improves retrieval quality.

---

### Step 5 – Create Embeddings

Generate vector embeddings using:

```
sentence-transformers/all-MiniLM-L6-v2
```

This is a free Hugging Face embedding model.

---

### Step 6 – Store in ChromaDB

Store all embeddings inside ChromaDB to enable semantic search.

---

### Step 7 – Ask Questions

Use Groq's Llama model to answer user questions using only the retrieved document chunks.

Example:

```
What is this document about?
```

---

## ▶ Example Output

```
Uploaded: sample.pdf

Number of chunks: 24

Vector database ready!

This document explains the concepts of...
```

---

## ✨ Features

- Upload any PDF document
- Automatic document chunking
- Semantic search using embeddings
- Fast vector retrieval with ChromaDB
- Context-aware answers
- Uses free Hugging Face embeddings
- Powered by Groq Llama 3.1

---

## 📊 RAG Pipeline

```
                +----------------+
                |   PDF File     |
                +-------+--------+
                        |
                        ▼
              Load PDF Document
                        |
                        ▼
               Split into Chunks
                        |
                        ▼
         Hugging Face Embeddings
                        |
                        ▼
                  ChromaDB Store
                        |
            User asks a Question
                        |
                        ▼
              Retrieve Best Chunks
                        |
                        ▼
                 Groq LLM Answer
                        |
                        ▼
               Context-Based Response
```

---

## 🔑 Requirements

- Google Colab
- Groq API Key
- Internet connection
- Any PDF document

---

## 🚀 How to Run

1. Open Google Colab.
2. Create a new notebook.
3. Install all required libraries.
4. Upload a PDF.
5. Create embeddings.
6. Store vectors in ChromaDB.
7. Enter your Groq API key.
8. Run the notebook.
9. Ask questions about the uploaded PDF.

---

## 📌 Learning Outcomes

After completing this lab, you will understand how to:

- Read PDF documents using LangChain
- Split large documents into chunks
- Generate semantic embeddings
- Build a vector database
- Perform similarity search
- Implement Retrieval-Augmented Generation (RAG)
- Generate grounded responses using Groq LLM

---

## 📝 Result

A working Retrieval-Augmented Generation (RAG) application was successfully developed using LangChain, ChromaDB, Hugging Face embeddings, and Groq LLM. The system loads a PDF document, converts it into searchable vector embeddings, retrieves the most relevant information, and generates accurate answers grounded in the document content rather than relying solely on the language model's knowledge.
