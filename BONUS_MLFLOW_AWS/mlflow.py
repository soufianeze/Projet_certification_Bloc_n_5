import mlflow
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment(experiment_name='LOG_MODELS_PROJET_GETROUND')
import mlflow.sklearn
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import Lasso
from mlflow.models.signature import infer_signature






df = pd.read_csv("get_around_pricing_project.csv")

df = df.drop(columns=['Unnamed: 0'], axis= 1)

df = pd.get_dummies(df, columns = ['model_key','fuel','paint_color','car_type'])
df.private_parking_available = df.private_parking_available.replace({True: 1, False: 0})
df.has_gps = df.has_gps.replace({True: 1, False: 0})
df.automatic_car = df.automatic_car.replace({True: 1, False: 0})
df.has_getaround_connect = df.has_getaround_connect.replace({True: 1, False: 0})
df.has_speed_regulator = df.has_speed_regulator.replace({True: 1, False: 0})
df.winter_tires = df.winter_tires.replace({True: 1, False: 0})

mlflow.set_tracking_uri("http://localhost:5000")

X = df.drop('rental_price_per_day', axis= 1)
y = df[['rental_price_per_day']]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=37)




with mlflow.start_run(run_name= 'Random Forest Regression') as run:
    
    RandomForestRegressor = RandomForestRegressor(random_state=0, min_samples_split=15)
    RandomForestRegressor.fit(X_train, y_train)
    score = RandomForestRegressor.score(X_test, y_test) 
    predictions = RandomForestRegressor.predict(X_test)


    mlflow.sklearn.log_model(RandomForestRegressor, "random-forest-model")
    
    mlflow.log_metric("score", score)
    mlflow.log_param("min_samples_split",15)
    mlflow.log_param("alpha", 0.1)

    mlflow.end_run()






