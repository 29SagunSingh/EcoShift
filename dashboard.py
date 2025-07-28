import streamlit as st
import requests

st.set_page_config(page_title="EcoShift", layout="centered")
st.title("🌿 EcoShift Product Impact Checker")

# Set up score in session state if not already present
if "score" not in st.session_state:
    st.session_state.score = None

# Input Fields
packaging = st.selectbox("Packaging", ["plastic", "recyclable", "biodegradable"])
transport = st.selectbox("Transport", ["imported", "local"])
certs = st.multiselect("Certifications", ["FSC", "Fair Trade", "B Corp"])

# Get EcoScore Button
if st.button("Get EcoScore"):
    res = requests.post("http://localhost:5000/score", json={
        "packaging": packaging,
        "transport": transport,
        "certifications": certs
    })
    st.session_state.score = res.json()["eco_score"]
    st.metric("🌱 EcoScore", st.session_state.score)

# Get Smart Suggestion Button
if st.button("Get Smart Suggestion"):
    if st.session_state.score is not None:
        input_product = {
            "name": "Your Product",
            "category": "toiletries",
            "eco_score": st.session_state.score,
            "packaging": packaging,
            "transport": transport,
            "certifications": certs
        }
        res = requests.post("http://localhost:5000/suggest", json=input_product)
        data = res.json()
        st.subheader(f"💡 Try: {data['suggestion']['name']}")
        st.caption(data["reason"])
    else:
        st.error("Please calculate the EcoScore first.")