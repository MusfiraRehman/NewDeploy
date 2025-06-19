import streamlit as st
import joblib
import numpy as np

# Load the model
model = joblib.load('homeprice_model.joblib')

# App title
st.title("Home Price Prediction")

# Input fields
area = st.number_input("Enter Area (in sq ft)", min_value=1500)


# Predict button
if st.button("Predict Price"):
    input_data = np.array([[area, bedrooms, age]])
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Home Price: ₹ {round(prediction, 2)}")
