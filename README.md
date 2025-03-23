# 🚀 AI-Powered Crop Yield Prediction and Harvest Optimization

**An AI-driven system to predict maize yield and optimize harvest schedules for Kenyan farmers using machine learning and real-time weather data.**

---

## 📌 Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Model Training & Deployment](#model-training--deployment)
- [API Usage](#api-usage)
- [Example API Request](#example-api-request)
- [Deployment Guide](#deployment-guide)
- [Future Improvements](#future-improvements)
- [Contributors](#contributors)

---

## 📌 Introduction
Agriculture is the backbone of Kenya’s economy, yet smallholder farmers struggle with **unpredictable yields, poor harvest planning, and lack of data-driven decision-making tools**. This project leverages **machine learning and weather APIs** to provide **accurate maize yield predictions and harvest optimization recommendations.**

### Key Objectives
✅ Predict maize yield based on soil conditions, weather, and farming practices.
✅ Optimize harvest scheduling using real-time weather data.
✅ Provide a user-friendly Django-based API for farmers & stakeholders.

---

## 🎯 Features
🔹 **Machine Learning-Based Yield Prediction** – Uses a Random Forest model to predict maize yield.
🔹 **Harvest Optimization** – Determines the best time to harvest based on weather conditions.
🔹 **Real-Time Weather Data** – Integrates OpenWeather API for live weather updates.
🔹 **Django API for Predictions** – Exposes an API to accept input & return yield forecasts.
🔹 **User-Friendly Web Interface** – Simple HTML form for farmers to input data & get predictions.

---

## 🛠 Technologies Used
✅ **Python (Pandas, Scikit-Learn, Joblib)** – Model training & deployment  
✅ **Django & Django REST Framework** – API & Web App Backend  
✅ **OpenWeather API** – Real-time weather data integration  
✅ **PostgreSQL / SQLite** – Database for storing predictions  
✅ **Docker (Optional)** – Containerized deployment  
✅ **AWS / Heroku (Optional)** – Cloud deployment  

---

## 📂 Project Structure
```
CropYieldPrediction/  # Root directory
│
├── data/                  # Dataset storage
│   ├── raw/               # Raw CSV datasets
│   ├── processed/         # Cleaned & preprocessed data
│   └── external/          # External API data (weather, soil, etc.)
│
├── notebooks/             # Jupyter notebooks for model training
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_preprocessing.ipynb
│   ├── 03_model_training.ipynb
│   ├── 04_model_tuning.ipynb
│   └── 05_model_deployment.ipynb
│
├── models/                # Trained models storage
│   └── maize_yield_kenya_model.pkl
│
├── maize_yield_prediction/  # Django project
│   ├── yield_predictor/      # Django app
│   │   ├── views.py          # API logic
│   │   ├── urls.py           # URL routing
│   │   ├── models.py         # Database models
│   │   └── templates/        # Frontend (HTML)
│   │
│   ├── settings.py          # Django project settings
│   ├── manage.py            # Django management script
│
├── webapp/                  # (Optional) Frontend UI
│   ├── templates/           # HTML templates
│   ├── static/              # CSS/JS files
│
├── requirements.txt         # Python dependencies
├── README.md                # Documentation
└── .gitignore               # Files to ignore in version control
```

---

## 💾 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/CropYieldPrediction.git
cd CropYieldPrediction
```
### 2️⃣ Create a Virtual Environment & Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # (Mac/Linux)
venv\Scripts\activate  # (Windows)

pip install -r requirements.txt
```
### 3️⃣ Set Up Django & Database
```bash
cd maize_yield_prediction
python manage.py makemigrations
python manage.py migrate
```
### 4️⃣ Start Django Server
```bash
python manage.py runserver
```
📌 Open **http://127.0.0.1:8000/predict/** in your browser.

---

## 🌍 API Usage
### Endpoint:  
```
POST http://127.0.0.1:8000/predict/
```
### Request Parameters (Form-Data)
| Parameter     | Type  | Description                 |
|--------------|------|-----------------------------|
| `city`       | Text | Location for weather data   |
| `soil_pH`    | Float | Soil pH level (e.g., 6.5)  |
| `pesticides` | Float | Amount of pesticide usage  |

---

## 📌 Example API Request
### Postman / Curl Request
```json
{
    "city": "Eldoret",
    "soil_pH": 6.5,
    "pesticides": 3.2
}
```
### Expected Response
```json
{
    "city": "Eldoret",
    "temperature (°C)": 24.5,
    "humidity (%)": 78,
    "predicted_yield (tons/ha)": 3.56
}
```

---

## 🚀 Deployment Guide
### Deploy to Heroku
```bash
heroku login
heroku create crop-yield-predictor
git push heroku main
```
### Deploy to AWS
1. **Set up EC2 instance**  
2. **Install Python, Django, and Dependencies**  
3. **Run `gunicorn` server**  
4. **Configure Nginx & SSL (Optional)**  

---

## 🔮 Future Improvements
- 📡 IoT Sensor Integration – Collect real-time soil & weather data  
- 📈 Advanced AI Models – Experiment with deep learning  
- 🌍 Expand Crop Coverage – Support other crops beyond maize  
- 📊 Dashboard UI – Build a more interactive analytics dashboard  

---

## 👨‍💻 Contributors
- **Moses Abwova** – Lead Developer & AI Engineer 🚀  
- **Open to Contributions!** PRs welcome.  

🔗 **GitHub Repo:** [https://github.com/mosetf/CropYieldPrediction]
