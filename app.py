import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Art Market Intelligence", layout="wide")

# --- Custom CSS (Dark Theme) ---
st.markdown("""
<style>
body {
  margin: 0;
  padding: 0;
  background: linear-gradient(135deg, #1e1e2f, #121212);
  color: #e0e0e0;
}
.container {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100vh;
  text-align: center;
  animation: fadeIn 2s ease-in;
}
.top-section {
  flex: 4; /* ~40% */
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.bottom-section {
  flex: 6; /* ~60% */
  display: flex;
  justify-content: center;
  align-items: flex-start;
  margin-top: 20px;
}
.title {
  font-size: 3.2rem;
  font-weight: 800;
  margin-bottom: 15px;
  color: #ffffff;
  text-shadow: 0 0 12px rgba(255, 94, 98, 0.6);
}
.subtitle {
  font-size: 1.3rem;
  color: #bbbbbb;
}
.button-container {
  display: flex;
  gap: 40px;
}
.stButton>button {
  font-size: 1.1rem;
  padding: 14px 36px;
  border-radius: 12px;
  font-weight: 600;
  background: linear-gradient(90deg, #ff5e62, #ff9966);
  color: white;
  border: none;
  box-shadow: 0 0 15px rgba(255, 94, 98, 0.4);
  transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
}
.stButton>button:hover {
  transform: scale(1.07);
  box-shadow: 0 0 25px rgba(255, 94, 98, 0.8);
}
@keyframes fadeIn {
  from {opacity: 0;}
  to {opacity: 1;}
}
</style>
""", unsafe_allow_html=True)

# --- Page Layout ---
st.markdown("""
<div class="container">
  <div class="top-section">
    <div class="title">🎨 Indian Art Market Intelligence</div>
    <div class="subtitle">AI-powered classification • Price prediction • Market insights</div>
  </div>
  <div class="bottom-section">
    <div class="button-container">
      <form action="pages/1_Home.py"><button>📖 Approach & Workflow</button></form>
      <form action="pages/2_Try_the_Model.py"><button>🖼️ Try the Model</button></form>
      <form action="pages/3_Model_Insights.py"><button>📊 Insights</button></form>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

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
