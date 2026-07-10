# Lab Program 3 – Human-in-the-Loop: Approve Before Sending

## Overview

This project demonstrates the concept of **Human-in-the-Loop (HITL)** using the **Groq LLM API**. The AI generates an email draft based on a user's request but pauses execution before sending it. The email is only considered "sent" after a human reviews the draft and types **APPROVED**, ensuring that the final decision remains under human control.

The project is designed to run in **Google Colab**.

---

## Objective

Create an AI agent that:

- Generates an email draft using a Large Language Model (LLM)
- Waits for human review before proceeding
- Sends the email only when the user types **APPROVED**
- Rejects the email for any other input

---

## Technologies Used

- Python
- Google Colab
- LangChain Groq
- Groq API (Llama 3.1 8B Instant)

---

## Project Structure

```
Lab3_HITL.ipynb
README.md
```

---

## Installation

Install the required library:

```bash
pip install langchain-groq
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

- Generates professional email drafts using AI
- Implements a Human-in-the-Loop (HITL) approval process
- Prevents execution until human approval is received
- Demonstrates a basic AI safety checkpoint
- Interactive terminal-based workflow

---

## Example Run

```
----- DRAFT EMAIL -----

Dear Professor,

I am writing to request a short extension for my assignment due to unforeseen circumstances. I would greatly appreciate your consideration.

Thank you for your understanding.

Sincerely,
Student

Type APPROVED to send, or anything else to reject:

APPROVED

✅ Email sent!
```

If any input other than **APPROVED** is entered:

```
❌ Not sent. The draft was rejected.
```

---

## Learning Outcomes

After completing this lab, you will understand how to:

- Connect Python applications with the Groq LLM API
- Generate AI-powered email drafts
- Implement Human-in-the-Loop (HITL) workflows
- Add manual approval checkpoints to AI applications
- Improve AI safety by keeping humans in control of important actions

---

## Result

A Human-in-the-Loop (HITL) agent was successfully implemented in Google Colab. The agent generated an email draft using the Groq language model and paused execution until the user reviewed the content and typed **APPROVED**, demonstrating a simple but effective human approval mechanism before completing the action.
