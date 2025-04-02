import pickle  
import pandas as pd
import streamlit as st 

with open("./advertising_model.pkl", 'rb') as file:
    model = pickle.load(file)

st.header('Sales Prediction')

tv_budget = st.number_input('TV Budget', min_value=0, max_value=1000000, value=50000, step=1000)
radio_budget = st.number_input('Radio Budget', min_value=0, max_value=1000000, value=50000, step=1000)

if st.button('Predict'):
    df_predict = pd.DataFrame({
        "TV": tv_budget,
        "radio": radio_budget
    },index=["TV", "radio"])

    predictions = model.predict(df_predict)
    st.write(f"Predicted Sales: {predictions[0]:.2f}m")