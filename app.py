import streamlit as st
import pandas as pd
import pickle
import os

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(page_title="Flood Prediction System", page_icon="🌊", layout="centered")

st.title("🌊 Flood Prediction System")
st.write("Enter values between 1 and 10 for each factor.")

# ----------------------------
# Load Model Safely
# ----------------------------
MODEL_PATH = "model.pkl"

if not os.path.exists(MODEL_PATH):
    st.error("❌ model.pkl not found. Please add the trained model file.")
    st.stop()

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

# ----------------------------
# Feature Inputs
# ----------------------------
MonsoonIntensity = st.number_input("Monsoon Intensity", 1, 10, 5)
TopographyDrainage = st.number_input("Topography Drainage", 1, 10, 5)
RiverManagement = st.number_input("River Management", 1, 10, 5)
Deforestation = st.number_input("Deforestation", 1, 10, 5)
Urbanization = st.number_input("Urbanization", 1, 10, 5)
ClimateChange = st.number_input("Climate Change", 1, 10, 5)
DamsQuality = st.number_input("Dams Quality", 1, 10, 5)
Siltation = st.number_input("Siltation", 1, 10, 5)
AgriculturalPractices = st.number_input("Agricultural Practices", 1, 10, 5)
Encroachments = st.number_input("Encroachments", 1, 10, 5)
IneffectiveDisasterPreparedness = st.number_input("Disaster Preparedness", 1, 10, 5)
DrainageSystems = st.number_input("Drainage Systems", 1, 10, 5)
CoastalVulnerability = st.number_input("Coastal Vulnerability", 1, 10, 5)
Landslides = st.number_input("Landslides", 1, 10, 5)
Watersheds = st.number_input("Watersheds", 1, 10, 5)
DeterioratingInfrastructure = st.number_input("Infrastructure Condition", 1, 10, 5)
PopulationScore = st.number_input("Population Score", 1, 10, 5)
WetlandLoss = st.number_input("Wetland Loss", 1, 10, 5)
InadequatePlanning = st.number_input("Inadequate Planning", 1, 10, 5)
PoliticalFactors = st.number_input("Political Factors", 1, 10, 5)

# ----------------------------
# Prediction Button
# ----------------------------
if st.button("Predict Flood Probability"):

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

    input_data = pd.DataFrame([[
        MonsoonIntensity,
        TopographyDrainage,
        RiverManagement,
        Deforestation,
        Urbanization,
        ClimateChange,
        DamsQuality,
        Siltation,
        AgriculturalPractices,
        Encroachments,
        IneffectiveDisasterPreparedness,
        DrainageSystems,
        CoastalVulnerability,
        Landslides,
        Watersheds,
        DeterioratingInfrastructure,
        PopulationScore,
        WetlandLoss,
        InadequatePlanning,
        PoliticalFactors
    ]], columns=feature_order)

    prediction = float(model.predict(input_data)[0])

    # Safety clamp (important for UI stability)
    prediction = max(0.0, min(1.0, prediction))

    st.success(f"🌊 Predicted Flood Probability: {prediction:.4f}")

    st.progress(prediction)

    # Risk Levels
    if prediction < 0.30:
        st.success("🟢 Low Flood Risk")
    elif prediction < 0.70:
        st.warning("🟡 Medium Flood Risk")
    else:
        st.error("🔴 High Flood Risk")