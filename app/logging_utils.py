import json
from datetime import datetime

def log_case(input_note, output_json):
    record = {
        "timestamp": str(datetime.utcnow()),
        "input": input_note,
        "output": output_json
    }

    with open("audit_log.json", "a") as f:
        f.write(json.dumps(record) + "\n")