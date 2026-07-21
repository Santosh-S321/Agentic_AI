# Agentic AI Lab 1 – Tool-Using Agent with LangChain

## Project Overview

This project demonstrates how to build a **Tool-Using AI Agent** using **LangChain** and **Groq's Llama 3.1 model**.

The agent is capable of:
- Retrieving factual information from **Wikipedia**
- Performing arithmetic calculations using a **Calculator Tool**
- Solving **multi-step questions** using the **ReAct (Reason + Act)** approach.

Example:

> "Who developed the theory of relativity, and what is his birth year multiplied by 2?"

The agent:
1. Searches Wikipedia.
2. Finds Albert Einstein and his birth year.
3. Uses the Calculator tool.
4. Produces the final answer.

---

## Features

- LangChain ReAct Agent
- Groq Llama 3.1 Integration
- Wikipedia Tool
- Calculator Tool
- Multi-step reasoning
- Environment variable support using `.env`

---

## Technologies Used

- Python 3.9+
- LangChain
- LangChain Community
- LangChain Groq
- Wikipedia API
- python-dotenv

---

## Project Structure

```
agentic_lab1/
│
├── agent_lab1.py
├── README.md
├── requirements.txt
├── .env          # Not uploaded to GitHub
└── venv/
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Agentic_AI.git
cd Agentic_AI/agentic_lab1
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create a `.env` file

Create a file named `.env`

```env
GROQ_API_KEY=your_groq_api_key
```

---

## Run the Project

```bash
python agent_lab1.py
```

---

## Sample Output

```
> Entering new AgentExecutor chain...

Action: Wikipedia
Observation:
Albert Einstein developed the theory of relativity.

Action: Calculator
Observation:
3758

Final Answer:
The theory of relativity was developed by Albert Einstein, and his birth year multiplied by 2 is 3758.
```

---

## Learning Outcomes

Through this project, I learned how to:

- Build an AI agent using LangChain
- Integrate external tools into an AI workflow
- Use the ReAct reasoning pattern
- Manage API keys securely using `.env`
- Connect Groq LLMs with LangChain

