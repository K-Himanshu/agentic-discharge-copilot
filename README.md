# 🏥 Agentic Post-Discharge Copilot

**AI-Powered Clinical Discharge Safety Assistant built with MedGemma**

---

## 🚨 The Problem

Hospital discharge is one of the highest-risk transition points in healthcare.

Patients often:

* Receive complex medication instructions
* Misunderstand warning signs
* Lack clear follow-up plans
* Experience avoidable readmissions

Clinical teams are overloaded, and discharge summaries are frequently dense, inconsistent, and difficult for patients to interpret.

There is a critical gap between hospital discharge and safe recovery at home.

---

## 💡 Our Solution

**Agentic Post-Discharge Copilot** is a MedGemma-powered AI system that:

* Converts discharge summaries into structured recovery plans
* Assigns readmission risk triage levels
* Extracts red-flag warning signs
* Generates patient-friendly instructions
* Applies rule-based safety validation
* Logs outputs for audit traceability

This system is designed to support clinicians, reduce readmission risk, and improve post-discharge clarity.

---

## 🧠 Agentic Workflow Design

Rather than a single model call, we implement a modular clinical workflow:

```
Discharge Note
      ↓
Risk Triage Agent
      ↓
Structured Care Plan Generator
      ↓
Safety Validator (Rule-based)
      ↓
Audit Logging + API Response
```

This layered architecture improves reliability and aligns with real-world healthcare workflows.

---

## 📦 Project Structure

```
agentic-discharge-copilot/
│
├── app/
│   ├── main.py              # FastAPI entrypoint
│   ├── models.py            # Pydantic schemas
│   ├── medgemma.py          # MedGemma loading + inference
│   ├── agents.py            # Triage + plan orchestration
│   ├── safety.py            # Rule-based safety validator
│   └── logging_utils.py     # Audit logging
│
├── requirements.txt
├── README.md
└── .env
```

---

## 🔬 Use of MedGemma (HAI-DEF Model)

This project uses:

**Model:** `google/medgemma-1.5-4b-it`

We leverage MedGemma’s instruction-tuned medical reasoning capabilities to:

* Generate structured clinical outputs
* Extract medication regimens
* Identify warning signs
* Assign triage risk levels
* Produce patient-friendly language

Inference is:

* Deterministic (no sampling)
* Structured JSON-constrained
* GPU-accelerated
* Precision optimized (bfloat16/float16)

---

## 🧾 Output Schema

The system enforces strict JSON output:

```json
{
  "triage_level": "low | medium | high",
  "medications": [
    {
      "drug": "",
      "dose": "",
      "frequency": "",
      "purpose": ""
    }
  ],
  "activity_guidance": [],
  "warning_signs": [],
  "red_flag_actions": [],
  "follow_up": [],
  "patient_instructions_simple": []
}
```

This structured design enables:

* EHR integration potential
* Clinical validation
* Safety rule application
* Reduced ambiguity

---

## ⚠️ Safety & Validation Layer

We implement hybrid AI + rule-based safeguards:

* Detection of high-risk symptoms (e.g., chest pain, shortness of breath)
* Escalation signals
* Audit logging for traceability
* Deterministic inference (no randomness in medical outputs)

Healthcare AI must prioritize safety over creativity.

---

## 🖥 Clinical UI

The Gradio interface provides:

* Discharge note input
* Visual triage indicator
* Medication display
* Warning signs section
* Follow-up plan
* Simplified patient instructions

Designed for clarity, readability, and workflow integration.

---

## 🚀 How to Run

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Start backend

```bash
uvicorn app.main:app --reload
```

### 3️⃣ Launch UI

```bash
python app/ui.py
```

---

## 📊 Impact Potential

If deployed in real-world settings, this system could:

* Improve discharge comprehension
* Reduce preventable readmissions
* Assist overburdened clinical staff
* Standardize recovery instructions
* Enhance patient safety monitoring

Structured AI discharge tools have the potential to significantly improve care transitions.



## 🔒 Audit & Traceability

All model outputs are logged for audit review.

This enables:

* Traceability
* Retrospective validation
* Continuous quality monitoring

---

## 🌍 Future Directions

* Edge deployment (quantized MedGemma)
* EHR integration APIs
* Multilingual patient instructions
* Post-discharge SMS follow-up integration
* Clinical validation studies

---

## 👥 Team

Built for the MedGemma Impact Challenge.

---

# 🎯 Final Note

Agentic Post-Discharge Copilot is not just a summarizer —
it is a structured, safety-focused clinical workflow assistant designed to bridge the critical gap between hospital discharge and safe recovery at home.




