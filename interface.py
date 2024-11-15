from flask import Flask,request,jsonify
import config
from Project.utils import MedicalInsurance
import numpy as np

app = Flask(__name__)
@app.route("/")
def get_home():
    return "Hello Good Evening"

@app.route("/predict_charges",methods = ["POST","GET"])
def get_insurance():
    if request.method == "POST":
        data = request.form
        print("Use input data is >>>>",data)
        age = eval(data["age"])
        gender = data["gender"]
        bmi = data["bmi"]
        children = int(data["children"])
        smoker = data["smoker"]
        region = data["region"]
        med_obj = MedicalInsurance(age,gender,bmi,children,smoker,region)
        charges = med_obj.get_predict_charges()
        return jsonify({"Result":f"Predicted medical insurance charges {charges[0]}"})

if __name__ == '__main__':
    app.run(debug=True)