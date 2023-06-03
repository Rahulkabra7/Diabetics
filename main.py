from flask import Flask, jsonify, render_template, request

from project_app.utils import Diabetics

# Creating instance here
app = Flask(__name__)

# Home API
@app.route("/")
def hello_flask():
    print("Welcome to Diabetics Prediction System")
    return render_template("index.html")

@app.route("/predict_charges", methods = ["POST", "GET"])
def get_prediction():
    if request.method == "GET":
        print("We are in a GET Method")

        Glucose = float(request.args.get('Glucose'))
        BloodPressure = float(request.args.get('BloodPressure'))
        SkinThickness = float(request.args.get('SkinThickness'))
        Insulin = float(request.args.get('Insulin'))
        BMI = float(request.args.get('BMI'))
        DiabetesPedigreeFunction = float(request.args.get('DiabetesPedigreeFunction'))
        Age = int(request.args.get('Age'))

    Diabetes =  Diabetics(Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
    prediction = Diabetes.get_prediction()

    return render_template("index.html", prediction = prediction)
    # print("prediction", prediction)
    # return jsonify({"Result": f"Predicted Charges is {charges} /- Rs."}) #postman test

print("__name__ -->", __name__)

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port= 5005, debug = False)  # By default Prameters