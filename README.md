# Car Price Predictor

Project link: https://github.com/Puspanjali05/Car_Price_Prediction

<img src="https://github.com/Puspanjali05/Car_Price_Prediction/blob/main/Car%20Price%20Predictor.png" alt="Car Price Predictor UI" width="600">

---

## Aim

This project aims to predict the **price of a used car** by taking its **company name, model, year of purchase**, and other parameters such as fuel type, kilometers driven, and transmission.

<img src="https://github.com/Puspanjali05/Car_Price_Prediction/blob/main/Demo%20Prediction.png" alt="Prediction Example" width="600">

---

## How to Use

1. Clone the repository
2. Install the required packages in "requirements.txt".

Some packages are:
 - numpy 
 - pandas 
 - scikit-learn
 - flask (if using web app)

3. Run the "application.py" file or open the notebook "Car_Price_Prediction.ipynb"
And you are good to go. 

# Description

## What this project does?

1. This project takes the parameters of a used car like: Company name, Model name, Year of Purchase, Fuel Type, Kilometers Driven, Transmission type.
2. It then predicts the possible price of the car. For example, the image below shows the predicted price of a Hyundai Grand i10. 

<img src="https://github.com/Puspanjali05/Car_Price_Prediction/blob/main/Demo%20Prediction.png" alt="Prediction Example" width="600">

## How this project does?

1. The dataset was collected and cleaned (handle missing values, format columns, etc.).
   > Example dataset: `quikr_car.csv`
2. Data preprocessing included encoding categorical variables, scaling numerical features, and feature selection.
3. A Linear Regression model was trained on the dataset.
   - Achieved R² score: 0.90 
4. The trained model is integrated into a Flask web application ("application.py") where users can input car details and get predicted prices in real-time.

# Author

**Puspanjali Behera**  
- GitHub: [@Puspanjali05](https://github.com/Puspanjali05)  
- Email: beherapuspanjali421@gmail.com
