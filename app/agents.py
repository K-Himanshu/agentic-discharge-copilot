from .medgemma import generate_json_response

def build_messages(note: str):
    return [
        {
            "role": "system",
            "content": "You are a senior clinical discharge copilot..."
        },
        {
            "role": "user",
            "content": f"""
Convert the following discharge note into STRICT JSON.

[Insert your final schema prompt here]

Discharge Note:
{note}
"""
        }
    ]


def run_discharge_agent(note: str):
    messages = build_messages(note)
    response = generate_json_response(messages)
    return response