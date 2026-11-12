# Exam Predictor AI

A fullstack Machine Learning web application designed with a luxury, cinematic dark UI inspired by modernist aesthetics. It predicts student examination outcomes based on multi-dimensional telemetry (study hours, attendance rate, past performance, and demographics).

![Tech Stack](https://img.shields.io/badge/Frontend-React_19_+_Vite-61dafb?logo=react)
![Backend](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi)
![ML](https://img.shields.io/badge/ML-Scikit--Learn-F7931E?logo=scikit-learn)
![Deployment](https://img.shields.io/badge/Deploy-Vercel-black?logo=vercel)

---

## Features

- **Cinematic Dark Rock UI:** Deep volcanic/basalt contours, warm amber rim lighting, and atmospheric depth.
- **Modernist Hero Canvas:**
  - Segmented pill switcher (`CREATE` / `EXPLORE`).
  - High-fashion typography with luxury italic serif accents.
  - Interactive 3D fanned card deck with warm candle ambient glow.
- **Interactive Student Telemetry Console:**
  - One-click scholar/average/at-risk candidate presets.
  - Interactive sliders & segmented pills for all 8 parameters.
  - Real-time ML prediction with confidence scores and dynamic guidance.
- **Model Insights & Architecture:**
  - Explore mode detailing Random Forest (100 estimators) metrics and feature importance ranking.
- **Vercel Fullstack Ready:**
  - Python Serverless Function under `/api/index.py`.
  - Vite static frontend under `frontend/`.

---

## Project Structure

```text
├── api/
│   ├── index.py                  # Vercel Python Serverless Function (FastAPI)
│   └── exam_predictor_model.pkl  # Trained ML model for serverless runtime
├── frontend/
│   ├── src/
│   │   ├── App.jsx               # Main React application & predictor console
│   │   ├── App.css               # Cinematic dark UI & 3D card styling
│   │   ├── index.css             # Typography & global theme variables
│   │   └── main.jsx
│   ├── index.html
│   ├── package.json
│   ├── vercel.json               # SPA rewrites config
│   └── vite.config.js
├── exam_predictor_model.pkl      # Pre-trained Random Forest model
├── main.py                       # Local FastAPI backend
├── requirements.txt              # Python serverless dependencies
├── student_performance_dataset.csv
├── train_model.py                # Model training pipeline
├── vercel.json                   # Root Vercel build & route configuration
└── package.json                  # Root build scripts
```

---

## Local Development

### 1. Backend (FastAPI)
```powershell
pip install -r requirements.txt
uvicorn main:app --reload
```
API runs on `http://127.0.0.1:8000`.

### 2. Frontend (React + Vite)
```powershell
cd frontend
npm install
npm run dev
```
Open `http://localhost:5173` in your browser.

---

## Deploy to Vercel

1. Import this repository in [Vercel](https://vercel.com/new).
2. Keep the **Root Directory** as `.` (root).
3. Vercel automatically detects `vercel.json` to build the frontend and deploy the serverless Python API at `/api/predict`.
4. Click **Deploy**!
