from pydantic import BaseModel, Field
from typing import Dict

class VehicleData(BaseModel):
    make: str
    model: str
    year: str
    current_mileage: int = Field(gt=0, description="Current mileage must be a positive integer")

class MaintenanceInterval(BaseModel):
    intervals: Dict[str, int]

