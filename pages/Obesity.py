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


main()
gender = st.radio("Gender: ",
    key="gender",
    options=["Male", "Female"])
if gender == "Male":
    Gender = 1
elif gender == "Female":
    Gender = 0  
Age = st.text_input("Age: ", "")
Height = st.text_input("Height (in meters): ", "")
Weight = st.text_input("Weight (in kilos): ", "")
fam_hist = st.radio("Was there any ancestor with obesity: ",  key="family", options=["Yes", "No"])
if fam_hist == "Yes":
    family_history_with_overweight = 1
elif fam_hist == "No":
    family_history_with_overweight = 0

favc = st.radio("Do you often consume high-calorie foods?: ",  key="favc", options=["Yes", "No"])
if favc == "Yes":
    FAVC = 1
elif fam_hist == "No":
    FAVC = 0

FCVC = st.text_input("How many times a day do you usually eat vegetables: ", "")
NCP = st.text_input("Number of main meals per day: ", "")
smoke = st.radio("Do you smoke?", key="smoke", options=["Yes", "No"])
if smoke == "Yes":
    SMOKE = 1
elif smoke == "No":
    SMOKE = 0
CH2O = st.text_input("How many times a day do you drink water?", "")
scc = st.radio("Do you monitor the number of calories you consume?", key="scc", options=["Yes", "No"])
if scc == "Yes":
    SCC = 1
elif scc == "No":
    SCC = 0
FAF = st.text_input("How many times a week do you engage in physical activities?", "")
TUE = st.text_input("How many hours a day do you spend on electronic devices (smartphone, computer, television, video games, etc.)", "")

caec = st.radio("Do you consume food between main meals?", key="caec", options=["Always", "Often", "Sometimes", "Never"])
if caec == "Always":
    CAEC_Always = 1
    CAEC_Frequently = 0
    CAEC_Sometimes = 0
    CAEC_no = 0
elif caec == "Often":
    CAEC_Always = 0
    CAEC_Frequently = 1
    CAEC_Sometimes = 0
    CAEC_no = 0
elif caec == "Sometimes":
    CAEC_Always = 0
    CAEC_Frequently = 0
    CAEC_Sometimes = 1
    CAEC_no = 0
elif caec == "Never":
    CAEC_Always = 0
    CAEC_Frequently = 0
    CAEC_Sometimes = 0
    CAEC_no = 1

calc = st.radio("How often do you consume alcohol?", key="calc", options=["Always", "Often", "Sometimes", "Never"])
if calc == "Always":
    CALC_Always = 1
    CALC_Frequently = 0
    CALC_Sometimes = 0
    CALC_no = 0
elif calc == "Often":
    CALC_Always = 0
    CALC_Frequently = 1
    CALC_Sometimes = 0
    CALC_no = 0
elif calc == "Sometimes":
    CALC_Always = 0
    CALC_Frequently = 0
    CALC_Sometimes = 1
    CALC_no = 0
elif calc == "Never":
    CALC_Always = 0
    CALC_Frequently = 0
    CALC_Sometimes = 0
    CALC_no = 1

mtrans = st.radio("What mode of transportation do you use most often?", key="mtrans", options=["Car", "Bicycle", "Motorcycle", "Public Transportation", "Walking"])
if mtrans == "Car":
    MTRANS_Automobile = 1
    MTRANS_Bike = 0
    MTRANS_Motorbike = 0
    MTRANS_Public_Transportation = 0
    MTRANS_Walking = 0
elif mtrans == "Bicycle":
    MTRANS_Automobile = 0
    MTRANS_Bike = 1
    MTRANS_Motorbike = 0
    MTRANS_Public_Transportation = 0
    MTRANS_Walking = 0 
elif mtrans == "Motorcycle":
    MTRANS_Automobile = 0
    MTRANS_Bike = 0
    MTRANS_Motorbike = 1
    MTRANS_Public_Transportation = 0
    MTRANS_Walking = 0
elif mtrans == "Public Transportation":
    MTRANS_Automobile = 0
    MTRANS_Bike = 0
    MTRANS_Motorbike = 0
    MTRANS_Public_Transportation = 1
    MTRANS_Walking = 0          
elif mtrans == "Walking":
    MTRANS_Automobile = 0
    MTRANS_Bike = 0
    MTRANS_Motorbike = 0
    MTRANS_Public_Transportation = 0
    MTRANS_Walking = 1

if st.button("Predict"):
    result = predict_obesity(Gender, Age, Height, Weight, family_history_with_overweight, FAVC, FCVC, NCP, SMOKE, CH2O, SCC, FAF, TUE, CAEC_Always, CAEC_Frequently, CAEC_Sometimes, CAEC_no, CALC_Always, CALC_Frequently, CALC_Sometimes, CALC_no, MTRANS_Automobile, MTRANS_Bike, MTRANS_Motorbike, MTRANS_Public_Transportation, MTRANS_Walking)
    accuracy_ = round(accuracy * 100, 2)
    st.write("Model Accuracy: ", accuracy_, "%")
    
    if result == 0:
        st.write("You are not obese but have insufficient weight for your parameters and habits.")
    elif result == 1:
        st.write("You are not obese. You have a normal weight; congratulations!")
    elif result == 2:
        st.write("You are not obese but have a slight overweight of the first level.")
    elif result == 3:
        st.write("You are not obese but have second-level overweight; you may have either muscle mass or fat.")
    elif result == 4:
        st.write("You have Grade I obesity.")
    elif result == 5:
        st.write("You have Grade II obesity.")
    elif result == 6:
        st.write("You have Grade III obesity.")


if __name__=='__main__':
   main()
