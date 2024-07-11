import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

values = [1, 2, 3, 4, 5]

threshold = 3

def radio_format_func(x):
    return str(x)

import base64
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
        background: url("data:image/png;base64,%s") no-repeat center bottom;
        background-size: 600px 800px; /* Adjust the size of the background image */
    }
    .stRadio > div {
        display: flex;
        align-items: center;
        margin-top: -40px;  /* Reduce margin to bring radio buttons closer */
    }
    .stRadio > div > label {
        margin-right: 10px;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('15.jpg')


with st.container():
   st.markdown("**<span style='color:green;'>Đề tài “Ứng dụng phương pháp SEM-NEURAL NETWORK để xây dựng mô hình dự báo trải nghiệm khách hàng về dịch vụ ngân hàng số tại các Ngân hàng thương mại Việt Nam” - TS. LÊ HOÀNG ANH </span>**", unsafe_allow_html=True)
    
   st.markdown("**<span style='color:red;'>PHẦN I: QUÝ KHÁCH VUI LÒNG CHO BIẾT TRẢI NGHIỆM CỦA MÌNH VỀ DỊCH VỤ NGÂN HÀNG SỐ CỦA CHÚNG TÔI</span>**", unsafe_allow_html=True)
    
   st.markdown("**<span style='color:red;'>1. NHẬN THỨC TIỆN LỢI</span>**", unsafe_allow_html=True)
   st.markdown('<span style="color:blue;">Tôi nhận thấy việc sử dụng dịch vụ ngân hàng số làm cho các giao dịch ngân hàng trở nên dễ dàng hơn</span>', unsafe_allow_html=True)
   STL1 = st.radio('', values, horizontal=True, key='STL1', format_func=radio_format_func)
   st.markdown('<span style="color:blue;">Tôi nhận thấy sử dụng dịch vụ ngân hàng số giúp tôi kiểm soát tài chính hiệu quả</span>', unsafe_allow_html=True)
   STL2 = st.radio('', values, horizontal=True, key='STL2')
   st.markdown('<span style="color:blue;">Tôi nhận thấy sử dụng dịch vụ ngân hàng số giúp tôi tiết kiệm thời gian</span>', unsafe_allow_html=True)
   STL3 = st.radio('', values, horizontal=True, key='STL3')
   st.markdown('<span style="color:blue;">Tôi nhận thấy sử dụng dịch vụ ngân hàng số giúp tôi có quyền kiểm soát và linh hoạt hơn</span>', unsafe_allow_html=True)
   STL4 = st.radio('', values, horizontal=True, key='STL4')
   
   st.markdown("**<span style='color:red;'>2. CHẤT LƯỢNG CHỨC NĂNG</span>**", unsafe_allow_html=True)
   st.markdown('<span style="color:blue;">Tôi nhận thấy dịch vụ ngân hàng số có tính linh hoạt về thời gian và không gian</span>', unsafe_allow_html=True)
   CLC1 = st.radio('', values, horizontal=True, key='CLC1')
   st.markdown('<span style="color:blue;">Tôi nhận thấy dịch vụ ngân hàng số có quy trình xử lí giao dịch hiệu quả</span>', unsafe_allow_html=True)
   CLC2 = st.radio('', values, horizontal=True, key='CLC2')
   st.markdown('<span style="color:blue;">Tôi nhận thấy các cơ sở hạ tầng dịch vụ ngân hàng số hoạt động ổn định và đồng bộ</span>', unsafe_allow_html=True)
   CLC3 = st.radio('', values, horizontal=True, key='CLC3')
   st.markdown('<span style="color:blue;">Tôi nhận thấy dịch vụ ngân hàng số có hệ thống hỗ trợ và tư vấn chuyên nghiệp</span>', unsafe_allow_html=True)
   CLC4 = st.radio('', values, horizontal=True, key='CLC4')
   
   st.markdown("**<span style='color:red;'>3. CHẤT LƯỢNG DỊCH VỤ</span>**", unsafe_allow_html=True)
   st.markdown('<span style="color:blue;">Tôi nhận thấy dịch vụ ngân hàng số đáp ứng được tất cả nhu cầu, nhiều chức năng ứng dụng đa dạng</span>', unsafe_allow_html=True)
   CDV1 = st.radio('', values, horizontal=True, key='CDV1')
   st.markdown('<span style="color:blue;">Tôi nhận thấy dịch vụ ngân hàng số có cơ sở vật chất và phương tiện kỹ thuật hiện đại, sạch sẽ</span>', unsafe_allow_html=True)
   CDV2 = st.radio('', values, horizontal=True, key='CDV2')
   st.markdown('<span style="color:blue;">Tôi nhận thấy dịch vụ ngân hàng số có khả năng thực hiện nhiều được nhiệm vụ đồng thời và độ tin cậy cao, nhanh gọn</span>', unsafe_allow_html=True)
   CDV3 = st.radio('', values, horizontal=True, key='CDV3')
   st.markdown('<span style="color:blue;">Tôi nhận thấy ngân hàng thực hiện cung cấp dịch vụ ngân hàng số như đã truyền thông</span>', unsafe_allow_html=True)
   CDV4 = st.radio('', values, horizontal=True, key='CDV4')
   
   st.markdown("**<span style='color:red;'>4. NHẬN THỨC THƯƠNG HIỆU</span>**", unsafe_allow_html=True)
   st.markdown('<span style="color:blue;">Tôi thường có ấn tượng tốt về thương hiệu dịch vụ ngân hàng số của ngân hàng này</span>', unsafe_allow_html=True)
   TH1 = st.radio('', values, horizontal=True, key='TH1')
   st.markdown('<span style="color:blue;">Theo tôi những người khác cũng có ấn tượng tốt về thương hiệu dịch vụ ngân hàng số của ngân hàng này</span>', unsafe_allow_html=True)
   TH2 = st.radio('', values, horizontal=True, key='TH2')
   st.markdown('<span style="color:blue;">Tôi nhận thấy hình ảnh thương hiệu dịch vụ ngân hàng số của ngân hàng này trong mắt người tiêu dùng tốt hơn các đối thủ cạnh tranh khác</span>', unsafe_allow_html=True)
   TH3 = st.radio('', values, horizontal=True, key='TH3')
   st.markdown('<span style="color:blue;">Chất lượng của thương hiệu dịch vụ ngân hàng số của ngân hàng này đạt chuẩn giúp tôi yên tâm sử dụng dịch vụ</span>', unsafe_allow_html=True)
   TH4 = st.radio('', values, horizontal=True, key='TH4')
   
   st.markdown("**<span style='color:red;'>5. NHẬN THỨC AN TOÀN</span>**", unsafe_allow_html=True)
   st.markdown('<span style="color:blue;">Tôi tin tưởng dịch vụ ngân hàng số đảm bảo tính riêng tư</span>', unsafe_allow_html=True)
   RR1 = st.radio('', values, horizontal=True, key='RR1')
   st.markdown('<span style="color:blue;">Tôi cho rằng người khác không thể giả mạo thông tin của tôi</span>', unsafe_allow_html=True)
   RR2 = st.radio('', values, horizontal=True, key='RR2')
   st.markdown('<span style="color:blue;">Tôi an tâm về công nghệ sử dụng trong dịch vụ ngân hàng số</span>', unsafe_allow_html=True)
   RR3 = st.radio('', values, horizontal=True, key='RR3')
   st.markdown('<span style="color:blue;">Tôi nhận thấy không có gian lận thất thoát tiền khi sử dụng dịch vụ ngân hàng số</span>', unsafe_allow_html=True)
   RR4 = st.radio('', values, horizontal=True, key='RR4')
   
   st.markdown("**<span style='color:red;'>6. KHẢ NĂNG SỬ DỤNG</span>**", unsafe_allow_html=True)
   st.markdown('<span style="color:blue;">Tôi nhận thấy học cách sử dụng dịch vụ ngân hàng số rất dễ dàng</span>', unsafe_allow_html=True)
   KNSD1 = st.radio('', values, horizontal=True, key='KNSD1')
   st.markdown('<span style="color:blue;">Tôi nhận thấy các thao tác thực hiện trên dịch vụ ngân hàng số rõ ràng, dễ hiểu</span>', unsafe_allow_html=True)
   KNSD2 = st.radio('', values, horizontal=True, key='KNSD2')
   st.markdown('<span style="color:blue;">Tôi nhận thấy nếu được hướng dẫn tôi có thể ngay lập tức sử dụng dịch vụ ngân hàng số một cách thuần thục</span>', unsafe_allow_html=True)
   KNSD3 = st.radio('', values, horizontal=True, key='KNSD3')
   st.markdown('<span style="color:blue;">Tôi nhận thấy các thao tác được thiết kế để sử dụng dịch vụ ngân hàng số rất gần gũi và quen thuộc với các ứng dụng ngày nay</span>', unsafe_allow_html=True)
   KNSD4 = st.radio('', values, horizontal=True, key='KNSD4')

with st.container():
    st.markdown("**<span style='color:red;'>PHẦN II: KẾT QUẢ DỰ BÁO TRẢI NGHIỆM CỦA KHÁCH HÀNG VỀ DỊCH VỤ NGÂN HÀNG SỐ</span>**", unsafe_allow_html=True)
    
    STL = np.array([STL1, STL2, STL3, STL4], dtype='float64').mean()
    CLC = np.array([CLC1, CLC2, CLC3, CLC4], dtype='float64').mean()
    CDV = np.array([CDV1, CDV2, CDV3, CDV4], dtype='float64').mean()
    TH = np.array([TH1, TH2, TH3, TH4], dtype='float64').mean()
    RR = np.array([RR1, RR2, RR3, RR4], dtype='float64').mean()    
    KNSD = np.array([KNSD1, KNSD2, KNSD3, KNSD4], dtype='float64').mean()
    
    X_new = np.array([[STL, CLC, CDV, TH, RR, KNSD]])
    df = pd.DataFrame(X_new, columns=['STL','CLC','CDV','TH','RR','KNSD'])
    st.write(df)
    
    # Load model
    model = pickle.load(open('model.pkl', 'rb'))
    sc_X = pickle.load(open('sc_X.pkl', 'rb'))
    sc_Y = pickle.load(open('sc_Y.pkl', 'rb'))
    
    # Transform input data
    sc_X_new = sc_X.transform(df)
    
    
    # Predict and inverse transform
    y_new = model.predict(sc_X_new)
    y_new_re = sc_Y.inverse_transform(y_new.reshape(-1,1))
    
    
    
    if y_new_re < threshold:
        st.warning('Khách hàng không có trải nghiệm tốt về dịch vụ ngân hàng số')
    else:
        st.success('Khách hàng có trải nghiệm tốt về dịch vụ ngân hàng số')
