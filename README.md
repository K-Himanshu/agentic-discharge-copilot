agentic-discharge-copilot/
│
├── app/
│   ├── main.py              ← FastAPI entrypoint
│   ├── models.py            ← Pydantic schemas
│   ├── medgemma.py          ← Model loading + inference
│   ├── agents.py            ← Risk + Plan agents
│   ├── safety.py            ← Rule-based validator
│   └── logging_utils.py     ← Audit logging
│
├── requirements.txt
├── README.md
└── .env