import joblib
from ultralytics import YOLO
from PIL import Image
import torchvision.transforms as T
import torch

class ArtMarketModel:
    def __init__(self, clf_weights, price_model_path, fallback_prices, explanations):
        self.clf_weights = clf_weights
        self.price_model_path = price_model_path
        self.fallback_prices = fallback_prices
        self.explanations = explanations
        self._clf = None
        self._price_model = None

    def load(self):
        if self._clf is None:
            self._clf = YOLO(self.clf_weights)
        if self._price_model is None:
            self._price_model = joblib.load(self.price_model_path)

    def predict(self, img_path):
        res = self._clf.predict(source=img_path, imgsz=224, verbose=False)[0]
        probs = res.probs.data.cpu().numpy()
        top_idx = int(probs.argmax())
        cname = res.names[top_idx]
        conf = float(probs[top_idx])

        # fallback pricing
        price = self.fallback_prices.get(cname, 20000)

        expl = self.explanations.get(cname, "General market context")
        return {"class": cname, "confidence": conf, "price": price, "market_explanation": expl}
