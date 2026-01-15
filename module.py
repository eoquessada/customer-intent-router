import dspy
from signatures import ClassifyIntent, DecideRouting


class TicketRoutingModule(dspy.Module):
    def __init__(self):
        super().__init__()
        self.classify_intent = dspy.Predict(ClassifyIntent)
        self.decide_routing = dspy.Predict(DecideRouting)

    def forward(self, ticket_text: str):
        intent_result = self.classify_intent(
            ticket_text=ticket_text
        )

        routing_result = self.decide_routing(
            intent=intent_result.intent
        )

        return {
            "intent": intent_result.intent,
            "routing_decision": routing_result.routing_decision
        }
