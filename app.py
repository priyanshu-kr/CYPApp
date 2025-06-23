import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("tuned_catboost_model.pkl")

# Encoding map
CROP_TYPE_MAP = {
    "Wheat": 0,
    "Rice": 1,
    "Maize": 2,
    "Soybean": 3,
    "Cotton": 4
}

st.title("🌾 Crop Yield Prediction App")

st.sidebar.header("Enter Inputs")

temp = st.sidebar.slider("🌡️ Temperature (°C)", 10.0, 50.0, 30.0)
soil_quality = st.sidebar.slider("🌱 Soil Quality (0-1)", 0.0, 1.0, 0.75)
index = st.sidebar.slider("📊 Temp-Humidity Index", 0.0, 100.0, 60.0)
crop_name = st.sidebar.selectbox("🌿 Crop Type", list(CROP_TYPE_MAP.keys()))
humidity = st.sidebar.slider("💧 Humidity (%)", 0.0, 100.0, 70.0)
npk_ratio = st.sidebar.slider("🧪 NPK Ratio", 0.0, 2.0, 1.0)

if st.sidebar.button("Predict Yield"):
    df = pd.DataFrame([{
        "Temperature": temp,
        "Soil_Quality": soil_quality,
        "Temp_Humidity_Index": index,
        "Crop_Type": CROP_TYPE_MAP[crop_name],
        "Humidity": humidity,
        "NPK_Ratio": npk_ratio
    }])

    prediction = model.predict(df)[0]
    st.success(f"🌟 Predicted Crop Yield: **{round(prediction, 2)} units/acre**")
i
