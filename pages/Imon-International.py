import streamlit as st
import numpy as np
import pandas as pd
import pickle
import joblib

model = joblib.load("models/imon_international_model.joblib")

def predict_eligibility(gender, age, old_client, credit_amount, deadline, duration_of_long_onetime_expiration, expiration_june,
            privilege_period, goal_manzil, goal_capital, goal_main_sources, goal_buying_house, goal_consuming, goal_repair,
            goal_startup, goal_building_house, status_divorced, status_married, status_single, status_widow, deposit_belongings,
            deposit_deposit, deposit_poor, deposit_property, deposit_bail, deposit_mixed_ensuring, deposit_jewel,
            education_post_graduate, education_high, education_elementary, education_secondary_partly, education_secondary_special,
            education_secondary, business_1, business_2, business_3, business_4, business_5, business_6, business_7,
            business_8):

    input_data = np.array([gender, age, old_client, credit_amount, deadline, duration_of_long_onetime_expiration, expiration_june,
            privilege_period, goal_manzil, goal_capital, goal_main_sources, goal_buying_house, goal_consuming, goal_repair,
            goal_startup, goal_building_house, status_divorced, status_married, status_single, status_widow, deposit_belongings,
            deposit_deposit, deposit_poor, deposit_property, deposit_bail, deposit_mixed_ensuring, deposit_jewel,
            education_post_graduate, education_high, education_elementary, education_secondary_partly, education_secondary_special,
            education_secondary, business_1, business_2, business_3, business_4, business_5, business_6, business_7,
            business_8]).reshape(1, -1)
    
    input_data = np.array(input_data, dtype=float).reshape(1, -1)
    prediction = model.predict(input_data)
    return prediction

