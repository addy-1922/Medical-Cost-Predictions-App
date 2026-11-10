from pathlib import Path
import pickle

import numpy as np
from django.shortcuts import render

MODEL_PATH = Path(__file__).resolve().parent / "model" / "Medical.pickle"

# Alphabetical LabelEncoder mappings for the original text categories.
ENCODING = {
    "sex": {"female": 0, "male": 1},
    "smoker": {"no": 0, "yes": 1},
    "region": {
        "northeast": 0,
        "northwest": 1,
        "southeast": 2,
        "southwest": 3,
    },
}

with MODEL_PATH.open("rb") as model_file:
    model = pickle.load(model_file)


def home(request):
    return render(request, "predictor/home.html")


def predict(request):
    if request.method != "POST":
        return render(request, "predictor/home.html")

    try:
        age = int(request.POST.get("age", ""))
        sex = request.POST.get("sex", "").lower()
        bmi = float(request.POST.get("bmi", ""))
        children = int(request.POST.get("children", ""))
        smoker = request.POST.get("smoker", "").lower()
        region = request.POST.get("region", "").lower()

        if not 18 <= age <= 100:
            raise ValueError("Age must be between 18 and 100.")
        if not 10 <= bmi <= 70:
            raise ValueError("Please enter a valid BMI between 10 and 70.")
        if not 0 <= children <= 10:
            raise ValueError("Children must be between 0 and 10.")
        if sex not in ENCODING["sex"]:
            raise ValueError("Please select a valid sex.")
        if smoker not in ENCODING["smoker"]:
            raise ValueError("Please select smoker status.")
        if region not in ENCODING["region"]:
            raise ValueError("Please select a valid region.")

        input_data = np.array([[
            age,
            ENCODING["sex"][sex],
            bmi,
            children,
            ENCODING["smoker"][smoker],
            ENCODING["region"][region],
        ]], dtype=float)

        prediction = float(model.predict(input_data)[0])
        return render(
            request,
            "predictor/result.html",
            {"prediction": prediction},
        )

    except (ValueError, TypeError) as error:
        return render(
            request,
            "predictor/home.html",
            {"error": str(error) or "Please enter valid values."},
        )
