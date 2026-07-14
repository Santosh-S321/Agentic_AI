# 🤖 Lab Program 5 – Self-Correcting (Adaptive) RAG

## 📌 Overview

This project implements an **Adaptive Retrieval-Augmented Generation (Adaptive RAG)** system using **LangChain**, **ChromaDB**, **Hugging Face Embeddings**, and **Groq LLM**.

Unlike a basic RAG system, the Adaptive RAG agent evaluates its own response. If it cannot answer a question (returns **"I don't know"**), it automatically **rephrases the query** and searches the document again. This self-correcting behavior improves the chances of retrieving the correct information from the PDF.

The implementation is designed to run in **Google Colab** using free resources.

---

# 🎯 Aim

To build an Adaptive Retrieval-Augmented Generation (Adaptive RAG) system that:

- Loads a PDF document
- Splits the document into chunks
- Generates vector embeddings
- Stores embeddings in ChromaDB
- Retrieves relevant document chunks
- Generates answers using Groq LLM
- Evaluates its own response
- Automatically rephrases the query and retries if the answer is insufficient

---

# 🛠 Technologies Used

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

# 📚 Python Libraries

Install the required libraries:

```bash
pip install langchain langchain-community langchain-groq chromadb sentence-transformers pypdf
```

---

# 📂 Project Workflow

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
Groq LLM Generates Answer
      │
      ▼
Is Answer "I don't know"?
      │
   ┌──┴───────────────┐
   │                  │
  Yes                No
   │                  │
   ▼                  ▼
Rephrase Query     Return Answer
   │
   ▼
Retrieve Again
   │
   ▼
Generate New Answer
```

---

# 📁 Project Structure

```
Lab5_Adaptive_RAG/
│
├── Lab5_Adaptive_RAG.ipynb
├── sample.pdf
├── README.md
```

---

# ⚙️ Program Steps

## Step 1 – Install Libraries

Install all required Python packages.

---

## Step 2 – Upload PDF

Upload a PDF document and create the vector database (same as Lab 4).

---

## Step 3 – Load PDF

Use **PyPDFLoader** to read the document.

---

## Step 4 – Split the Document

Split the document into overlapping chunks.

Recommended settings:

- Chunk Size = 500
- Chunk Overlap = 50

---

## Step 5 – Generate Embeddings

Generate vector embeddings using the free Hugging Face model:

```
sentence-transformers/all-MiniLM-L6-v2
```

---

## Step 6 – Store in ChromaDB

Store all document embeddings in ChromaDB for semantic retrieval.

---

## Step 7 – Connect Groq LLM

Initialize the Groq language model using:

- Model: `llama-3.1-8b-instant`
- Temperature = 0

---

## Step 8 – Retrieve and Answer

Create a helper function that:

- Retrieves relevant document chunks
- Builds a context
- Generates an answer
- Returns **"I don't know"** if the answer is not present in the document

---

## Step 9 – Adaptive Self-Correction

If the model replies:

```
I don't know
```

the system:

1. Rephrases the original question.
2. Searches the vector database again.
3. Retrieves new context.
4. Generates another answer.
5. Repeats until:
   - A valid answer is found, or
   - The maximum retry limit is reached.

---

# ▶ Example Output

```
Attempt 1 with query:

What is the main conclusion of the document?

Response:

I don't know

-----------------------------------

Attempt 2 with query:

Summarise the document's final findings

Response:

The document concludes that...
```

---

# ✨ Features

- Upload any PDF document
- Automatic document chunking
- Semantic search using embeddings
- Vector storage with ChromaDB
- Question answering using Groq
- Automatic answer evaluation
- Self-correcting query rephrasing
- Multiple retrieval attempts
- Adaptive RAG implementation
- Uses completely free embedding models

---

# 📊 Adaptive RAG Architecture

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
                User asks Question
                         |
                         ▼
              Retrieve Relevant Chunks
                         |
                         ▼
                Groq Generates Answer
                         |
                         ▼
          Is answer "I don't know"?
                 │             │
              Yes             No
                 │             │
                 ▼             ▼
          Rephrase Query   Return Answer
                 │
                 ▼
          Search ChromaDB Again
                 │
                 ▼
          Generate New Answer
                 │
                 ▼
       Repeat Until Success or Limit
```

---

# 🔑 Requirements

- Google Colab
- Groq API Key
- Internet connection
- PDF document
- Hugging Face embedding model

---

# 🚀 How to Run

1. Open Google Colab.
2. Create a new notebook.
3. Install all required libraries.
4. Upload a PDF document.
5. Build the ChromaDB vector database.
6. Enter your Groq API key.
7. Run the helper function.
8. Execute the adaptive answer function.
9. Ask questions related to the uploaded PDF.
10. Observe automatic retries if the first answer is insufficient.

---

# 📖 Learning Outcomes

After completing this lab, you will understand how to:

- Build a Retrieval-Augmented Generation (RAG) system
- Generate document embeddings using Hugging Face
- Store vectors in ChromaDB
- Retrieve relevant document context
- Generate grounded answers using Groq
- Implement adaptive retrieval strategies
- Automatically evaluate answer quality
- Rephrase search queries using an LLM
- Design self-correcting AI workflows

---

# 📝 Result

An Adaptive Retrieval-Augmented Generation (Adaptive RAG) system was successfully implemented using LangChain, ChromaDB, Hugging Face embeddings, and Groq LLM. The system retrieves relevant information from a PDF document, generates context-aware answers, evaluates its own response, and automatically rephrases the query to retry when the initial answer is insufficient. This demonstrates self-correcting, agentic behavior with a bounded number of retrieval attempts.
