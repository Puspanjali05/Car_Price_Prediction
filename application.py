# flask, pandas, scikit-learn, pickle-mixin
from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)
car = pd.read_csv("Cleaned_Car_data.csv")

model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))

@app.route("/")

def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    year = sorted(car['year'].unique(), reverse=True)
    fuel_type = sorted(car['fuel_type'].unique())
    companies.insert(0, "Select Company")
    car_models.insert(0, "Select Model")
    year.insert(0, "Select Year of Purchase")
    fuel_type.insert(0, "Select Fuel Type")
    return render_template('index.html', companies=companies, car_models=car_models, years=year, fuel_types=fuel_type)

@app.route('/predict', methods=['POST'])
def predict():
    company = request.form.get('company')
    car_models = request.form.get('car_model')
    year = int(request.form.get('year'))
    fuel_type = request.form.get('fuel_type')
    kms_driven = int(request.form.get('kilo_driven'))

    prediction = model.predict(pd.DataFrame([[car_models, company, year, kms_driven, fuel_type]], columns=['name','company','year','kms_driven','fuel_type']))
    return str(np.round(prediction[0],2))

if __name__ == "__main__":
    app.run(debug=True)