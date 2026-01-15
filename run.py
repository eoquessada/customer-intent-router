import dspy
from module import TicketRoutingModule
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    lm = dspy.LM(
        model="openai/gpt-4o-mini",
        api_key=OPENAI_API_KEY,
    )
    dspy.configure(lm=lm)

    system = TicketRoutingModule()
    system.load("artifacts/ticket_router.json")

    ticket_text = input("Enter the ticket text: ")

    result = system(ticket_text=ticket_text)

    print("Intent:", result["intent"])
    print("Routing decision:", result["routing_decision"])