def main():
    html_temp = """
    <div style="background-color:#93d;padding:10px;border-radius:5px">
        <h2 style="color:white;text-align:center;">Credit Scoring Approval</h2>
    </div><br>
    """
    st.caption("Imon-International")
    st.markdown(html_temp, unsafe_allow_html=True)

    gend = st.radio("Gender: ",
        key="gender",
        options=["Male", "Female"])
    if gend == "Male":
        gender = 1
    elif gend == "Female":
        gender = 0  
        
    age = st.number_input("Возраст", min_value=18, max_value=90)
    old = st.radio("Вы повторный клиент", options=["Да", "Нет"], key="old_client")
    if old == "Да":
        old_client = 1
    elif old == "Нет":
        old_client = 0
    credit_amount = st.text_input("Сумма выдачи", "")
    deadline = st.text_input("Срок (в месяцах)", "")
    duration_of_long_onetime_expiration = st.text_input("Длительность самой долгой единовременной просрочки (в месяцах)", "")
    expiration_june = st.text_input("Просрочки на дату 07.06.2021 (в месяцах)", "")
    privilege_period = st.text_input("Льготный период")
    goal = st.radio("Цель кредита", options=[
        "Баланд бардоштани сам. эн. манзил", "Оборотный капитал", "Основные средства", "Покупка жилья",
        "Потребительские цели", "Ремонт жилья", "Старт-ап", "Строительство жилья"
    ])
    if goal == "Баланд бардоштани сам. эн. манзил":
        goal_manzil = 1
        goal_capital = 0
        goal_main_sources = 0
        goal_buying_house = 0
        goal_consuming = 0
        goal_repair = 0
        goal_startup = 0
        goal_building_house = 0
    elif goal == "Оборотный капитал":
        goal_manzil = 0
        goal_capital = 1
        goal_main_sources = 0
        goal_buying_house = 0
        goal_consuming = 0
        goal_repair = 0
        goal_startup = 0
        goal_building_house = 0
    elif goal == "Основные средства":
        goal_manzil = 0
        goal_capital = 0
        goal_main_sources = 1
        goal_buying_house = 0
        goal_consuming = 0
        goal_repair = 0
        goal_startup = 0
        goal_building_house = 0
    elif goal == "Покупка жилья":
        goal_manzil = 0
        goal_capital = 0
        goal_main_sources = 0
        goal_buying_house = 1
        goal_consuming = 0
        goal_repair = 0
        goal_startup = 0
        goal_building_house = 0
    elif goal == "Потребительские цели":
        goal_manzil = 0
        goal_capital = 0
        goal_main_sources = 0
        goal_buying_house = 0
        goal_consuming = 1
        goal_repair = 0
        goal_startup = 0
        goal_building_house = 0
    elif goal == "Ремонт жилья":
        goal_manzil = 0
        goal_capital = 0
        goal_main_sources = 0
        goal_buying_house = 0
        goal_consuming = 0
        goal_repair = 1
        goal_startup = 0
        goal_building_house = 0
    elif goal == "Старт-ап":
        goal_manzil = 0
        goal_capital = 0
        goal_main_sources = 0
        goal_buying_house = 0
        goal_consuming = 0
        goal_repair = 0
        goal_startup = 1
        goal_building_house = 0 
    elif goal == "Строительство жилья":
        goal_manzil = 0
        goal_capital = 0
        goal_main_sources = 0
        goal_buying_house = 0
        goal_consuming = 0
        goal_repair = 0
        goal_startup = 0
        goal_building_house = 1

    status = st.radio("Семейный статус", options=[
        "Женат/Замужем", "не женат/не замужем", "В разводе", "Вдова/вдовец"
    ])
    if status == "Женат/Замужем":
        status_divorced = 0
        status_married = 1
        status_single = 0
        status_widow = 0
    elif status == "не женат/не замужем":
        status_divorced = 0
        status_married = 0
        status_single = 1
        status_widow = 0 
    elif status ==  "В разводе":
        status_divorced = 1
        status_married = 0
        status_single = 0
        status_widow = 0
    elif status == "Вдова/вдовец":
        status_divorced = 0
        status_married = 0
        status_single = 0
        status_widow = 1     

    deposit = st.radio("Вид залога", options=[
        "Движимое имущество", "Депозит", "Не обеспеченный", "Недвижимость", "Поручительство", "Смешанное обеспечение",
        "Ювелирные изделия"
    ])
    if deposit == "Движимое имущество":
        deposit_belongings = 1
        deposit_deposit = 0
        deposit_poor = 0
        deposit_property = 0
        deposit_bail = 0
        deposit_mixed_ensuring = 0
        deposit_jewel = 0
    elif deposit == "Депозит":
        deposit_belongings = 0
        deposit_deposit = 1
        deposit_poor = 0
        deposit_property = 0
        deposit_bail = 0
        deposit_mixed_ensuring = 0
        deposit_jewel = 0 
    elif deposit == "Не обеспеченный":
        deposit_belongings = 0
        deposit_deposit = 0
        deposit_poor = 1
        deposit_property = 0
        deposit_bail = 0
        deposit_mixed_ensuring = 0
        deposit_jewel = 0  
    elif deposit == "Недвижимость":
        deposit_belongings = 0
        deposit_deposit = 0
        deposit_poor = 0
        deposit_property = 1
        deposit_bail = 0
        deposit_mixed_ensuring = 0
        deposit_jewel = 0  
    elif deposit == "Поручительство":
        deposit_belongings = 0
        deposit_deposit = 0
        deposit_poor = 0
        deposit_property = 0
        deposit_bail = 1
        deposit_mixed_ensuring = 0
        deposit_jewel = 0
    elif deposit == "Смешанное обеспечение":
        deposit_belongings = 0
        deposit_deposit = 0
        deposit_poor = 0
        deposit_property = 0
        deposit_bail = 0
        deposit_mixed_ensuring = 1
        deposit_jewel = 0   
    elif deposit == "Ювелирные изделия":
        deposit_belongings = 0
        deposit_deposit = 0
        deposit_poor = 0
        deposit_property = 0
        deposit_bail = 0
        deposit_mixed_ensuring = 0
        deposit_jewel = 1
    
    education = st.radio("Образование", options=['Аспирантура',
       'Высшее образование', 'Начальное образование',
       'Неполное среднее образование', 'Среднее специальное образование',
       'Среднее образование'])
    if education == 'Аспирантура':
        education_post_graduate = 1
        education_high = 0
        education_elementary = 0
        education_secondary_partly = 0
        education_secondary_special = 0
        education_secondary = 0
    elif education == 'Высшее образование':
        education_post_graduate = 0
        education_high = 1
        education_elementary = 0
        education_secondary_partly = 0
        education_secondary_special = 0
        education_secondary = 0
    elif education == 'Начальное образование':
        education_post_graduate = 0
        education_high = 0
        education_elementary = 1
        education_secondary_partly = 0
        education_secondary_special = 0
        education_secondary = 0  
    elif education == 'Неполное среднее образование':
        education_post_graduate = 0
        education_high = 0
        education_elementary = 0
        education_secondary_partly = 1
        education_secondary_special = 0
        education_secondary = 0
    elif education == 'Среднее специальное образование':
        education_post_graduate = 0
        education_high = 0
        education_elementary = 0
        education_secondary_partly = 0
        education_secondary_special = 1
        education_secondary = 0
    elif education == 'Среднее образование':
        education_post_graduate = 0
        education_high = 0
        education_elementary = 0
        education_secondary_partly = 0
        education_secondary_special = 0
        education_secondary = 1

    business = st.radio("Вид бизнеса: ", options=[
        'Карзи истеъмоли/Потребительский кредит',
       'Истехсолот/Производство',
       'Хизматрасони/Услуги', 'Савдо / Торговля',
       'Чорводори / Животноводство',
       'Хочагии кишлок / Сельское хозяйство',
       'Тичорати бурунмарзи / Внешняя торговля',
       'Ипотека'
    ], key="business")
    if business == 'Карзи истеъмоли/Потребительский кредит':
        business_1 = 1
        business_2 = 0
        business_3 = 0
        business_4 = 0
        business_5 = 0
        business_6 = 0
        business_7 = 0
        business_8 = 0
    elif business == 'Истехсолот/Производство':
        business_1 = 0
        business_2 = 1
        business_3 = 0
        business_4 = 0
        business_5 = 0
        business_6 = 0
        business_7 = 0
        business_8 = 0
    elif business == ' Хизматрасони/Услуги':
        business_1 = 0
        business_2 = 0
        business_3 = 1
        business_4 = 0
        business_5 = 0
        business_6 = 0
        business_7 = 0
        business_8 = 0
    elif business == 'Савдо / Торговля':
        business_1 = 0
        business_2 = 0
        business_3 = 0
        business_4 = 1
        business_5 = 0
        business_6 = 0
        business_7 = 0
        business_8 = 0   
    elif business == 'Чорводори / Животноводство':
        business_1 = 0
        business_2 = 0
        business_3 = 0
        business_4 = 0
        business_5 = 1
        business_6 = 0
        business_7 = 0
        business_8 = 0
    elif business == 'Хочагии кишлок / Сельское хозяйство':
        business_1 = 0
        business_2 = 0
        business_3 = 0
        business_4 = 0
        business_5 = 0
        business_6 = 1
        business_7 = 0
        business_8 = 0 
    elif business == 'Тичорати бурунмарзи / Внешняя торговля':
        business_1 = 0
        business_2 = 0
        business_3 = 0
        business_4 = 0
        business_5 = 0
        business_6 = 0
        business_7 = 1
        business_8 = 0 
    elif business == 'Ипотека':
        business_1 = 0
        business_2 = 0
        business_3 = 0
        business_4 = 0
        business_5 = 0
        business_6 = 0
        business_7 = 0
        business_8 = 1 
                
    if st.button("Predict"):
        result = predict_eligibility(gender, age, old_client, credit_amount, deadline, duration_of_long_onetime_expiration, expiration_june,
            privilege_period, goal_manzil, goal_capital, goal_main_sources, goal_buying_house, goal_consuming, goal_repair,
            goal_startup, goal_building_house, status_divorced, status_married, status_single, status_widow, deposit_belongings,
            deposit_deposit, deposit_poor, deposit_property, deposit_bail, deposit_mixed_ensuring, deposit_jewel,
            education_post_graduate, education_high, education_elementary, education_secondary_partly, education_secondary_special,
            education_secondary, business_1, business_2, business_3, business_4, business_5, business_6, business_7,
            business_8)
        
        if result == 0:
            st.write("Sorry to inform, but you are not eligible for the loan")
        elif result == 1:
            st.success("Congratulations, you are eligible for the loan")
        st.write("Accuracy of the model: ", 95.9, "%")
if __name__=='__main__':
    main()
