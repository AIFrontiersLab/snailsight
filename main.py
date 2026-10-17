"""Minimal Galaxy Event Detector MVP."""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Galaxy Events")

class EventResult(BaseModel):
    id: int
    region: str
    intensity: int
    status: str

def detect_gals(region: str, intensity: int) -> List[dict]:
    """Simulate detection logic."""
    if region == "default":
        return [{"id": 1, "region": region, "intensity": intensity}]
    return []

@app.get("/events", response_model=List[EventResult])
def get_events(region: str = "default", intensity: int = 1):
    gals = detect_gals(region, intensity)
    if not gals:
        raise HTTPException(status_code=404, detail="No events found")
    return [{**g, "status": "detected"} for g in gals]

def demo():
    result = get_events()
    print(f"Demo result: {result}")
