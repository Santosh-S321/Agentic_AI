# Lab Program 2 – A Chatbot that Remembers using LangGraph

## Overview

This project demonstrates how to build a simple conversational chatbot using **LangGraph** and the **Groq LLM API**. Unlike a basic chatbot, this implementation maintains a **State** that stores the user's name and preferences, allowing the chatbot to remember information across multiple conversation turns.

The project is designed to run in **Google Colab**.

---

## Objective

Implement a basic conversation loop using **LangGraph** where the chatbot maintains a state to remember:

- User's name
- User's preferences
- Conversation history

---

## Technologies Used

- Python
- Google Colab
- LangGraph
- LangChain Groq
- Groq API (Llama 3.1 8B Instant)

---

## Project Structure

```
Lab2_LangGraph.ipynb
README.md
```

---

## Installation

Install the required libraries:

```bash
pip install langgraph langchain-groq
```

---

## Configuration

Create a Groq API key from:

https://console.groq.com

Replace:

```python
api_key="PASTE_YOUR_GROQ_KEY_HERE"
```

with your own API key.

---

## Features

- Maintains conversation state using LangGraph
- Remembers the user's name
- Remembers user preferences
- Uses Groq's Llama 3.1 model for responses
- Interactive command-line conversation loop

---

## Example Conversation

```
You: My name is Riya and I like cricket

Bot: Nice to meet you, Riya! Cricket is great.

You: What is my name and what do I like?

Bot: Your name is Riya and you like cricket.
```

---

## Learning Outcomes

After completing this lab, you will understand how to:

- Build a simple LangGraph workflow
- Create and use a Typed State
- Maintain memory across multiple chat turns
- Connect LangGraph with the Groq API
- Develop a stateful conversational chatbot

---

## Result

A LangGraph-based chatbot was successfully implemented. By maintaining a typed state object, the chatbot remembered the user's name and preferences throughout the conversation, demonstrating persistent memory across multiple interactions.

