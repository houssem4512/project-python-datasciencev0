from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .predictor import get_prediction
from fastapi.middleware.cors import CORSMiddleware  # 👈 NEW IMPORT

app = FastAPI(title="Tunisia Car Price Predictor")

# 👇 ADD THIS BLOCK
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CarInput(BaseModel):
    brand: str
    model_name: str
    vehicle_age: int
    km_driven: int
    seller_type: str = "Dealer"
    fuel_type: str = "Petrol"
    transmission_type: str = "Manual"

@app.get("/")
def home():
    return {"message": "Tunisia Car Price API is running"}

@app.post("/predict")
def predict_price(car: CarInput):
    try:
        price, low, high = get_prediction(
            brand=car.brand,
            model_name=car.model_name,
            vehicle_age=car.vehicle_age,
            km_driven=car.km_driven,
            seller_type=car.seller_type,
            fuel_type=car.fuel_type,
            transmission_type=car.transmission_type
        )
        return {
            "predicted_price_tnd": price,
            "price_range": {"min": low, "max": high}
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))