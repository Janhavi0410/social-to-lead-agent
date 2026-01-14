# Social-to-Lead Conversational Agent

"This implementation focuses on agentic flow, intent handling, and controlled tool execution using deterministic logic. While an LLM-based framework such as LangGraph or AutoGen could be integrated, a rule-based approach was chosen here to ensure predictability, debuggability, and clarity of reasoning within the assignment scope.”

A lightweight conversational AI agent that converts product-related conversations into **qualified leads** using intent detection and a local knowledge base.

Built as a CLI-based prototype to demonstrate how early-stage AI assistants can qualify interest before initiating lead capture.

---

## 🚀 What This Agent Does

The agent simulates interactions for a fictional SaaS product called **AutoStream**, an automated video editing platform for content creators.

**Core capabilities:**
- Handles basic user greetings
- Answers pricing and plan-related questions
- Detects high purchase intent
- Collects lead details (name, email, platform)
- Captures leads only after all required information is provided

---

## 🧠 Architecture & Design Choices

### Intent Detection
- Rule-based keyword matching
- Deterministic and easy to debug
- High-intent queries are prioritized over informational ones

This approach avoids unnecessary complexity while remaining production-realistic for early-stage systems.

---

### Knowledge Retrieval (RAG-lite)
- Pricing and plan data stored in `knowledge_base.json`
- Retrieved at runtime
- No embeddings, vector databases, or external APIs

This simulates a simple Retrieval-Augmented Generation workflow without overengineering.

---

### State Management
- In-memory conversation state
- Tracks user-provided lead details
- Triggers lead capture only when all required fields are collected

---

## 🛠️ Tech Stack

- Python 3
- Standard libraries (`json`, `typing`)
- Command-line interface
- No external services or APIs

---

## 📂 Project Structure

```text
social-to-lead-agent/
├── agent.py
├── knowledge_base.json
├── requirements.txt

````
## ▶️ Running the Project

git clone https://github.com/Janhavi0410/social-to-lead-agent.git
cd social-to-lead-agent
pip install -r requirements.txt
python agent.py

---

## 💬 Example Interaction
User: hi
Agent: Hi! I can help you with AutoStream pricing or plans.

User: i want pricing
Agent: [Displays pricing details]

User: i want to try the pro plan
Agent: Great! I just need a few details to get you started.

---

## 🔮 Possible Extensions

- ML-based intent classification
- Persistent lead storage
- Messaging platform integrations (e.g., WhatsApp, Slack)
- Dynamic knowledge base expansion

---
