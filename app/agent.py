import re


def extract_medications(text):
    meds_section = re.findall(r"Discharge Medications:(.*?)(?:\n\n|\Z)", text, re.S)

    if meds_section:
        meds = meds_section[0].strip().split("\n")
        return [m.strip("- ").strip() for m in meds if m.strip()]
    
    return ["No medications identified"]


def extract_red_flags(text):
    flags = re.findall(r"(?:Warning Signs:|Return to ER if:|Seek urgent care if:)(.*?)(?:\n\n|\Z)", text, re.S)

    if flags:
        items = flags[0].strip().split("\n")
        return [i.strip("- ").strip() for i in items if i.strip()]

    return ["No major red flags identified"]


def build_recovery_plan(text):

    medications = extract_medications(text)
    red_flags = extract_red_flags(text)

    med_markdown = "\n".join([f"- 💊 {m}" for m in medications])
    flag_markdown = "\n".join([f"- ⚠️ {f}" for f in red_flags])

    return f"""
# ✅ Personalized Recovery Plan

---

## 💊 Medications
{med_markdown}

---

## ⚠️ Seek Immediate Care If:
{flag_markdown}

---

## 🛌 General Recovery Guidance
- Get adequate rest  
- Stay hydrated  
- Follow your doctor's activity recommendations  

---

### ⚠️ Clinical Safety Notice
This AI-generated summary is for assistive purposes only and must be reviewed by a qualified healthcare professional.
"""