import streamlit as st

def menu():
    # Show a navigation menu for users
    st.sidebar.page_link("main.py", label="Home Page")
    st.sidebar.page_link("pages/nba.py", label="NBA Score Prediction")
    st.sidebar.page_link("pages/obesity.py", label="Obesity Level Prediction")
    st.sidebar.page_link("pages/Imon-International.py", label="Imon-International")

html_temp = """
<p>ML models app</p><br><br><br>
<div style="background-color:#93d;padding:10px;border-radius:5px">
    <h2 style="color:white;text-align:center;">Welcome.</h2>
</div>
"""
st.markdown(html_temp, unsafe_allow_html=True)
menu()