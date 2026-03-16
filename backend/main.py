from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AuditData(BaseModel):
    company_name: str
    energy_usage_kwh: float
    waste_tonnes: float

@app.post("/calculate-audit")
async def calculate_carbon(data: AuditData):

    electricity_factor = 0.233
    waste_factor = 100

    electricity_emission = data.energy_usage_kwh * electricity_factor
    waste_emission = data.waste_tonnes * waste_factor

    total = electricity_emission + waste_emission

    return {
        "company": data.company_name,
        "total_co2e": round(total,2),
        "status": "Verified"
    }
