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

   st.subheader('NHẬN THỨC TIỆN LỢI')
   
   STL1 = st.radio('Tôi nhận thấy việc sử dụng dịch vụ ngân hàng số làm cho các giao dịch ngân hàng trở nên dễ dàng hơn', values, horizontal=True, key= 'STL1', format_func = radio_format_func)
   STL2 = st.radio('Tôi nhận thấy sử dụng dịch vụ ngân hàng số giúp tôi kiểm soát tài chính hiệu quả', values, horizontal=True, key= 'STL2')
   STL3 = st.radio('Tôi nhận thấy sử dụng dịch vụ ngân hàng số giúp tôi tiết kiệm thời gian', values, horizontal=True, key= 'STL3')
   STL4 = st.radio('Tôi nhận thấy sử dụng dịch vụ ngân hàng số giúp tôi có quyền kiểm soát và linh hoạt hơn', values, horizontal=True, key= 'STL4')
   
   st.subheader('CHẤT LƯỢNG CHỨC NĂNG')
   CLC1 = st.radio('Tôi nhận thấy dịch vụ ngân hàng số có tính linh hoạt về thời gian và không gian', values, horizontal=True, key= 'CLC1')
   CLC2 = st.radio('Tôi nhận thấy dịch vụ ngân hàng số có quy trình xử lí giao dịch hiệu quả', values, horizontal=True, key= 'CLC2')
   CLC3 = st.radio('Tôi nhận thấy các cơ sở hạ tầng dịch vụ ngân hàng số hoạt động ổn định và đồng bộ', values, horizontal=True, key= 'CLC3')
   CLC4 = st.radio('Tôi nhận thấy dịch vụ ngân hàng số có hệ thống hỗ trợ và tư vấn chuyên nghiệp', values, horizontal=True, key= 'CLC4')
   
   st.subheader('CHẤT LƯỢNG DỊCH VỤ')
   CDV1 = st.radio('Tôi nhận thấy dịch vụ ngân hàng số đáp ứng được tất cả nhu cầu, nhiều chức năng ứng dụng đa dạng', values, horizontal=True, key='CDV1')
   CDV2 = st.radio('Tôi nhận thấy dịch vụ ngân hàng số có cơ sở vật chất và phương tiện kỹ thuật hiện đại, sạch sẽ', values, horizontal=True, key='CDV2')
   CDV3 = st.radio('Tôi nhận thấy dịch vụ ngân hàng số có khả năng thực hiện nhiều được nhiệm vụ đồng thời và độ tin cậy cao, nhanh gọn', values, horizontal=True, key='CDV3')
   CDV4 = st.radio('Tôi nhận thấy ngân hàng thực hiện cung cấp dịch vụ ngân hàng số như đã truyền thông', values, horizontal=True, key='CDV4')
   
   st.subheader('NHẬN THỨC THƯƠNG HIỆU')
   TH1 = st.radio('Tôi thường có ấn tượng tốt về thương hiệu dịch vụ ngân hàng số của ngân hàng này', values, horizontal=True, key='TH1')
   TH2 = st.radio('Theo tôi những người khác cũng có ấn tượng tốt về thương hiệu dịch vụ ngân hàng số của ngân hàng này', values, horizontal=True, key='TH2')
   TH3 = st.radio('Tôi nhận thấy hình ảnh thương hiệu dịch vụ ngân hàng số của ngân hàng này trong mắt người tiêu dùng tốt hơn các đối thủ cạnh tranh khác', values, horizontal=True, key='TH3')
   TH4 = st.radio('Chất lượng của thương hiệu dịch vụ ngân hàng số của ngân hàng này đạt chuẩn giúp tôi yên tâm sử dụng dịch vụ', values, horizontal=True, key='TH4')
   
   st.subheader('NHẬN THỨC AN TOÀN')
   RR1 = st.radio('Tôi tin tưởng dịch vụ ngân hàng số đảm bảo tính riêng tư', values, horizontal=True, key='RR1')
   RR2 = st.radio('Tôi cho rằng người khác không thể giả mạo thông tin của tôi', values, horizontal=True, key='RR2')
   RR3 = st.radio('Tôi an tâm về công nghệ sử dụng trong dịch vụ ngân hàng số', values, horizontal=True, key='RR3')
   RR4 = st.radio('Tôi nhận thấy không có gian lận thất thoát tiền khi sử dụng dịch vụ ngân hàng số', values, horizontal=True, key='RR4')
   
   st.subheader('KHẢ NĂNG SỬ DỤNG')
   KNSD1 = st.radio('Tôi nhận thấy học cách sử dụng dịch vụ ngân hàng số rất dễ dàng', values, horizontal=True, key='KNSD1')
   KNSD2 = st.radio('Tôi nhận thấy các thao tác thực hiện trên dịch vụ ngân hàng số rõ ràng, dễ hiểu', values, horizontal=True, key='KNSD2')
   KNSD3 = st.radio('Tôi nhận thấy nếu được hướng dẫn tôi có thể ngay lập tức sử dụng dịch vụ ngân hàng số một cách thuần thục', values, horizontal=True, key='KNSD3')
   KNSD4 = st.radio('Tôi nhận thấy các thao tác được thiết kế để sử dụng dịch vụ ngân hàng số rất gần gũi và quen thuộc với các ứng dụng ngày nay', values, horizontal=True, key='KNSD4')
   
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
        st.warning('Khách hàng không có trải nghiệm tốt về dịch vụ ngân hàng số')
    else:
        st.success('Khách hàng có trải nghiệm tốt về dịch vụ ngân hàng số')
