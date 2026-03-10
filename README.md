🇹🇳 Tunisia Car Price Predictor: Guided ML Project
GitHub stars
GitHub forks
GitHub issues
GitHub license

📋 Course Overview
This repository contains the complete materials for the Tunisia Car Price Predictor project. This is a 100% project-based course where you will learn to build, track, and deploy a complete Machine Learning solution for predicting car prices in Tunisia.

🚀 Project Synopsis
The repository provides a complete example based on Tunisia Car Price Prediction. The goal is to build a full-stack ML application that estimates car prices with confidence intervals, using real-world data from Tunisia.

⚠️ Important
This is a baseline example. Each team must choose their own dataset and objective, which must be validated by the tutor before proceeding.

🛠️ Installation & Setup
To run this project locally, clone the repository and install the dependencies:

Bash

git clone https://github.com/your-username/tunisia-car-price-predictor.git
cd tunisia-car-price-predictor

# Install backend dependencies
cd code/tunisia-car-api
pip install -r requirements.txt

# Install frontend dependencies
cd ../client
npm install
📅 7-Week Roadmap
Week	Topic
Week 1	Setup, Data Collection & EDA
Week 2	Preprocessing & Feature Engineering
Week 3	Modeling (Boosting) & MLflow
Week 4	API Development (FastAPI)
Week 5	Frontend Development (React)
Week 6	Containerization (Docker)
Week 7	Deployment & Final Review
🏗️ Project Architecture
mermaid

graph TD;
    A[Raw Data] --> B[EDA & Preprocessing];
    B --> C[Feature Engineering];
    C --> D[Model Training];
    D --> E[MLflow Tracking];
    E --> F[FastAPI Backend];
    F --> G[React Frontend];
    G --> H[User];
    I[Docker] --> J[Deployment to Render/Vercel];
📁 Repository Structure
text

tunisia-car-price-predictor/
├── guide_projet.pdf: Detailed global project guide (Full Roadmap).
├── cours/: Course notes and slides (PDF).
├── code/: Structured and modular Python scripts.
│   ├── tunisia-car-api/: FastAPI backend.
│   │   ├── app/: Application code.
│   │   ├── requirements.txt: Dependencies.
│   │   └── Dockerfile: Containerization config.
│   └── client/: React frontend.
│       ├── src/: Application code.
│       └── package.json: Dependencies.
├── tutos/: Step-by-step tutorials (PDF).
├── data/: Datasets and generated visualizations.
│   ├── raw/: Raw car price data from Tunisia.
│   └── processed/: Cleaned and preprocessed data.
└── README.md: This file.
🎯 How to Use This Repository
Clone the repository:
Bash

git clone https://github.com/your-username/tunisia-car-price-predictor.git
Follow the tutorials in the tutos/ folder step-by-step.
Use the code/ folder as a reference for structuring your own project.
Adapt the data to your own dataset by modifying the data processing scripts.
🚀 Deployment
🐳 Backend Deployment (Render)
Bash

# Push code to GitHub
git add .
git commit -m "Initial commit"
git push origin main

# Deploy to Render:
# 1. Go to https://render.com → New Web Service → Connect GitHub
# 2. Set Build Command: docker build -t tunisia-car-api .
# 3. Set Start Command: docker run -p 8000:8000 tunisia-car-api
# 4. Add Environment Variable: PORT=8000
🎨 Frontend Deployment (Vercel)
Bash

# Push code to GitHub
git add .
git commit -m "Initial commit"
git push origin main

# Deploy to Vercel:
# 1. Go to https://vercel.com/new → Import Git Repo
# 2. Vercel will automatically build and deploy your frontend
📄 License
This project is licensed under the MIT License — see the LICENSE file for details.

© 2025-2026 [Your Name]
GitHub: https://github.com/your-username
LinkedIn: https://linkedin.com/in/your-username
Email: your-email@example.com
🎯 Final Notes
This project is a complete, production-ready ML application that demonstrates:

Full-Stack Development: Backend + Frontend + Deployment.
ML Engineering: Data processing, model training, feature engineering.
DevOps: Docker, CI/CD, cloud deployment.
It’s perfect for showcasing your skills to recruiters, clients, or investors! 🚀

