import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Approach & Workflow", layout="wide")

# --- Custom CSS for Dark Theme ---
st.markdown("""
<style>
body {
  background: linear-gradient(135deg, #121212, #1c1c2b);
  color: #e0e0e0;
}
h1, h2, h3 {
  color: #ffffff;
}
.section {
  padding: 30px 0;
}
.card {
  background: #1e1e2f;
  padding: 20px;
  border-radius: 12px;
  box-shadow: 0 0 12px rgba(0,0,0,0.4);
  margin-bottom: 25px;
}
</style>
""", unsafe_allow_html=True)

# --- Title ---
st.title("📖 Approach & Workflow")
st.write("This page explains the motivation, methodology, and full AI-powered pipeline behind the project.")

# --- Section 1: Problem Statement ---
with st.container():
    st.subheader("❌ The Problem")
    st.markdown("""
    Indian artisans face challenges like:
    - Lack of **digital presence** and marketing knowledge.  
    - Difficulty in setting **fair prices** for their artwork.  
    - Limited reach to **global buyers**.  
    - Platforms not tailored to **traditional art forms**.
    """)

# --- Section 2: Our Approach ---
with st.container():
    st.subheader("✅ Our Approach")
    st.markdown("""
    We built an **AI-powered Art Market Intelligence system** that:
    1. **Classifies** the art style using a YOLOv8 classifier.  
    2. **Predicts price** using a Random Forest regressor trained on ResNet18 features.  
    3. **Explains the market** with curated rule-based insights for each art style.  
    """)

# --- Section 3: Workflow ---
with st.container():
    st.subheader("🔄 Workflow")
    st.markdown("The system follows a clear end-to-end pipeline:")

    st.markdown("""
    **Dataset → Preprocessing → Training → Price Model → Inference → Market Insight**
    """)
    st.image("assets/1.jpg", caption="Pipeline Overview", use_container_width=True)

# --- Section 4: Key Features ---
with st.container():
    st.subheader("✨ Key Features")
    st.markdown("""
    - **Balanced Dataset Augmentation** for fairness across classes.  
    - **Price Prediction with Confidence Intervals** (Conformal Calibration).  
    - **Explainable AI** via Grad-CAM visualizations.  
    - **Packaged Wrapper (`.joblib`)** for easy deployment in apps (Streamlit/Django).  
    """)
