from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd

# Initialize the FastAPI app
app = FastAPI()

# Enable CORS so your React frontend can communicate with this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for local development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the trained machine learning model
print("Loading model...")
model = joblib.load('exam_predictor_model.pkl')

@app.get("/")
def read_root():
    return {"message": "Exam Predictor API is running!"}

@app.post("/predict")
async def predict_exam(request: Request):
    # Receive JSON data from the frontend
    data = await request.json()
    
    # Convert the JSON dictionary into a Pandas DataFrame
    df = pd.DataFrame([data])
    
    # Generate the prediction using the loaded model
    prediction = model.predict(df)
    
    # Return the result (e.g., 'Pass' or 'Fail')
    return {"predicted_result": str(prediction[0])}