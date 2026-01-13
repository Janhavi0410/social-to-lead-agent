🧠 Social-to-Lead Conversational Agent

A lightweight conversational AI agent that demonstrates how product-focused conversations can be converted into qualified leads using intent detection, a local knowledge base, and simple state management.

This project simulates a real-world SaaS workflow where a user explores pricing, signals purchase intent, and is smoothly guided through a lead capture process—without unnecessary complexity or external dependencies.

🚀 Project Overview

The agent is built around a fictional SaaS product called AutoStream, an automated video editing platform for content creators.

The agent can:

Greet users and handle basic conversation flow

Answer pricing and plan-related questions

Detect high purchase intent

Collect lead information step-by-step (name, email, platform)

Trigger a lead capture action only after all required details are collected

This mirrors how early-stage AI assistants are used in production environments to qualify interest before handing users off to sales or onboarding systems.

🧠 Design Decisions
Intent Detection

Intent detection is implemented using rule-based keyword matching rather than a machine learning model.

This choice keeps the system:

Deterministic and predictable

Easy to debug and extend

Suitable for early-stage or prototype environments

High-intent queries (e.g., “I want the pro plan”) are prioritized over informational requests to avoid unnecessary interruptions once a user is ready to convert.

Knowledge Retrieval (RAG-lite)

Pricing and plan information is stored in a local knowledge_base.json file and retrieved at runtime.

This simulates a lightweight Retrieval-Augmented Generation (RAG) approach without:

Vector databases

Embeddings

External APIs

The result is a simple, transparent system that still reflects real-world architecture patterns.

State Management

The agent maintains an in-memory conversation state to track user-provided information during the session.

This enables:

Progressive data collection

Context-aware responses

Safe triggering of the lead capture process only when all required fields are present

🛠️ Tech Stack

Python 3

Standard libraries (json, typing)

CLI-based interaction

No external APIs or frameworks

Minimal dependencies. Maximum clarity. No drama.

📂 Project Structure
social-to-lead-agent/
├── agent.py              # Core conversational logic
├── knowledge_base.json   # Pricing and product data
├── requirements.txt      # Dependencies

▶️ How to Run

Clone the repository

git clone https://github.com/Janhavi0410/social-to-lead-agent.git


Navigate to the project directory

cd social-to-lead-agent


Install dependencies

pip install -r requirements.txt


Run the agent

python agent.py


Interact with the agent directly through the terminal.

💬 Sample Conversation Flow
User: hi
Agent: Hi! I can help you with AutoStream pricing or plans.

User: i want pricing
Agent: [Displays pricing details]

User: i want to try the pro plan
Agent: Great! I just need a few details to get you started.


The agent then collects the user’s name, email, and content platform before capturing the lead.

Simple. Linear. Effective.

🔮 Future Improvements

Replace rule-based intent detection with an ML-based classifier

Add persistent storage for captured leads

Integrate with messaging platforms (e.g., WhatsApp, Slack) via webhooks

Expand the knowledge base dynamically from external sources
