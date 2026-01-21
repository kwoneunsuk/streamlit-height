import streamlit as st
import numpy as np
import joblib

# -----------------------
# 페이지 설정
# -----------------------
st.header("신체 정보를 이용한 키 예측 머신러닝 모델")
st.write("신체 정보를 입력하면 키를 예측합니다.")

# -----------------------
# 모델 로드 (한 번만)
# -----------------------
model_male = joblib.load("height_model_male.pkl")
model_female = joblib.load("height_model_female.pkl")

# -----------------------
# 성별 선택
# -----------------------
gender = st.radio("성별 선택", ["남자", "여자"])

st.sidebar.header("머신러닝 모델 설계 실습 (다중회귀)")

# -----------------------
# 입력 UI + 모델 선택
# -----------------------
if gender == "남자":
    weight = st.slider("몸무게 (kg)", 30.0, 150.0, 60.0)
    hip = st.slider("엉덩이 둘레 (cm)", 60.0, 150.0, 90.0)
    shoe = st.slider("신발 치수 (mm)", 200, 320, 260)

    X = np.array([[weight, hip, shoe]])
    model = model_male

else:
    weight = st.slider("몸무게 (kg)", 30.0, 150.0, 60.0)
    neck = st.slider("목 둘레 (cm)", 20.0, 50.0, 30.0)
    hip = st.slider("엉덩이 둘레 (cm)", 60.0, 150.0, 90.0)

    X = np.array([[weight, neck, hip]])
    model = model_female

# -----------------------
# 예측
# -----------------------
if st.button("키 예측하기"):
    prediction = model.predict(X)
    st.success(f"예측 키: {prediction[0]:.1f} cm")

