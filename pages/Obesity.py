import streamlit as st
import numpy as np
import pandas as pd
import joblib
from PIL import Image

image_1 = Image.open("img/1.png")

model = joblib.load("models/obesity_model.joblib")

def predict_obesity(Gender, Age, Height, Weight, family_history_with_overweight, FAVC, FCVC, NCP, SMOKE, CH2O, SCC, FAF, TUE, CAEC_Always, CAEC_Frequently, CAEC_Sometimes, CAEC_no, CALC_Always, CALC_Frequently, CALC_Sometimes, CALC_no, MTRANS_Automobile, MTRANS_Bike, MTRANS_Motorbike, MTRANS_Public_Transportation, MTRANS_Walking):
    input_data = np.array([Gender, Age, Height, Weight, family_history_with_overweight, FAVC, FCVC, NCP, SMOKE, CH2O, SCC, FAF, TUE, CAEC_Always, CAEC_Frequently, CAEC_Sometimes, CAEC_no, CALC_Always, CALC_Frequently, CALC_Sometimes, CALC_no, MTRANS_Automobile, MTRANS_Bike, MTRANS_Motorbike, MTRANS_Public_Transportation, MTRANS_Walking]).reshape(1, -1)
    input_data = np.array(input_data, dtype=float).reshape(1, -1)
    prediction = model.predict(input_data)
    return prediction

def main():
    html_temp = """
    <div style="background-color:#93d;padding:10px;border-radius:5px">
        <h2 style="color:white;text-align:center;">Obesity Level Prediction</h2>
    </div><br>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    st.image(image_1, use_column_width=True)  

    gender = st.radio("Gender: ",
        key="gender",
        options=["Male", "Female"])
    if gender == "Male":
        Gender = 1
    elif gender == "Female":
        Gender = 0  
    Age = st.text_input("Возраст: ", "")
    Height = st.text_input("Рост (in meters): ", "")
    Weight = st.text_input("Вес (in kilos): ", "")
    fam_hist = st.radio("Был ли какой либо предок с ожирением: ",  key="family", options=["Yes", "No"])
    if fam_hist == "Yes":
        family_history_with_overweight = 1
    elif fam_hist == "No":
        family_history_with_overweight = 0

    favc = st.radio("Употребляете ли вы часто высоко-колорийные продукты: ",  key="favc", options=["Yes", "No"])
    if favc == "Yes":
        FAVC = 1
    elif fam_hist == "No":
        FAVC = 0

    FCVC = st.text_input("Сколько раз за день вы обычно употребляете овощи: ", "")
    NCP = st.text_input("Количество основных приемов пищи в день: ", "")
    smoke = st.radio("Вы курите?", key="smoke", options=["Yes", "No"])
    if smoke == "Yes":
        SMOKE = 1
    elif smoke == "No":
        SMOKE = 0
    CH2O = st.text_input("Сколько раз в день вы пьете воду?", "")
    scc = st.radio("Мониторите ли вы за кол. употребляемых колорий?", key="scc", options=["Yes", "No"])
    if scc == "Yes":
        SCC = 1
    elif scc == "No":
        SCC = 0
    FAF = st.text_input("Сколько раз в неделю вы занимаетесь физическими активностями", "")
    TUE = st.text_input("Сколько часов в день вы тратите на электронные устройства (сматрфон, комп., телевизор, видео-игры итд)","")

    caec = st.radio("Употребляете ли еду между основными приемами пищи", key="caec", options=["Всегда", "Часто", "Иногда", "Никогда"])
    if caec == "Всегда":
        CAEC_Always = 1
        CAEC_Frequently = 0
        CAEC_Sometimes = 0
        CAEC_no = 0
    elif caec == "Часто":
        CAEC_Always = 0
        CAEC_Frequently = 1
        CAEC_Sometimes = 0
        CAEC_no = 0
    elif caec == "Иногда":
        CAEC_Always = 0
        CAEC_Frequently = 0
        CAEC_Sometimes = 1
        CAEC_no = 0
    elif caec == "Никогда":
        CAEC_Always = 0
        CAEC_Frequently = 0
        CAEC_Sometimes = 0
        CAEC_no = 1

    calc = st.radio("Как часто употреляет алкоголь?", key="calc", options=["Всегда", "Часто", "Иногда", "Никогда"])
    if calc == "Всегда":
        CALC_Always = 1
        CALC_Frequently = 0
        CALC_Sometimes = 0
        CALC_no = 0
    elif calc == "Часто":
        CALC_Always = 0
        CALC_Frequently = 1
        CALC_Sometimes = 0
        CALC_no = 0
    elif calc == "Иногда":
        CALC_Always = 0
        CALC_Frequently = 0
        CALC_Sometimes = 1
        CALC_no = 0
    elif calc == "Никогда":
        CALC_Always = 0
        CALC_Frequently = 0
        CALC_Sometimes = 0
        CALC_no = 1

    mtrans = st.radio("Каким видом транспорта часто пользуетесь?", key="mtrans", options=["Автомобиль", "Велосипед", "Мотоцикл", "Общественный транспорт", "Пешком"])
    if mtrans == "Автомобиль":
        MTRANS_Automobile = 1
        MTRANS_Bike = 0
        MTRANS_Motorbike = 0
        MTRANS_Public_Transportation = 0
        MTRANS_Walking = 0
    elif mtrans == "Велосипед":
        MTRANS_Automobile = 0
        MTRANS_Bike = 1
        MTRANS_Motorbike = 0
        MTRANS_Public_Transportation = 0
        MTRANS_Walking = 0 
    elif mtrans == "Мотоцикл":
        MTRANS_Automobile = 0
        MTRANS_Bike = 0
        MTRANS_Motorbike = 1
        MTRANS_Public_Transportation = 0
        MTRANS_Walking = 0
    elif mtrans == "Общественный транспорт":
        MTRANS_Automobile = 0
        MTRANS_Bike = 0
        MTRANS_Motorbike = 0
        MTRANS_Public_Transportation = 1
        MTRANS_Walking = 0          
    elif mtrans == "Пешком":
        MTRANS_Automobile = 0
        MTRANS_Bike = 0
        MTRANS_Motorbike = 0
        MTRANS_Public_Transportation = 0
        MTRANS_Walking = 1

     
    if st.button("Predict"):
        result = predict_obesity(Gender, Age, Height, Weight, family_history_with_overweight, FAVC, FCVC, NCP, SMOKE, CH2O, SCC, FAF, TUE, CAEC_Always, CAEC_Frequently, CAEC_Sometimes, CAEC_no, CALC_Always, CALC_Frequently, CALC_Sometimes, CALC_no, MTRANS_Automobile, MTRANS_Bike, MTRANS_Motorbike, MTRANS_Public_Transportation, MTRANS_Walking)
        accuracy = 93.1
        st.write("Model Accuracy: ", accuracy, "%")
        #st.write("Predicted Level of Obesity: ", result)
        if result == 0:
            st.write("У вас недостаточный вес для ваших параметров и превычек")
        elif result == 1:
            st.write("У вас нормальный вес")
        elif result == 2:
            st.write("У вас перевес I-го уровня, вам следует сбросить вес")
        elif result == 3:
            st.write("У вас перевес II-го уровня, вам следует сбросить вес")
        elif result == 4:
            st.write("У вас Ожирение I степени")
        elif result == 5:
            st.write("У вас Ожирение II степени")
        elif result == 6:
            st.write("У вас Ожирение III степени")
 
if __name__=='__main__':
    main()
