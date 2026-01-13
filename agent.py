import json
from typing import Dict

# -------- Mock Tool --------
def mock_lead_capture(name, email, platform):
    print(f"\n✅ Lead captured successfully: {name}, {email}, {platform}\n")


# -------- Load Knowledge Base --------
with open("knowledge_base.json", "r") as f:
    KB = json.load(f)


# -------- Intent Detection --------
def detect_intent(user_input: str) -> str:
    text = user_input.lower()

    # HIGH INTENT FIRST (absolute priority)
    high_intent_keywords = [
        "try",
        "sign up",
        "signup",
        "subscribe",
        "buy",
        "get pro",
        "go with pro",
        "choose",
        "select",
        "i want pro",
        "i will get",
        "i want to try",
        "i choose pro",
    ]

    if any(word in text for word in high_intent_keywords):
        return "high_intent"

    if any(word in text for word in ["hi", "hello", "hey"]):
        return "greeting"

    if any(word in text for word in ["price", "pricing", "cost", "plan", "pro", "basic"]):
        return "product_inquiry"

    return "other"


# -------- RAG Answering --------
def answer_with_rag(query: str) -> str:
    return (
        f"📦 AutoStream Pricing:\n"
        f"Basic Plan: {KB['pricing']['basic']['price']} "
        f"({KB['pricing']['basic']['videos']}, {KB['pricing']['basic']['resolution']})\n"
        f"Pro Plan: {KB['pricing']['pro']['price']} "
        f"({KB['pricing']['pro']['videos']}, {KB['pricing']['pro']['resolution']}, AI captions)"
    )


# -------- Agent State --------
state: Dict = {
    "name": None,
    "email": None,
    "platform": None
}


# -------- Main Loop --------
def run_agent():
    print("🤖 AutoStream Assistant started. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        intent = detect_intent(user_input)

        # 1️⃣ HIGH INTENT — ALWAYS WINS
        if intent == "high_intent":
            print("Agent: Great! I just need a few details to get you started.")

            state["name"] = input("Agent: What is your name? ")
            state["email"] = input("Agent: Your email address? ")
            state["platform"] = input("Agent: Which platform do you create on? ")

            mock_lead_capture(
                state["name"], state["email"], state["platform"]
            )
            break

        # 2️⃣ GREETING
        elif intent == "greeting":
            print("Agent: Hi! I can help you with AutoStream pricing or plans.")

        # 3️⃣ PRICING / PRODUCT
        elif intent == "product_inquiry":
            print("Agent:", answer_with_rag(user_input))

        # 4️⃣ FALLBACK
        else:
            print("Agent: Could you please clarify your question?")


# -------- Run --------
if __name__ == "__main__":
    run_agent()
