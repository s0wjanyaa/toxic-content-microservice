import joblib
import json
import re
from langdetect import detect

CLASS_INDEX_TO_NAME = {
    0: "toxic",
    1: "insult",
    2: "harassment",
    3: "obscene",
    4: "threat",
    5: "identity_attack"
}

class ToxicityClassifier:
    def __init__(self, model_path, vectorizer_path, config_path):
        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)
        with open(config_path) as f:
            self.config = json.load(f)
        self.enabled_categories = self.config.get("enabled_categories", list(CLASS_INDEX_TO_NAME.values()))

    def clean_text(self, text):
        text = str(text).lower()
        text = re.sub(r'[^a-z0-9\s]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    def predict_toxicity(self, text):
        cleaned = self.clean_text(text)
        X = self.vectorizer.transform([cleaned])
        probs = self.model.predict_proba(X)[0]
        scores = {CLASS_INDEX_TO_NAME[int(k)]: float(v) for k, v in zip(self.model.classes_, probs)}
        return scores
    
    def is_non_english(self, text):
        try:
            return detect(text) != "en"
        except:
            return True

    def make_decision(self, scores, user_id=None, post_id=None, text=None):
        threshold = self.config["toxicity_threshold"]
        flag_threshold = self.config["flag_threshold"]
        enabled = self.enabled_categories

        if text and self.is_non_english(text):
            return {
                "user_id": user_id,
                "post_id": post_id,
                "toxicity_score": 0.0,
                "label": "abusive",
                "action": "flagged",
                "reasons": ["slang"],
                "threshold": threshold
            }

        reasons = []
        for cat in enabled:
            if cat == "harassment":
                if any(scores.get(mapped, 0) >= threshold for mapped in ["toxic", "insult"]):
                    reasons.append("harassment")
            elif scores.get(cat, 0) >= threshold:
                reasons.append(cat)
        max_score = max(scores.values()) if scores else 0.0
        if max_score >= threshold:
            label = "toxic"
            action = "blocked"
        elif max_score >= flag_threshold:
            label = "abusive"
            action = "flagged"
        else:
            label = "safe"
            action = "approved"
        result = {
            "user_id": user_id,
            "post_id": post_id,
            "toxicity_score": float(max_score),
            "label": label,
            "action": action,
            "reasons": reasons,
            "threshold": threshold
        }
        return result