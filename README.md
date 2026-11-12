# Student Examination Performance Predictor

An interactive machine learning platform for assessing student performance and predicting examination outcomes based on historical grades, attendance, and study habits.

## Live Deployments

- **Frontend Application (Vercel):** [https://examresultpredictor1217.vercel.app/](https://examresultpredictor1217.vercel.app/)
- **Backend API Service (Render):** [https://examresultpredictor.onrender.com](https://examresultpredictor.onrender.com)
- **API Documentation (Swagger):** [https://examresultpredictor.onrender.com/docs](https://examresultpredictor.onrender.com/docs)

*Note: The backend service is hosted on Render's free tier. If inactive, the service may require 30 to 50 seconds to initialize on the first request.*

---

## Overview

This project provides an end-to-end machine learning system that evaluates student telemetry to predict final exam pass or fail outcomes. 

### Key Features
- **Cinematic Dark User Interface:** Dark basalt rock theme with warm amber accents, segmented controls, and a 3D layered card layout.
- **Interactive Parameter Console:** Real-time sliders and selectors for all 8 input features.
- **Preset Student Profiles:** One-click presets for high-achieving, average, and at-risk student scenarios.
- **Dynamic Prediction Insights:** Displays outcome status, model confidence score, and feature-driven guidance.
- **Model Overview Tab:** Details the Random Forest classifier metrics and feature importance rankings.

---

## Technical Specifications

### Architecture & Tech Stack
- **Client:** React 19, Vite, Axios, Custom CSS with 3D transforms
- **Server:** FastAPI, Uvicorn, Pydantic
- **Machine Learning:** Scikit-Learn (Random Forest Classifier), Pandas, NumPy, Joblib
- **Hosting:** Vercel (Client) and Render (API)

### Model Features
1. `Study_Hours_per_Week`: Weekly study duration (0–60 hours)
2. `Attendance_Rate`: Percentage of classes attended (30–100%)
3. `Past_Exam_Scores`: Historical examination average (0–100)
4. `Final_Exam_Score`: Benchmark final test score (0–100)
5. `Gender`: Student gender (0 = Female, 1 = Male)
6. `Parental_Education_Level`: Education level (0 = Bachelors, 1 = High School, 2 = Masters, 3 = PhD)
7. `Internet_Access_at_Home`: Internet availability (0 = No, 1 = Yes)
8. `Extracurricular_Activities`: Participation in extracurriculars (0 = No, 1 = Yes)

---

## API Reference

### Health Check
- **Endpoint:** `GET /`
- **Output:** `{"message": "Exam Predictor API is running!"}`

### Predict Result
- **Endpoint:** `POST /predict`
- **Payload Example:**
```json
{
  "Gender": 1,
  "Study_Hours_per_Week": 28,
  "Attendance_Rate": 84.5,
  "Past_Exam_Scores": 78,
  "Parental_Education_Level": 0,
  "Internet_Access_at_Home": 1,
  "Extracurricular_Activities": 1,
  "Final_Exam_Score": 75
}
```
- **Response Example:**
```json
{
  "predicted_result": "1"
}
```
*(1 represents Pass, 0 represents Fail)*

---

## Project Structure

```text
├── api/
│   ├── index.py                  # Serverless endpoint configuration
│   └── exam_predictor_model.pkl  # Trained model binary
├── frontend/
│   ├── src/
│   │   ├── App.jsx               # React UI & prediction form
│   │   ├── App.css               # Styling and 3D card layout
│   │   └── index.css             # Typography and base theme
│   ├── index.html
│   └── package.json
├── exam_predictor_model.pkl      # Random Forest model
├── main.py                       # FastAPI application entrypoint
├── requirements.txt              # Python server dependencies
├── student_performance_dataset.csv
├── train_model.py                # Model training script
└── vercel.json                   # Deployment routing
```

---

## Local Setup

### 1. Backend Service
```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### 2. Frontend Application
```bash
cd frontend
npm install
npm run dev
```
Access the application locally at `http://localhost:5173`.
