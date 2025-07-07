#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("logistic_regression_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("❤️ Heart Disease Predictor")
st.write("Enter the patient's health information below:")

# Input features
age = st.number_input("Age", 20, 100, step=1)
sex = st.selectbox("Sex", ["Male", "Female"])
bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200)
cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 600)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", ["No", "Yes"])
rest_ecg = st.selectbox("Resting ECG results", ['Normal', 'ST-T wave abnormality', 'Left ventricular hypertrophy'])
max_hr = st.number_input("Maximum Heart Rate Achieved", 60, 220)
exang = st.selectbox("Exercise-induced Angina", ["No", "Yes"])
oldpeak = st.number_input("ST depression (Oldpeak)", 0.0, 6.0, step=0.1)
slope = st.selectbox("Slope of the ST segment", ['Upsloping', 'Flat', 'Downsloping'])
thal = st.selectbox("Thallium Stress Test Result", ['Normal', 'Fixed Defect', 'Reversible Defect'])

# Encode inputs manually (adjust to match training encodings)
sex_bin = 1 if sex == "Male" else 0
fasting_bs_bin = 1 if fasting_bs == "Yes" else 0
exang_bin = 1 if exang == "Yes" else 0

# Dummy encoding for categorical features (this must match training data structure!)
ecg_normal = int(rest_ecg == "Normal")
ecg_lv = int(rest_ecg == "Left ventricular hypertrophy")
slope_flat = int(slope == "Flat")
slope_down = int(slope == "Downsloping")
thal_fixed = int(thal == "Fixed Defect")
thal_reversible = int(thal == "Reversible Defect")

# Create input array
input_data = np.array([[
    age, sex_bin, bp, cholesterol, fasting_bs_bin, max_hr, exang_bin, oldpeak,
    ecg_lv, ecg_normal, slope_down, slope_flat, thal_fixed, thal_reversible, 0, 0, 0, 0
]])

# Predict
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("⚠️ The patient is likely to have heart disease.")
    else:
        st.success("✅ The patient is unlikely to have heart disease.")

