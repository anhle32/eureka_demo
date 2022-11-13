# -*- coding: utf-8 -*-

import streamlit as st
import pickle
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler

values = [1, 2, 3, 4, 5]

threshold = 3

def radio_format_func(x):
    return str(x)

with st.container():
   st.write("Chọn các giá trị")

   st.subheader('Nhóm câu hỏi STL')
   
   STL1 = st.radio('Câu hỏi 1', values, horizontal=True, key= 'STL1', format_func = radio_format_func)
   STL2 = st.radio('Câu hỏi 2', values, horizontal=True, key= 'STL2')
   STL3 = st.radio('Câu hỏi 3', values, horizontal=True, key= 'STL3')
   STL4 = st.radio('Câu hỏi 4', values, horizontal=True, key= 'STL4')
   
   st.subheader('Nhóm câu hỏi CLC')
   CLC1 = st.radio('Câu hỏi 5', values, horizontal=True, key= 'CLC1')
   CLC2 = st.radio('Câu hỏi 6', values, horizontal=True, key= 'CLC2')
   CLC3 = st.radio('Câu hỏi 7', values, horizontal=True, key= 'CLC3')
   CLC4 = st.radio('Câu hỏi 8', values, horizontal=True, key= 'CLC4')
   
   st.subheader('Nhóm câu hỏi CDV')
   CDV1 = st.radio('Câu hỏi 5', values, horizontal=True, key='CDV1')
   CDV2 = st.radio('Câu hỏi 6', values, horizontal=True, key='CDV2')
   CDV3 = st.radio('Câu hỏi 7', values, horizontal=True, key='CDV3')
   CDV4 = st.radio('Câu hỏi 8', values, horizontal=True, key='CDV4')
   
   st.subheader('Nhóm câu hỏi TH')
   TH1 = st.radio('Câu hỏi 5', values, horizontal=True, key='TH1')
   TH2 = st.radio('Câu hỏi 6', values, horizontal=True, key='TH2')
   TH3 = st.radio('Câu hỏi 7', values, horizontal=True, key='TH3')
   TH4 = st.radio('Câu hỏi 8', values, horizontal=True, key='TH4')
   
   st.subheader('Nhóm câu hỏi RR')
   RR1 = st.radio('Câu hỏi 5', values, horizontal=True, key='RR1')
   RR2 = st.radio('Câu hỏi 6', values, horizontal=True, key='RR2')
   RR3 = st.radio('Câu hỏi 7', values, horizontal=True, key='RR3')
   RR4 = st.radio('Câu hỏi 8', values, horizontal=True, key='RR4')
   
   st.subheader('Nhóm câu hỏi KNSD')
   KNSD1 = st.radio('Câu hỏi 5', values, horizontal=True, key='KNSD1')
   KNSD2 = st.radio('Câu hỏi 6', values, horizontal=True, key='KNSD2')
   KNSD3 = st.radio('Câu hỏi 7', values, horizontal=True, key='KNSD3')
   KNSD4 = st.radio('Câu hỏi 8', values, horizontal=True, key='KNSD4')
   
with st.container():
    st.subheader('Dự báo kết quả với ANN')
    
    STL = np.array([STL1, STL2, STL3, STL4], dtype='float64').mean()
    CLC = np.array([CLC1, CLC2, CLC3, CLC4], dtype='float64').mean()
    CDV = np.array([CDV1, CDV2, CDV3, CDV4], dtype='float64').mean()
    TH = np.array([TH1, TH2, TH3, TH4], dtype='float64').mean()
    RR = np.array([RR1, RR2, RR3, RR4], dtype='float64').mean()    
    KNSD = np.array([KNSD1, KNSD2, KNSD3, KNSD4], dtype='float64').mean()
    
    X_new = np.array([[STL, CLC, CDV, TH, RR, KNSD]])
    df = pd.DataFrame(X_new, columns=['STL','CLC','CDV','TH','RR','KNSD'])
    st.write(df)
    
    #Load model
    model = pickle.load(open('model.pkl', 'rb'))
    sc_X = pickle.load(open('sc_X.pkl', 'rb'))
    sc_Y = pickle.load(open('sc_Y.pkl', 'rb'))
    
    #st.write('sc_X', sc_X.scale_, sc_X.mean_)
    sc_X_new = sc_X.transform(df)
    st.write('sc_X_new: ', sc_X_new)
    
    
    y_new = model.predict(sc_X_new)
    
    y_new_re = sc_Y.inverse_transform(y_new.reshape(-1,1))
    
    st.write('y_new: ', y_new)
    st.write('y_new_re: ', y_new_re)
    if y_new_re < threshold:
        st.warning('Không')
    else:
        st.success('Có')