import dspy
from dotenv import load_dotenv
import os
from typing import Literal

load_dotenv()  
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

lm = dspy.LM(
    model="openai/gpt-4o-mini",
    api_key=OPENAI_API_KEY,
)
dspy.configure(lm=lm)

class ClassifyIntent(dspy.Signature):
    ticket_text: str = dspy.InputField(
        desc="Raw text of the customer support ticket"
    )

    intent: Literal[
        "refund_request",
        "delivery_issue",
        "general_question",
        "payment_issue",
        "other"
    ] = dspy.OutputField(
        desc="Primary intent of the ticket"
    )

class DecideRouting(dspy.Signature):
    intent: Literal[
        "refund_request",
        "delivery_issue",
        "general_question",
        "payment_issue",
        "other"
    ] = dspy.InputField(
        desc="Previously classified ticket intent"
    )

    routing_decision: Literal[
        "auto_route",
        "escalate_to_human"
    ] = dspy.OutputField(
        desc="Final routing decision"
    )

