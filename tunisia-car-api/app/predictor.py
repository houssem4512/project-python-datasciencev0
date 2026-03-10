import joblib
import pandas as pd
import numpy as np
import json
import os

# Load Artifacts
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PIPELINE_PATH = os.path.join(BASE_DIR, "artifacts", "car_price_pipeline.pkl")
MODEL_DEFAULTS_PATH = os.path.join(BASE_DIR, "artifacts", "model_defaults.json")
BRAND_DEFAULTS_PATH = os.path.join(BASE_DIR, "artifacts", "brand_defaults.json")

pipeline = joblib.load(PIPELINE_PATH)

with open(MODEL_DEFAULTS_PATH, 'r') as f:
    model_defaults = pd.DataFrame(json.load(f)).T

with open(BRAND_DEFAULTS_PATH, 'r') as f:
    brand_defaults = pd.DataFrame(json.load(f)).T

def get_prediction(brand, model_name, vehicle_age, km_driven, seller_type, fuel_type, transmission_type):
    
    # Try specific model defaults
    try:
        defaults = model_defaults.loc[(brand, model_name)]
        mileage = defaults["mileage"]
        engine = defaults["engine"]
        max_power = defaults["max_power"]
        seats = int(defaults["seats"])
    except KeyError:
        # Fallback to brand defaults
        try:
            defaults = brand_defaults.loc[brand]
            mileage = defaults["mileage"]
            engine = defaults["engine"]
            max_power = defaults["max_power"]
            seats = int(defaults["seats"])
        except KeyError:
            # Ultimate fallback
            mileage = 18.0
            engine = 1200.0
            max_power = 85.0
            seats = 5

    # Feature Engineering (from Kaggle)
    km_driven_adj = -np.log1p(km_driven)
    age_km_interaction = vehicle_age * km_driven_adj
    
    # Build sample
    sample = pd.DataFrame({
        "brand": [brand],
        "model_name": [model_name],
        "vehicle_age": [vehicle_age],
        "km_driven": [km_driven],
        "km_driven_adj": [km_driven_adj],
        "age_km_interaction": [age_km_interaction],
        "mileage": [mileage],
        "engine": [engine],
        "max_power": [max_power],
        "seats": [seats],
        "seller_type": [seller_type],
        "fuel_type": [fuel_type],
        "transmission_type": [transmission_type]
    })
    
    # Predict
    pred_price = pipeline.predict(sample)[0]
    pred_price_adjusted = max(pred_price, 5000)
    
    lower = round(pred_price_adjusted * 0.9)
    upper = round(pred_price_adjusted * 1.1)
    
    return int(pred_price_adjusted), lower, upper