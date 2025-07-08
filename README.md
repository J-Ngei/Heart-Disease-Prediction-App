# 🫀 Heart Disease Prediction App

This machine learning project predicts the likelihood of heart disease in a patient based on clinical features. The app is built using Streamlit and deployed online for real-time predictions.

The project includes data preprocessing, feature encoding, model training and evaluation.

---

## 📊 Dataset

- Source: [Kaggle Heart Disease Prediction Dataset](https://www.kaggle.com/datasets/rishidamarla/heart-disease-prediction)
- Records: 270
- Features: Age, Sex, Chest pain type, Blood pressure, Cholesterol, Fasting blood sugar, ECG results, Max heart rate etc.

---

## Process
- Cleaned and preprocessed real-world health dataset
- Feature encoding and scaling
- Model training and performance comparison
- ROC and confusion matrix visualizations
- Live Streamlit application for user input and prediction

---

## 🧠 Models Used

- 🔹 Logistic Regression
- 🔸 Random Forest
- 🔺 XGBoost

---

## 📈 Model Performance

| Model              | Accuracy | ROC AUC |
|-------------------|----------|---------|
| Logistic Regression | 85%     | 0.90    |
| Random Forest       | 81%     | 0.87    |
| XGBoost             | 81%     | 0.87    |

---

## 🔍 Visualizations
- Confusion Matrix
- ROC Curve Comparison

---

### 🚀 Deployment
The application is deployed using Streamlit Cloud.

🔗 [Click here to try it live](https://heart-disease-prediction-app-gdmqpy3cxkpruxcthxdtfn.streamlit.app/)

---

## 🛠️ How to Run the App Locally

### 1. Clone the repository
```bash
git clone https://github.com/J-Ngei/Heart-Disease-Prediction-App.git
cd Heart-Disease-Prediction-App
```

### 2. Create a Virtual Environment (Optional but Recommended)
``` bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install Required Packages
``` bash
pip install -r requirements.txt
```
### 4. Run the Streamlit App
``` bash
streamlit run heart_disease_app.py
```
👤 Author

James Ngei

MSc Software Engineering Student | GIS Specialist | Aspiring ML Engineer

[LinkedIn](https://www.linkedin.com/in/james-ngei-61461b1a5) • [GitHub](https://github.com/J-Ngei)


