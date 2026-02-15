import gradio as gr


def generate_plan(discharge_text):

    return f"""
# ✅ Personalized Recovery Plan

---

## 🩺 Summary
Your discharge instructions have been simplified for safer recovery at home.

---

## 💊 Medications
*(Agent extraction coming next)*

---

## 🚶 Activity Guidance
Follow your physician's instructions. Avoid overexertion.

---

## ⚠️ Red Flags — Seek Immediate Care If You Notice:
- Chest pain  
- Difficulty breathing  
- High fever  
- Sudden worsening symptoms  

---

## 📅 Follow-Up
Please attend all scheduled appointments.

---

### ⚠️ Disclaimer
This AI-generated plan must be reviewed by a qualified healthcare professional.
"""


iface = gr.Interface(
    fn=generate_plan,
    inputs=gr.Textbox(lines=20, placeholder="Paste discharge summary here..."),
    outputs=gr.Markdown(),
    title="Agentic Post-Discharge Copilot",
    description="AI-powered assistant that transforms complex hospital discharge instructions into personalized recovery guidance."
)

iface.launch()
