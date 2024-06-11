import streamlit as st
from streamlit.components.v1 import html
import pandas as pd
from ipyvizzu import Chart, Data, Config, Style
import time

def menu():
    # Show a navigation menu for users
    st.sidebar.page_link("main.py", label="Home Page")
    st.sidebar.page_link("pages/NBA.py", label="NBA Score Prediction")
    st.sidebar.page_link("pages/Obesity.py", label="Obesity Level Prediction")
    st.sidebar.page_link("pages/Imon-International.py", label="Imon-International")

def gradual_print_small(text, delay=0.075):
    placeholder = st.empty()
    current_text = ""
    for char in text:
        current_text += char
        placeholder.text(current_text)
        time.sleep(delay)

def gradual_print_large(text, delay=0.1):
    placeholder = st.empty()
    current_text = ""
    for char in text:
        current_text += char
        placeholder.markdown(f"""
<div style="background-color:#93d;padding:15px;border-radius:10px">
    <h3 style="color:white;text-align:center;font-family: OCR A Std, monospace;">{current_text}</h3>
</div><br>
""", unsafe_allow_html=True)
        time.sleep(delay)

st.caption("Dev: Khushbakht Shoymardonov")
menu()
gradual_print_large("Welcome to Machine Learning Repo.")
