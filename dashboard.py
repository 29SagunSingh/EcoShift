import streamlit as st

st.set_page_config(page_title="EcoShift", layout="centered")
st.title("🌿 EcoShift Product Impact Checker")

# Calculate EcoScore directly (formerly in Flask)
def calculate_eco_score(packaging, transport, certifications):
    score = 0
    if packaging == "biodegradable":
        score += 40
    elif packaging == "recyclable":
        score += 20
    if transport == "local":
        score += 30
    if "FSC" in certifications or "Fair Trade" in certifications:
        score += 30
    return min(score, 100)

# Smart Suggestion logic (can be improved later)
def suggest_better_product(product):
    reasons = []
    suggestion = product.copy()

    if product["packaging"] == "plastic":
        suggestion["packaging"] = "biodegradable"
        reasons.append("Try switching to biodegradable packaging.")
    if product["transport"] == "imported":
        suggestion["transport"] = "local"
        reasons.append("Locally sourced products reduce emissions.")
    if "FSC" not in product["certifications"]:
        suggestion["certifications"].append("FSC")
        reasons.append("Add FSC certification for better environmental impact.")

    suggestion["eco_score"] = calculate_eco_score(
        suggestion["packaging"],
        suggestion["transport"],
        suggestion["certifications"]
    )
    return suggestion, " ".join(reasons)

# Session state setup
if "score" not in st.session_state:
    st.session_state.score = None

# Inputs
packaging = st.selectbox("Packaging", ["plastic", "recyclable", "biodegradable"])
transport = st.selectbox("Transport", ["imported", "local"])
certs = st.multiselect("Certifications", ["FSC", "Fair Trade", "B Corp"])

# Get Score
if st.button("Get EcoScore"):
    st.session_state.score = calculate_eco_score(packaging, transport, certs)
    st.metric("🌱 EcoScore", st.session_state.score)

# Get Suggestion
if st.button("Get Smart Suggestion"):
    if st.session_state.score is not None:
        product = {
            "name": "Your Product",
            "category": "toiletries",
            "eco_score": st.session_state.score,
            "packaging": packaging,
            "transport": transport,
            "certifications": certs.copy()
        }
        suggestion, reason = suggest_better_product(product)
        st.subheader(f"💡 Try: {suggestion['name']}")
        st.write(f"**Packaging:** {suggestion['packaging']}")
        st.write(f"**Transport:** {suggestion['transport']}")
        st.write(f"**Certifications:** {', '.join(suggestion['certifications'])}")
        st.write(f"**New EcoScore:** {suggestion['eco_score']}")
        st.caption(reason)
    else:
        st.error("Please calculate the EcoScore first.")