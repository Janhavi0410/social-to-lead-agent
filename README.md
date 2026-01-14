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

## WhatsApp Integration (Conceptual)

To integrate this conversational agent with WhatsApp, the system would use the WhatsApp Business API in combination with a webhook-based backend service.

Incoming WhatsApp messages from users would be forwarded to a webhook endpoint hosted by the application (for example, using a lightweight framework such as FastAPI or Flask). Each incoming message would include the user’s WhatsApp number, message content, and metadata. This message would then be passed to the agent logic for intent detection and response generation.

The agent’s conversation state (such as name, email, and creator platform) would be stored against the user’s WhatsApp ID, allowing the agent to maintain context across multiple message exchanges. Based on the detected intent, the agent would either respond with pricing information retrieved from the knowledge base or initiate the lead qualification flow.

Once all required lead details are collected, the mock lead capture function could be replaced with a real backend service or CRM integration. The agent’s response would then be sent back to the user via the WhatsApp Business API, completing the conversational loop.

This webhook-based architecture allows the agent to scale easily, handle multiple concurrent conversations, and integrate seamlessly with existing business systems while maintaining controlled and predictable agent behavior.

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
