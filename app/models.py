from pydantic import BaseModel
from typing import List

class Medication(BaseModel):
    drug: str
    dose: str
    frequency: str
    purpose: str

class DischargeResponse(BaseModel):
    triage_level: str
    medications: List[Medication]
    activity_guidance: List[str]
    warning_signs: List[str]
    red_flag_actions: List[str]
    follow_up: List[str]
    patient_instructions_simple: List[str]