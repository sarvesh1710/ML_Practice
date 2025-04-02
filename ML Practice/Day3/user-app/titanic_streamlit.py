import streamlit as st
import pandas as pd
import pickle

with open("../titanic_classification_model.pkl", "rb") as file:
    model = pickle.load(file)

st.header("Titanic Dataset Explorer")
st.write("This app allows you to explore the Titanic dataset.")

pclass = st.selectbox("Passenger Class", [1, 2, 3])
gender = st.selectbox("Gender",["Male","Female"])
fare = st.number_input("Fare", min_value=0.0, max_value=500.0, value=0.0, step=1.0)
embarked = st.selectbox("Embarked", [2, 0, 1])

encoded_gender = 0 if gender == "Female" else 1

if st.button("Predict"):
    predict_df = pd.DataFrame({
        "pclass": pclass,
        "gender": encoded_gender,
        "fare":fare,
        "embarked":embarked
    },index=["pclass","gender","fare","embarked"])

    predictions = model.predict(predict_df)
    st.write(f"Survival Probability: {predictions[0]:.2f}")


