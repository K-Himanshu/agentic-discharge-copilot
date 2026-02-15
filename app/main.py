import gradio as gr

def generate_plan(discharge_text):
    return f"""
✅ Simplified Recovery Plan:

{discharge_text}

(This is a placeholder — agent logic coming next.)
"""

iface = gr.Interface(
    fn=generate_plan,
    inputs="textbox",
    outputs="textbox",
    title="Agentic Post-Discharge Copilot"
)

iface.launch()
