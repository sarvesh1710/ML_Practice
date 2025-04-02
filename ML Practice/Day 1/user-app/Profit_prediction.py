import streamlit as st
import pandas as pd
import pickle

with open("./profit_prediction_model.pkl", "rb") as file:
    model = pickle.load(file)

st.header("Profit Prediction")
st.subheader("Predict profit using RnD and Marketing budget")

rnd_budget = st.number_input("RnD Budget")
marketing_budget = st.number_input("Marketing Budget")

if st.button("Predict"):
    predict_df = pd.DataFrame({
        "Rnd": rnd_budget,
        "Marketing":marketing_budget
    },index=["RnD","Marketing"])

    predictions = model.predict(predict_df)

    st.write(f"Profit Will be {predictions:.2f}")