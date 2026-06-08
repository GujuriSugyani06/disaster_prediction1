import streamlit as st
import pandas as pd
import pickle
import os

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="Flood Prediction System",
    page_icon="🌊",
    layout="centered"
)

st.title("🌊 Flood Prediction System")
st.write("Enter values between 1 and 10 for each factor.")

# ----------------------------
# Load Model Safely (FIXED)
# ----------------------------
BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "Notebook", "model.pkl")

if not os.path.exists(MODEL_PATH):
    st.error(f"❌ model.pkl not found at: {MODEL_PATH}")
    st.stop()

with open(MODEL_PATH, "rb") as file:
    data = pickle.load(file)

# Handle both formats
if isinstance(data, dict):
    model = data["model"]
    feature_order = data["features"]
else:
    model = data
    feature_order = [
        "MonsoonIntensity",
        "TopographyDrainage",
        "RiverManagement",
        "Deforestation",
        "Urbanization",
        "ClimateChange",
        "DamsQuality",
        "Siltation",
        "AgriculturalPractices",
        "Encroachments",
        "IneffectiveDisasterPreparedness",
        "DrainageSystems",
        "CoastalVulnerability",
        "Landslides",
        "Watersheds",
        "DeterioratingInfrastructure",
        "PopulationScore",
        "WetlandLoss",
        "InadequatePlanning",
        "PoliticalFactors"
    ]

# ----------------------------
# Input Fields (auto-generated)
# ----------------------------
inputs = {}

for feature in feature_order:
    label = feature.replace("_", " ")
    inputs[feature] = st.number_input(label, 1, 10, 5)

# ----------------------------
# Prediction
# ----------------------------
if st.button("Predict Flood Probability"):

    input_data = pd.DataFrame([[inputs[f] for f in feature_order]],
                               columns=feature_order)

    prediction = float(model.predict(input_data)[0])

    # Safety clamp
    prediction = max(0.0, min(1.0, prediction))

    st.success(f"🌊 Predicted Flood Probability: {prediction:.4f}")

    st.progress(prediction)

    # Risk levels
    if prediction < 0.30:
        st.success("🟢 Low Flood Risk")
    elif prediction < 0.70:
        st.warning("🟡 Medium Flood Risk")
    else:
        st.error("🔴 High Flood Risk")
        