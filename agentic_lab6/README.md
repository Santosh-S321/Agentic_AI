# 🤖 Lab Program 6 – Two Agents: Writer & Critic (AutoGen)

## 📌 Overview

This project demonstrates a **multi-agent AI system** using **AutoGen** and **Groq LLM**. Two AI agents—a **Writer** and a **Critic**—collaborate to produce high-quality content through iterative feedback.

The **Writer Agent** generates an initial blog post based on a given topic. The **Critic Agent** reviews the draft, identifies areas for improvement, and provides constructive feedback. The Writer then revises the content based on the Critic’s suggestions. This process continues until the Critic approves the final version.

The implementation is designed to run in **Google Colab** using the free **Groq API**.

---

# 🎯 Aim

To implement a multi-agent collaboration system using AutoGen where:

- A **Writer Agent** creates a blog post.
- A **Critic Agent** reviews the draft.
- The Writer revises the content based on the feedback.
- The process continues until the Critic approves the final version.

---

# 🛠 Technologies Used

- Python 3
- Google Colab
- AutoGen (pyautogen)
- Groq API
- Llama 3.1 8B Instant
- OpenAI-Compatible API

---

# 📚 Python Libraries

Install the required library:

```bash
pip install pyautogen
```

---

# 📂 Project Workflow

```
          User Task
              │
              ▼
      Writer Agent Creates
        Initial Blog Post
              │
              ▼
      Critic Agent Reviews
          the Blog Post
              │
              ▼
     Feedback / Suggestions
              │
              ▼
      Writer Revises Draft
              │
              ▼
       Critic Reviews Again
              │
       ┌──────┴──────┐
       │             │
   Needs Changes   APPROVED
       │             │
       ▼             ▼
 Rewrite Again   Final Blog Post
```

---

# 📁 Project Structure

```
Lab6_AutoGen/
│
├── Lab6_AutoGen.ipynb
└── README.md
```

---

# ⚙️ Program Steps

## Step 1 – Install AutoGen

Install the required AutoGen library.

---

## Step 2 – Configure Groq

Configure the Groq API using the OpenAI-compatible endpoint.

Model used:

```
llama-3.1-8b-instant
```

Temperature:

```
0.4
```

---

## Step 3 – Create the Writer Agent

The Writer Agent is responsible for:

- Writing clear and concise blog posts.
- Improving the content based on feedback.
- Producing revised versions until approval.

---

## Step 4 – Create the Critic Agent

The Critic Agent is responsible for:

- Reviewing the Writer's draft.
- Providing 2–3 specific suggestions.
- Approving the final version when the quality is satisfactory.

---

## Step 5 – Start Collaboration

The Critic initiates the conversation with the Writer by providing a writing task.

Example task:

```
Write a 150-word blog post about the benefits of reading.
```

---

## Step 6 – Iterative Improvement

The agents collaborate through multiple rounds:

1. Writer generates the first draft.
2. Critic reviews the draft.
3. Writer revises the draft.
4. Critic reviews again.
5. Process repeats until the Critic replies:

```
APPROVED
```

---

# ▶ Example Output

```
Writer:

Reading is one of the best habits that helps people
gain knowledge and improve imagination...

-----------------------------------------

Critic:

Good introduction.

Suggestions:

• Include a real-life example.
• Make the conclusion stronger.
• Shorten the first paragraph.

-----------------------------------------

Writer:

(Improved blog post)

-----------------------------------------

Critic:

APPROVED
```

---

# ✨ Features

- Multi-agent collaboration
- Writer and Critic AI agents
- Automatic iterative feedback
- Content refinement through multiple revisions
- Groq-powered language generation
- AutoGen conversation management
- OpenAI-compatible API integration
- Google Colab compatible
- Uses free Groq API

---

# 📊 Multi-Agent Architecture

```
                    User Prompt
                         │
                         ▼
               Writer Agent Creates
                  Initial Draft
                         │
                         ▼
                Critic Agent Reviews
                         │
          ┌──────────────┴──────────────┐
          │                             │
     Needs Improvement            APPROVED
          │                             │
          ▼                             ▼
   Writer Revises Draft         Final Blog Post
          │
          └──────────────► Repeat
```

---

# 🔑 Requirements

- Google Colab
- Groq API Key
- Internet connection
- Python 3

---

# 🚀 How to Run

1. Open Google Colab.
2. Create a new notebook.
3. Install the AutoGen library.
4. Enter your Groq API key.
5. Configure the language model.
6. Create the Writer Agent.
7. Create the Critic Agent.
8. Run the collaboration script.
9. Observe the iterative conversation between the agents.
10. View the final approved blog post.

---

# 📖 Learning Outcomes

After completing this lab, you will understand how to:

- Build multi-agent AI systems using AutoGen
- Configure Groq with an OpenAI-compatible API
- Design AI agents with different roles
- Enable collaboration between multiple agents
- Implement iterative feedback loops
- Improve AI-generated content through self-review
- Develop agentic AI workflows
- Simulate collaborative writing using LLMs

---

# 📝 Result

A multi-agent writing system was successfully implemented using AutoGen and Groq LLM. Two AI agents—a Writer and a Critic—collaborated through multiple rounds of feedback to generate and refine a blog post. The iterative process demonstrated how agentic AI systems can improve content quality through autonomous collaboration and constructive critique.
