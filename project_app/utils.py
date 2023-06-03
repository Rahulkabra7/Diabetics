import pandas as pd
import numpy as np
import pickle
import warnings
warnings.filterwarnings('ignore')
import os
import config

class Diabetics():
    def __init__(self,Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
        self.Glucose = Glucose
        self.BloodPressure = BloodPressure
        self.SkinThickness = SkinThickness
        self.Insulin = Insulin
        self.BMI = BMI
        self.DiabetesPedigreeFunction = DiabetesPedigreeFunction
        self.Age = Age

    def load_models(self):
        with open ('project_app/Logistic model.pkl','rb') as f:
            self.logistic_model = pickle.load(f)

    def get_prediction(self):
        self.load_models()

        test_array = np.array([[self.Glucose, self.BloodPressure, self.SkinThickness, self.Insulin, self.BMI, self.DiabetesPedigreeFunction, self.Age]])
        # test_array

        result = self.logistic_model.predict(test_array)
        if result==1:
            prediction = "Yes,You are Having Diabetics"
        else:
            prediction = "No,You are not Having Diabetics"

        return prediction

if __name__ == "__main__":
    Glucose = 141.000000
    BloodPressure = 72.375171
    SkinThickness = 29.153420
    Insulin = 155.548223
    BMI = 42.400000
    DiabetesPedigreeFunction = 0.205000
    Age = 29.000000

    Diabetes =  Diabetics(Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
    prediction = Heart.get_prediction()
    print("prediction", prediction)