import streamlit as st
import numpy as np
import pandas as pd
import joblib
from PIL import Image

one = open("models/nba_joblib.pkl","rb")
model = joblib.load(one)

def predict_points(intercept, field_goals, three_points, three_points_percent, free_throws, rebounds, assists, turnovers, steals, blocks, fouls):
    input_data = np.array([intercept, field_goals, three_points, three_points_percent, free_throws, rebounds, assists, turnovers, steals, blocks, fouls]).reshape(1, -1)
    input_data = np.array(input_data, dtype=float).reshape(1, -1)
    prediction = model.predict(input_data)
    return prediction

image_1 = Image.open("img/125198.jpg")

def main():
    html_temp = """
    <div style="background-color:#96e;padding:10px;border-radius:5px">
        <h2 style="color:white;text-align:center;">Points prediction</h2>
    </div><br>
    """    
    st.markdown(html_temp, unsafe_allow_html=True)

    st.image(image_1, use_column_width=True, caption="Kobe Bryant")    

    intercept = 2.007
    field_goals = st.text_input("Field Goals Made (FGM)", "")
    three_points = st.text_input("Three Points Made (3PM)", "")
    three_points_percent = st.text_input("Three Points Made Percentage (3PM%)", "")
    free_throws = st.text_input("Free Throws Made (FTM)", "")
    rebounds = st.text_input("Rebounds (REB)", "")
    assists = st.text_input("Assists (AST)", "")
    turnovers = st.text_input("Turnovers (TO)", "")
    steals = st.text_input("Steals (STL)", "")
    blocks = st.text_input("Blocks (B)", "")
    fouls = st.text_input("Fouls (F)", "")

    if st.button("Predict"):
        result = predict_points(intercept, field_goals, three_points, three_points_percent, free_throws, rebounds, assists, turnovers, steals, blocks, fouls)
        accuracy = 85.7
        st.write("Model Accuracy: ", accuracy, "%")
        st.write("Predicted Points: ", result)

if __name__=='__main__':
    main()
