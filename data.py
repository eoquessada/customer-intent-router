import dspy

train_examples = [
    dspy.Example(
        ticket_text="Quero solicitar o reembolso da minha compra.",
        intent="refund_request",
        routing_decision="auto_route"
    ).with_inputs("ticket_text"),

    dspy.Example(
        ticket_text="Meu pedido ainda não foi entregue e está atrasado.",
        intent="delivery_issue",
        routing_decision="auto_route"
    ).with_inputs("ticket_text"),

    dspy.Example(
        ticket_text="Não entendi como funciona o plano mensal.",
        intent="general_question",
        routing_decision="auto_route"
    ).with_inputs("ticket_text"),

    dspy.Example(
        ticket_text="Gostaria de saber o prazo de entrega do meu pedido.",
        intent="delivery_issue",
        routing_decision="auto_route"
    ).with_inputs("ticket_text"),

    dspy.Example(
        ticket_text="Estou muito insatisfeito e quero falar com um atendente humano agora.",
        intent="other",
        routing_decision="escalate_to_human"
    ).with_inputs("ticket_text"),

    dspy.Example(
        ticket_text="Meu pedido ainda não foi entregue e já passou do prazo.",
        intent="delivery_issue",
        routing_decision="auto_route"
    ).with_inputs("ticket_text"),

    dspy.Example(
        ticket_text="O rastreamento não atualiza e meu pedido está atrasado.",
        intent="delivery_issue",
        routing_decision="auto_route"
    ).with_inputs("ticket_text"),

    dspy.Example(
        ticket_text="Quero solicitar o reembolso da minha compra.",
        intent="refund_request",
        routing_decision="auto_route"
    ).with_inputs("ticket_text"),

    dspy.Example(
        ticket_text="Gostaria de cancelar o pedido e receber meu dinheiro de volta.",
        intent="refund_request",
        routing_decision="auto_route"
    ).with_inputs("ticket_text"),

    dspy.Example(
        ticket_text="Como funciona o plano mensal?",
        intent="general_question",
        routing_decision="auto_route"
    ).with_inputs("ticket_text"),

    dspy.Example(
        ticket_text="Quais são as formas de pagamento disponíveis?",
        intent="general_question",
        routing_decision="auto_route"
    ).with_inputs("ticket_text"),

    dspy.Example(
        ticket_text="Estou muito insatisfeito e quero falar com um atendente humano agora.",
        intent="other",
        routing_decision="escalate_to_human"
    ).with_inputs("ticket_text"),

    dspy.Example(
        ticket_text="Isso é um absurdo, ninguém resolve meu problema!",
        intent="other",
        routing_decision="escalate_to_human"
    ).with_inputs("ticket_text"),
]
