import gradio as gr
from agent import build_recovery_plan


def generate_plan(discharge_text):
    return build_recovery_plan(discharge_text)


iface = gr.Interface(
    fn=generate_plan,
    inputs=gr.Textbox(lines=20, placeholder="Paste discharge summary here..."),
    outputs=gr.Markdown(),
    title="Agentic Post-Discharge Copilot",
    description="AI-powered assistant that extracts medications, warning signs, and recovery guidance from hospital discharge notes."
)

iface.launch(share=True)