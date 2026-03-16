# GGCIL Platform API

## Carbon Audit Endpoint

POST /calculate-audit

This endpoint calculates the carbon footprint of an organization based on energy usage and waste.

### Request Example

{
 "company_name": "Example Company",
 "energy_usage_kwh": 15000,
 "waste_tonnes": 5
}

### Response Example

{
 "company": "Example Company",
 "total_co2e": 3995,
 "status": "Verified"
}

### Explanation

electricity_factor = 0.233 kgCO2e per kWh
waste_factor = 100 kgCO2e per tonne
