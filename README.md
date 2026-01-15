# Customer Intent Router

## Objetivo do Sistema

Este sistema classifica tickets de atendimento ao cliente e decide se eles podem ser tratados automaticamente ou se devem ser encaminhados para um agente humano.
Ele é utilizado como uma etapa inicial de triagem em operações de suporte, ajudando a reduzir carga manual e melhorar o roteamento de tickets.
O sistema não interage diretamente com o cliente nem executa ações operacionais.

## Como Rodar o Projeto

### Pré-requisitos
- Python 3.8+
- pip

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/eoquessada/customet-intent-router.git
cd customer_intent_router
```

2. Crie um ambiente virtual:
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows PowerShell
# ou
source .venv/bin/activate  # Linux/Mac
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Crie um arquivo `.env` na raiz do projeto com sua API key:
```
OPENAI_API_KEY=sua_api_key_aqui
```

### Executar o Projeto

```bash
python run.py
```

### Otimizar o Sistema

Para treinar/otimizar o sistema com novos exemplos:
```bash
python optimize.py
```

## Escopo Funcional

O sistema é capaz de:
- Analisar o texto de um ticket de atendimento
- Classificar a intenção principal do ticket
- Decidir se o ticket é simples ou complexo
- Indicar se o ticket pode seguir um fluxo automatizado ou deve ser escalado para um humano

## Tipos de Intenção 

Todo ticket deve ser classificado em exatamente uma das intenções abaixo:

- refund_request
- delivery_issue
- general_question
- other

## Decisão de Encaminhamento

Após a classificação da intenção, o sistema deve tomar exatamente uma decisão:

- auto_route
- escalate_to_human
