import gradio as gr
import json
from .api_client import generate_plan
from .safety import validate_output
from .logging_utils import log_case

def run_workflow(note):
    raw = generate_plan(note)
    try:
        parsed = json.loads(raw)
    except:
        print("INVALID JSON FROM MODEL:", raw)
        return "ERROR", [], "", "", "", "Model returned invalid JSON"

    alerts = validate_output(parsed)
    log_case(note, parsed)

    return (
        parsed.get("triage_level"),
        parsed.get("medications"),
        "\n".join(parsed.get("warning_signs", [])),
        "\n".join(parsed.get("follow_up", [])),
        "\n".join(parsed.get("patient_instructions_simple", [])),
        "\n".join(alerts)
    )

with gr.Blocks(title="Post-Discharge Risk Copilot") as demo:
    gr.Markdown("# 🏥 Post-Discharge Risk Copilot")
    gr.Markdown("MedGemma-powered discharge safety assistant")

    with gr.Row():
        with gr.Column(scale=2):
            note_input = gr.Textbox(lines=10, label="Discharge Note")
            submit_btn = gr.Button("Generate Plan")

        with gr.Column(scale=3):
            triage = gr.Label(label="Triage Level")
            meds = gr.JSON(label="Medications")
            warnings = gr.Textbox(label="Warning Signs")
            followup = gr.Textbox(label="Follow-Up")
            patient = gr.Textbox(label="Patient Instructions")
            alerts = gr.Textbox(label="Safety Alerts")

    submit_btn.click(
        run_workflow,
        inputs=note_input,
        outputs=[triage, meds, warnings, followup, patient, alerts]
    )

demo.launch()