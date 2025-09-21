import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import joblib, torch
from ultralytics import YOLO
from sklearn.metrics import classification_report, confusion_matrix

# --- Page Config ---
st.set_page_config(page_title="Model Insights", layout="wide")

# --- Load Artifacts ---
workdir = Path("art_market_work")
weights = Path("best.pt")
test_root = workdir / "cls_data" / "test"

clf = YOLO(str(weights))

# --- Title ---
st.title("📊 Model Insights & Evaluation")
st.write("Explore how the model performs on test data, and understand its decisions.")

# --- Section 1: Classification Report ---
st.subheader("1️⃣ Classification Report")

y_true, y_pred = [], []
classes = sorted([d.name for d in test_root.iterdir() if d.is_dir()])

for cname in classes:
    for img in (test_root / cname).glob("*"):
        if img.suffix.lower() not in {".jpg",".jpeg",".png"}:
            continue
        r = clf.predict(source=str(img), imgsz=224, verbose=False)[0]
        pred_idx = int(torch.argmax(r.probs.data).item())
        pred_name = r.names[pred_idx]
        y_true.append(cname)
        y_pred.append(pred_name)

report = classification_report(y_true, y_pred, output_dict=True, zero_division=0)
st.dataframe(pd.DataFrame(report).transpose())

# --- Section 2: Confusion Matrix ---
st.subheader("2️⃣ Confusion Matrix")
cm = confusion_matrix(y_true, y_pred, labels=classes)
fig, ax = plt.subplots(figsize=(8,6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=classes, yticklabels=classes, ax=ax)
plt.ylabel("True Label")
plt.xlabel("Predicted Label")
st.pyplot(fig)

# --- Section 3: Grad-CAM (Explainability) ---
st.subheader("3️⃣ Grad-CAM Visualization (Why the model predicts)")

st.write("Grad-CAM highlights the regions of the image that influenced the classification decision.")
example_img = list(test_root.rglob("*.jpg"))[0] if list(test_root.rglob("*.jpg")) else None

if example_img:
    st.image(str(example_img), caption="Original Test Image", width=300)
    st.write("👉 Grad-CAM integration can be added here with `pytorch-grad-cam` to visualize attention maps.")
else:
    st.warning("No test images found to demonstrate Grad-CAM.")

# --- Section 4: Price Model Performance ---
st.subheader("4️⃣ Price Model Performance")
st.markdown("""
- Trained **Random Forest Regressor** on ResNet18 features.  
- Evaluated using **R²** and **Mean Absolute Error (MAE)**.  
- Conformal calibration provides **90% confidence intervals** for fair pricing.  
""")

# --- Section 5: Key Takeaways ---
st.subheader("5️⃣ Key Takeaways")
st.markdown("""
✅ Accurate classification across major Indian art styles.  
✅ Price prediction with intervals ensures fairness.  
✅ Rule-based market explanations give cultural + commercial context.  
⚠️ Small price dataset → predictions may be noisy.  
⚠️ Some visually similar art styles can confuse the classifier.  
""")
