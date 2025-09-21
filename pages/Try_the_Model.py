# Try_the_Model.py
import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
import joblib, json
from ultralytics import YOLO
from PIL import Image
from model_wrapper import ArtMarketModel

# --- Page Config ---
st.set_page_config(page_title="Try the Model", layout="wide")

# --- Load Artifacts ---
clf_weights = "best.pt"
price_model_path = "rf_price.joblib"
conf_path = "conformal_calib.npz"
fallback_prices = json.load(open("fallback_prices.json"))
wrapper = joblib.load("art_market_model.joblib")

# --- Title ---
st.title("🖼️ Try the Art Market Model")
st.write("Upload artwork images and get predictions for **style, price, and market insights**.")

# --- Upload images ---
uploaded_files = st.file_uploader(
    "Upload one or more artwork images",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

# --- Run predictions ---
if uploaded_files:
    results = []

    for file in uploaded_files:
        # Save temporarily
        img_path = Path(file.name)
        with open(img_path, "wb") as f:
            f.write(file.getbuffer())

        # Run prediction with wrapper
        pred = wrapper.predict(str(img_path))
        price = pred["price"]

        # Load conformal interval
        q = float(np.load(conf_path)["q"]) if Path(conf_path).exists() else 0
        lo, hi = max(0, price - q), price + q

        # Display results
        st.image(Image.open(img_path), caption=pred["class"], use_container_width=True)
        st.markdown(f"**🎨 Art Style:** {pred['class']} (confidence: {pred['confidence']:.2f})")
        st.markdown(f"**💰 Estimated Price:** ₹{price:,.0f} (90% range: ₹{lo:,.0f} – ₹{hi:,.0f})")
        st.info(f"**📊 Market Insight:** {pred['market_explanation']}")

        # Save to list
        results.append({
            "image": file.name,
            "predicted_style": pred["class"],
            "confidence": pred["confidence"],
            "predicted_price": price,
            "interval_low": lo,
            "interval_high": hi,
            "market_explanation": pred["market_explanation"]
        })

    # Download results
    df = pd.DataFrame(results)
    st.download_button(
        "⬇️ Download Results as CSV",
        df.to_csv(index=False).encode("utf-8"),
        "predictions.csv",
        "text/csv"
    )
wrapper = ArtMarketModel(
    clf_weights="best.pt",
    price_model_path="rf_price.joblib",
    fallback_prices=json.load(open("fallback_prices.json")),
    explanations={
        "gond painting": "Heritage Folk Art — narrative motifs...",
        "warli painting": "Tribal minimalism...",
        # ... (rest of your MARKET_EXPLANATION dict)
    }
)
wrapper.load()
