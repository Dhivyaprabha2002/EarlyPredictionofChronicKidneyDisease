# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 13:48:57 2023

@author: akhil
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from sklearn.neighbors import _dist_metrics
kidney_disease_model = pickle.load(open("C:/Users/akhil/Desktop/kidney diseases prediction/my_classifier (1).pkl"))
with st.sidebar:
    selected = option_menu('kidney disease prediction system',
                           ['kidney disease prediction'],
                           icon=['kidney'],
                           default_index = 0)
if (selected == 'kidney disease prediction'):
    st.title('kidney disease prediction using ML')
    age = st.text_input('age')
    blood_pressure = st.text_input('blood pressure value')
    specific_gravity = st.text_input('specific gravity') 
    albumin = st.text_input('albumin value')
    sugar = st.text_input('sugar value')
    red_blood_cells = st.text_input('red blood cell value')  
    pus_cells = st.text_input('pus_cells value')
    pus_cells_clumps = st.text_input('pus_cells_clumps value')  
    bacteria = st.text_input('bacteria')
    blood_glucose_random = st.text_input('blood_glucose_random')
    blood_urea = st.text_input('blood urea value')
    serum_creatinine = st.text_input('serum creatinine')     
    sodium = st.text_input('sodium') 
    potassium = st.text_input('potassium')
    hemoglobin = st.text_input('hemoglobin')
    packed_cell_volume = st.text_input('packed cell volume')
    white_blood__cell_count = st.text_input('white_blood__cell_count')
    red_blood_cell_count = st.text_input('red_blood_cell_count')
    hypertension = st.text_input('hypertension')    
    diabetes_mellitus = st.text_input('diabetes mellitus')     
    coronary_artery_disease = st.text_input('coronary artery value') 
    appetite = st.text_input('appetite')
    peda_edema = st.text_input('peda_edema')
    aanemia = st.text_input('aanemia')
    kidney_disease_diagnosis= ''
if st.button('kidney_diseases_test_result'):
    kidney_disease_prediction = kidney_disease_model.predict([[age, blood_pressure, specific_gravity, albumin, sugar, red_blood_cells, pus_cells, pus_cells_clumps, bacteria, blood_glucose_random, blood_urea, serum_creatinine, sodium, potassium, hemoglobin, packed_cell_volume, white_blood__cell_count, red_blood_cell_count, hypertension, diabetes_mellitus, coronary_artery_disease, appetite, peda_edema, aanemia]])
if(kidney_disease_prediction[0]==0):
    kidney_disease_diagnosis = 'the person is not suffering from kidney disease'
else:
    kidney_disease_diagnosis = 'the person have kidney dsisease'
    st.success(kidney_disease_diagnosis)
    col1, col2, col3 = st.columns(3)
with col1:
    age = st.text_input('age')
with col2:
    blood_pressure = st.text_input('blood pressure value')
with col3:
    specific_gravity = st.text_input('specific gravity')       
with col1:
    albumin = st.text_input('albumin value')
with col2:
    sugar = st.text_input('sugar value')
with col3:
    red_blood_cells = st.text_input('red blood cell value')    
with col1:
    pus_cells = st.text_input('pus_cells value')
with col2:
    pus_cells_clumps = st.text_input('pus_cells_clumps value')    
with col3:
    bacteria = st.text_input('bacteria')
with col1:
    blood_glucose_random = st.text_input('blood_glucose_random')
with col2:
    blood_urea = st.text_input('blood urea value')
with col3:
    serum_creatinine = st.text_input('serum creatinine')     
with col1:
    sodium = st.text_input('sodium') 
with col2:
    potassium = st.text_input('potassium')
with col3:
    hemoglobin = st.text_input('hemoglobin')
with col1:
    packed_cell_volume = st.text_input('packed cell volume')
with col2:
    white_blood_cell_count = st.text_input('white_blood_cell_count')
with col3:
    red_blood_cell_count = st.text_input('red_blood_cell_count')
with col1:
    hypertension = st.text_input('hypertension')  
with col2:
    diabetes_mellitus = st.text_input('diabetes mellitus')     
with col3:
    coronary_artery_disease = st.text_input('coronary artery value') 
with col1:
    appetite = st.text_input('appetite')
with col2:
    peda_edema = st.text_input('peda edema')
with col3:
    aanemia = st.text_input('aanemia') 
with open('filename', 'r', encoding='UTF-8') as f:
    text = f.read()
with open('filename', 'r', encoding='UTF-8', errors='ignore') as f:
    text = f.read()
with open('test.txt', 'r', encoding='ascii') as f:
    text = f.read()
with open("C:/Users/akhil/Desktop/kidney diseases prediction/my_classifier (1).pkl", "rb") as f:
    kidney_disease_model = pickle.load(f, encoding="UTF-8")    
import chardet
with open("C:/Users/akhil/Desktop/kidney diseases prediction/my_classifier (1).pkl", "rb") as f:
    result = chardet.detect(f.read())   
encoding = result['encoding']
with open("C:/Users/akhil/Desktop/kidney diseases prediction/my_classifier (1).pkl", "rb") as f:
    kidney_disease_model = pickle.load(f, encoding=encoding)  
    open('filename.csv', encoding="cp437", errors='ignore')
open(my_classifier.pkl, 'w', newline='', encoding="cp437", errors='ignore')
with open("my_classifier.pkl", "r+", encoding="utf-8") as file:
    pass