from fastapi import FastAPI
from .agents import run_discharge_agent
from .logging_utils import log_case
import json

app = FastAPI()

@app.post("/generate")
def generate(note: str):
    raw_response = run_discharge_agent(note)

    parsed = json.loads(raw_response)

    log_case(note, parsed)

    return parsed