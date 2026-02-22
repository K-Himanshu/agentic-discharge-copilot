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

The system is designed to support clinicians, reduce readmission risk, and improve post-discharge clarity.

---

# 🏗 System Architecture

This project uses a **hybrid cloud + local architecture** to ensure stable GPU inference while keeping the repository lightweight and reproducible.

## ☁️ Cloud (Google Colab GPU)

* MedGemma (`google/medgemma-1.5-4b-it`)
* FastAPI inference service
* Deterministic JSON-constrained generation
* Exposed securely via ngrok

## 💻 Local Repository

* Gradio clinical UI
* API client layer
* Rule-based safety validator
* Audit logging
* Configuration management

The model **does not run locally**.
All inference is performed remotely on GPU for stability and reproducibility.

---

## 🧠 Agentic Workflow Design

Rather than a single model call, we implement a modular clinical workflow:

```
Discharge Note
      ↓
Remote MedGemma Inference (GPU)
      ↓
Structured Care Plan (JSON)
      ↓
Local Safety Validator (Rule-based)
      ↓
Audit Logging + UI Display
```

This separation of concerns improves reliability and mirrors real-world healthcare system design.

---

## 📦 Project Structure

```
agentic-discharge-copilot/
│
├── app/
│   ├── ui.py                # Gradio clinical interface
│   ├── api_client.py        # Calls remote Colab inference service
│   ├── safety.py            # Rule-based safety validator
│   ├── models.py            # Pydantic schemas
│   ├── config.py            # Environment configuration
│   └── logging_utils.py     # Audit logging
│
├── medgemma_inference_server.ipynb
├── requirements.txt
├── README.md
└── .env
```

---

## 🔬 Use of MedGemma (HAI-DEF Model)

**Model Used:** `google/medgemma-1.5-4b-it`

We leverage MedGemma’s instruction-tuned medical reasoning to:

* Generate structured clinical outputs
* Extract medication regimens
* Identify warning signs
* Assign triage risk levels
* Produce patient-friendly language

Inference characteristics:

* Deterministic (no sampling)
* Strict JSON schema enforcement
* GPU-accelerated (Colab)
* Precision optimized (bfloat16)

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
* Escalation flags
* Structured red-flag actions
* Audit logging for traceability
* Deterministic inference (no randomness)

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
* Safety alerts

Designed for clarity, readability, and workflow integration.

---
## 🧪 Running MedGemma Inference (Colab)

The model runs remotely on GPU via Google Colab.

1. Open `medgemma_inference_server.ipynb`
2. Run all cells
3. Copy the generated ngrok URL
4. Update `.env` with the endpoint
5. Launch the local UI

Inference is not performed locally.

# 🚀 How to Run (Local UI)

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Configure remote endpoint

Create `.env`:

```
API_URL=https://your-ngrok-url.ngrok-free.app/generate
```

### 3️⃣ Launch UI

```bash
python app/ui.py
```

⚠️ Ensure the Colab inference server is running before launching the UI.

---

## 📊 Impact Potential

If deployed in real-world settings, this system could:

* Improve discharge comprehension
* Reduce preventable readmissions
* Assist overburdened clinical staff
* Standardize recovery instructions
* Enhance patient safety monitoring

Structured AI discharge tools have the potential to significantly improve care transitions.

---

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

