import streamlit as st
import numpy as np
import pandas as pd
import pickle
import joblib

one = open("models/imon.pkl", "rb")
model = joblib.load(one)

def predict():
    pass

def main():
    html_temp = """
    <div style="background-color:#93d;padding:10px;border-radius:5px">
        <h2 style="color:white;text-align:center;">Credit Scoring Approval</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)


if __name__=='__main__':
    main()
