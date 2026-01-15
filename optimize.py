import dspy
from module import TicketRoutingModule
from data import train_examples
from dotenv import load_dotenv
import os


def routing_metric(example, prediction, trace=None):
    intent_correct = example.intent == prediction["intent"]
    routing_correct = example.routing_decision == prediction["routing_decision"]
    return intent_correct and routing_correct


if __name__ == "__main__":
    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    lm = dspy.LM(
        model="openai/gpt-4o-mini",
        api_key=OPENAI_API_KEY,
    )
    dspy.configure(lm=lm)

    optimizer = dspy.BootstrapFewShot(
        metric=routing_metric,
        max_bootstrapped_demos=5
    )

    system = TicketRoutingModule()

    optimized_system = optimizer.compile(
        system,
        trainset=train_examples
    )

    optimized_system.save("artifacts/ticket_router.json")