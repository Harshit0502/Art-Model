import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Art Market Intelligence", layout="wide")

# --- Custom CSS for animation & styling ---
st.markdown("""
<style>
@keyframes fadeIn {
  from {opacity: 0;}
  to {opacity: 1;}
}
.title {
  font-size: 3rem;
  font-weight: 700;
  text-align: center;
  margin-top: 20%;
  animation: fadeIn 2s ease-in;
}
.subtitle {
  font-size: 1.2rem;
  text-align: center;
  color: #666;
  margin-bottom: 50px;
  animation: fadeIn 3s ease-in;
}
.button-container {
  display: flex;
  justify-content: center;
  gap: 30px;
  margin-top: 100px;
}
.stButton>button {
  font-size: 1.1rem;
  padding: 12px 30px;
  border-radius: 12px;
  font-weight: 600;
  background: linear-gradient(90deg, #ff9966, #ff5e62);
  color: white;
  border: none;
  transition: transform 0.2s ease-in-out;
}
.stButton>button:hover {
  transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# --- Title and subtitle ---
st.markdown('<div class="title">🎨 Indian Art Market Intelligence</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered classification • Price prediction • Market insights</div>', unsafe_allow_html=True)

# --- Three buttons at bottom ---
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("📖 Approach & Workflow"):
        st.switch_page("pages/1_Home.py")
with col2:
    if st.button("🖼️ Try the Model"):
        st.switch_page("pages/2_Try_the_Model.py")
with col3:
    if st.button("📊 Insights"):
        st.switch_page("pages/3_Model_Insights.py")
