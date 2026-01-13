# Social-to-Lead Conversational Agent

This project is a simple conversational AI agent built to demonstrate how product-related conversations can be converted into qualified leads using intent detection and a local knowledge base.

The agent simulates a real-world workflow where a user asks about pricing, shows interest in a product, and is then guided through a lead capture process.

---

## 🚀 Project Overview

The agent is designed for a fictional SaaS product called **AutoStream**, which provides automated video editing tools for content creators.

The agent can:
- Greet users
- Answer pricing and plan-related questions
- Detect high purchase intent
- Collect lead details (name, email, platform)
- Trigger a lead capture tool only after all required information is collected

This mirrors how early-stage AI assistants are used in real products to qualify and convert interested users.

---

## 🧠 Design Approach & Decisions

### Intent Detection
Intent detection is implemented using **rule-based keyword matching** instead of a machine learning classifier.  
This was a deliberate choice to keep the system deterministic, easy to debug, and predictable for an early-stage product.

High-intent detection is prioritized over informational queries to ensure that users who express purchase intent are not interrupted by additional pricing responses.

### Knowledge Retrieval (RAG)
Pricing and policy information is stored in a local JSON file and retrieved at runtime.  
This simulates a lightweight Retrieval-Augmented Generation (RAG) setup without adding unnecessary complexity such as vector databases or embeddings.

### State Management
The agent maintains a simple in-memory state to track user-provided details during the conversation.  
This allows the agent to collect information step-by-step and trigger the lead capture tool only when all required data is available.

---

## 🛠️ Tech Stack

- Python 3
- Standard Python libraries (`json`, `typing`)
- CLI-based interaction (no external APIs required)

---

## 📂 Project Structure

```text
social-to-lead-agent/
├── agent.py
├── knowledge_base.json
├── requirements.txt


## ▶️ How to Run the Project

1. **Clone the repository**
   ```bash
   git clone https://github.com/Janhavi0410/social-to-lead-agent.git
Navigate to the project directory

bash
Copy code
cd social-to-lead-agent
Install dependencies

bash
Copy code
pip install -r requirements.txt
Run the agent

bash
Copy code
python agent.py
Interact with the agent through the terminal.

💬 Sample Conversation Flow
vbnet
Copy code
User: hi
Agent: Hi! I can help you with AutoStream pricing or plans.

User: i want pricing
Agent: [Displays pricing details]

User: i want to try the pro plan
Agent: Great! I just need a few details to get you started.
The agent then collects the user’s name, email, and creator platform before capturing the lead.

🔮 Future Improvements
Replace rule-based intent detection with an ML-based classifier

Add persistent storage for captured leads

Integrate with messaging platforms such as WhatsApp using webhooks

Expand the knowledge base dynamically from external sources

