from fastapi import FastAPI
from pydantic import BaseModel
from classifier import ToxicityClassifier

app = FastAPI()

classifier = ToxicityClassifier(
    model_path="toxic_classifier.pkl",
    vectorizer_path="tfidf_vectorizer.pkl",
    config_path="config.json"
)

class AnalyzeRequest(BaseModel):
    user_id: str
    post_id: str
    text: str

class AnalyzeResponse(BaseModel):
    user_id: str
    post_id: str
    toxicity_score: float
    label: str
    action: str
    reasons: list
    threshold: float

@app.post("/analyze-text", response_model=AnalyzeResponse)
def analyze_text(request: AnalyzeRequest):
    scores = classifier.predict_toxicity(request.text)
    result = classifier.make_decision(scores, user_id=request.user_id, post_id=request.post_id, text=request.text)
    return result

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"model_version": "1.0.0"}