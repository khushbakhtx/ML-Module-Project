import streamlit as st
import numpy as np
import pandas as pd
import pickle
import joblib

model = joblib.load("models/imon_international_model.joblib")

def predict(age, old_client, credit_nominal, deadline, gender):
    pass

def main():
    html_temp = """
    <div style="background-color:#93d;padding:10px;border-radius:5px">
        <h2 style="color:white;text-align:center;">Credit Scoring Approval</h2>
    </div><br>
    """
    st.caption("Imon-International")
    st.markdown(html_temp, unsafe_allow_html=True)

    age = st.number_input("Возраст", min_value=18, max_value=90)
    old = st.radio("Вы повторный клиент", options=["Да", "Нет"], key="old_client")
    if old == "Да":
        old_client = 1
    elif old == "Нет":
        old_client = 0

    st.write("Accuracy of the model: ", 95.9, "%")
if __name__=='__main__':
    main()
