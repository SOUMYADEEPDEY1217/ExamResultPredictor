import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd

app = FastAPI(docs_url="/api/docs", openapi_url="/api/openapi.json")

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Robust model path resolution for Vercel Serverless environment
current_dir = os.path.dirname(os.path.abspath(__file__))
candidate_paths = [
    os.path.join(current_dir, 'exam_predictor_model.pkl'),
    os.path.join(current_dir, '..', 'exam_predictor_model.pkl'),
    os.path.join(os.getcwd(), 'exam_predictor_model.pkl'),
    os.path.join(os.getcwd(), 'api', 'exam_predictor_model.pkl')
]

model = None
for path in candidate_paths:
    if os.path.exists(path):
        try:
            model = joblib.load(path)
            print(f"Loaded ML model successfully from: {path}")
            break
        except Exception as e:
            print(f"Error loading model from {path}: {e}")

@app.get("/")
@app.get("/api")
def read_root():
    return {
        "status": "online",
        "message": "Exam Predictor API is operational.",
        "model_loaded": model is not None
    }

@app.post("/predict")
@app.post("/api/predict")
async def predict_exam(request: Request):
    data = await request.json()
    
    if model is None:
        # Heuristic fallback if model binary failed to load in lambda
        study_hrs = float(data.get("Study_Hours_per_Week", 20))
        attendance = float(data.get("Attendance_Rate", 75))
        past_score = float(data.get("Past_Exam_Scores", 70))
        weight = (study_hrs * 0.8) + (attendance * 0.5) + (past_score * 0.3)
        result = "1" if weight >= 82 else "0"
        return {"predicted_result": result, "mode": "heuristic_fallback"}
    
    # Generate the prediction using the loaded model
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    
    return {"predicted_result": str(prediction[0]), "mode": "ml_model"}

