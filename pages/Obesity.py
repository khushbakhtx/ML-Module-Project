import streamlit as st
import numpy as np
import pandas as pd
import joblib
from PIL import Image
import time
image_1 = Image.open("img/1.png")

model_info = joblib.load("models/obesity_package.joblib")
model = model_info['model']
accuracy = model_info['accuracy']

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

def predict_obesity(Gender, Age, Height, Weight, family_history_with_overweight, FAVC, FCVC, NCP, SMOKE, CH2O, SCC, FAF, TUE, CAEC_Always, CAEC_Frequently, CAEC_Sometimes, CAEC_no, CALC_Always, CALC_Frequently, CALC_Sometimes, CALC_no, MTRANS_Automobile, MTRANS_Bike, MTRANS_Motorbike, MTRANS_Public_Transportation, MTRANS_Walking):
    input_data = np.array([Gender, Age, Height, Weight, family_history_with_overweight, FAVC, FCVC, NCP, SMOKE, CH2O, SCC, FAF, TUE, CAEC_Always, CAEC_Frequently, CAEC_Sometimes, CAEC_no, CALC_Always, CALC_Frequently, CALC_Sometimes, CALC_no, MTRANS_Automobile, MTRANS_Bike, MTRANS_Motorbike, MTRANS_Public_Transportation, MTRANS_Walking]).reshape(1, -1)
    input_data = np.array(input_data, dtype=float).reshape(1, -1)
    prediction = model.predict(input_data)
    return prediction

def main():
    gradual_print_large("Obesity Level Prediction")

    #st.image(image_1, use_column_width=True) 

    from streamlit.components.v1 import html
    import pandas as pd
    from ipyvizzu import Chart, Data, Config, Style

    def create_chart():
        chart = Chart(width="640px", height="360px", display="manual")
        data_frame = pd.read_csv("datasets/obesity_levels.csv")

        data = Data()
        data.add_data_frame(data_frame)
        chart.animate(data)

        chart.animate(Config({
            "x": "Count",
            "y": "ObesityLevel",
            "label": "Count",
        }))

        # Transition config: Show divided by obesity categories
        chart.animate(Config({
            "x": "Count",
            "y": "ObesityCategory",
            "color": "ObesityCategory",
            "label": ["Count", "ObesityCategory"],
        }))
        # Add style
        # Custom styling
        chart.animate(Style({
            "title": {
                "fontSize": "35px",
                "color": "#4a90e2"
            },
            "plot": {
                "backgroundColor": "#000",
                "xAxis": {
                    "label": {"color": "#000000"},
                    "title": {"color": "#4a90e2"}
                },
                "yAxis": {
                    "label": {"color": "#000000"},
                    "title": {"color": "#4a90e2"}
                },
                "marker": {
                    "colorPalette": ["#bd10e0", "#4a90e2", "#50e3c2", "#b8e986", "#f5a623", "#f8e71c", "#d0021b"]
                }
            },
        }))

        return chart._repr_html_()

    CHART = create_chart()
    html(CHART, width=650, height=370)



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
        accuracy_ = round(accuracy*100, 2)
        st.write("Model Accuracy: ", accuracy_, "%")
        #st.write("Predicted Level of Obesity: ", result)
        if result == 0:
            st.write("Вы не болеете ожирением, но у вас недостаточный вес для ваших параметров и превычек")
        elif result == 1:
            st.write("Вы не болеете ожирением.\n У вас нормальный вес, поздравляем!")
        elif result == 2:
            st.write("Вы не болеете ожирением, но у вас небольшой перевес I-го уровня")
        elif result == 3:
            st.write("Вы не болеете ожирением,но у вас перевес II-го уровня, у вас либо мышечная масса либо жир")
        elif result == 4:
            st.write("У вас Ожирение I степени")
        elif result == 5:
            st.write("У вас Ожирение II степени")
        elif result == 6:
            st.write("У вас Ожирение III степени")

if __name__=='__main__':
    main()
