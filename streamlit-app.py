import streamlit as st
import numpy as np
import joblib

# -----------------------
# 모델 불러오기
# -----------------------
model = joblib.load("height_model.pkl")

# -----------------------
# UI
# -----------------------
st.title("키 예측 웹앱")
st.write("신체 정보를 입력하면 키를 예측합니다.")

st.sidebar.header("신체 정보 입력")

weight = st.slider("몸무게 (kg)", 30.0, 150.0, 60.0)
hip = st.slider("엉덩이 둘레 (cm)", 60.0, 150.0, 90.0)
shoe = st.slider("신발 치수 (mm)", 200, 320, 260)

# -----------------------
# 예측
# -----------------------
if st.button("키 예측하기"):
    input_data = np.array([[weight, hip, shoe]])
    prediction = model.predict(input_data)

    st.success(f"예측 키: {prediction[0]:.1f} cm")




