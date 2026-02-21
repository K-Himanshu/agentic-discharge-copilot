def validate_output(output_json: dict):
    alerts = []

    warning_signs = output_json.get("warning_signs", [])

    high_risk_terms = ["chest pain", "shortness of breath", "confusion"]

    for term in high_risk_terms:
        if any(term in w.lower() for w in warning_signs):
            alerts.append(f"High risk symptom detected: {term}")

    return alerts