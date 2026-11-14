# Medical Insurance Charges Prediction — Django

🚀 **Live Demo:** [Click Here to View the Application](https://medical-cost-predictions-app.onrender.com)

A Django web app that loads your trained RandomForestRegressor and predicts medical insurance charges.

## Model details checked from your uploaded `Medical.pickle`
- Model: `RandomForestRegressor`
- Trees: 250
- Expected input columns and order: `age, sex, bmi, children, smoker, region`
- The model expects 6 numeric inputs.

## Categorical encoding
This project uses the alphabetical `LabelEncoder` mapping:
- `sex`: female = 0, male = 1
- `smoker`: no = 0, yes = 1
- `region`: northeast = 0, northwest = 1, southeast = 2, southwest = 3

These are the usual LabelEncoder mappings for these category names. If your notebook used a different mapping, update `ENCODING` in `predictor/views.py` to match it.

## Setup (Windows)
Open a terminal in this project folder:

```bash
py -3.12 -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/

**Important:** The pickle was created with scikit-learn 1.7.2. The requirements pin that version because loading scikit-learn pickle files across versions can cause warnings or errors. Python 3.12 is recommended for a smooth install.

## Run a prediction
Enter age, sex, BMI, number of children, smoker status and region, then click Predict.

## Project structure
- `MedicalInsurance/` — Django project configuration
- `predictor/` — prediction app
- `predictor/model/Medical.pickle` — your trained model
- `predictor/templates/predictor/` — HTML pages
- `predictor/static/predictor/` — CSS and JavaScript
