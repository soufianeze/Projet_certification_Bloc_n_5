# -*- coding: utf-8 -*-
"""
Created on  august 05 2:40  2022

@author: win10
"""

# 1. Library imports
import uvicorn
from fastapi import FastAPI
from Notes import Notes
import numpy as np
import pickle
import pandas as pd
# 2. Create the app object
app = FastAPI()
pickle_in = open("randomforest.pkl","rb")
randomforest=pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Soufiane ZEMRANI GET AROUAND BLOC 5'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To GET AROUND': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_note(data:Notes):
    data = data.dict()
    model_key=data['model_key']
    mileage=data['mileage']
    engine_power=data['engine_power']
    fuel=data['fuel']
    paint_color=data['paint_color']
    car_type=data['car_type']
    private_parking_available=data['private_parking_available']
    has_gps=data['has_gps']
    has_air_conditioning=data['has_air_conditioning']
    automatic_car=data['automatic_car']
    has_getaround_connect=data['has_getaround_connect']
    has_speed_regulator=data['has_speed_regulator']
    winter_tires=data['has_speed_regulator']
  


   
    prediction = randomforest.predict([[model_key,mileage,engine_power,fuel,paint_color,car_type,private_parking_available,has_gps,has_air_conditioning,automatic_car,has_getaround_connect,has_speed_regulator,winter_tires]])
    output = round(prediction[0],2)
    return{'ESTIMATED RENTAL PRICE {}'.format(output)}

    
# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8001)
    
#uvicorn app:app --reload