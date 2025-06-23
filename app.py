import streamlit as st
import pandas as pd
import pickle

# ------------------------------
# Load the trained CatBoost model
# ------------------------------
@st.cache_data
def load_model():
    with open("tuned_catboost_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

model = load_model()

# ------------------------------
# Crop Encoding Map (Update if needed)
# ------------------------------
CROP_TYPE_MAP = {
    "Wheat 🌾": 0,
    "Rice 🍚": 1,
    "Maize 🌽": 2,
    "Soybean 🌱": 3,
    "Cotton 🧥": 4
}

# ------------------------------
# App Title
# ------------------------------
st.set_page_config(page_title="Crop Yield Prediction", page_icon="🌾")
st.title("🌾 Crop Yield Prediction App")

st.markdown("""
Enter the environmental conditions and select the crop type to get an estimated crop yield prediction (in units/acre).
""")

# ------------------------------
# Input Sliders and Selectors
# ------------------------------
temp = st.slider("🌡️ Temperature (°C)", min_value=10.0, max_value=50.0, value=30.0, step=0.1)
soil_quality = st.slider("🌱 Soil Quality (0–1)", min_value=0.0, max_value=1.0, value=0.75, step=0.01)
index = st.slider("📊 Temp-Humidity Index (%)", min_value=0.0, max_value=100.0, value=60.0, step=0.1)
crop_name = st.selectbox("🌾 Crop Type", list(CROP_TYPE_MAP.keys()))
humidity = st.slider("💧 Humidity (%)", min_value=0, max_value=100, value=70, step=1)
npk_ratio = st.slider("🧪 NPK Ratio", min_value=0.0, max_value=2.0, value=1.0, step=0.01)

# ------------------------------
# Prepare Input & Predict
# ------------------------------
if st.button("🚀 Predict Yield"):
    input_data = pd.DataFrame([{
        "Temperature": temp,
        "Soil_Quality": soil_quality,
        "Temp_Humidity_Index": index,
        "Crop_Type": CROP_TYPE_MAP[crop_name],
        "Humidity": humidity,
        "NPK_Ratio": npk_ratio
    }])
    prediction = model.predict(input_data)[0]
    st.success(f"🌟 **Predicted Crop Yield:** `{round(prediction, 2)} units/acre`")

# ------------------------------
# Footer
# ------------------------------
st.markdown("---")
st.caption("Developed with ❤️ using Streamlit | Model: CatBoost")
