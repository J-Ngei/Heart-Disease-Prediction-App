# 🫀 Heart Disease Prediction App

This project predicts the presence or absence of heart disease based on clinical features using machine learning models. The app is built with **Streamlit** and uses a **Logistic Regression** model trained on a structured dataset.

---

## 📊 Dataset

- Source: [Kaggle Heart Disease Prediction Dataset](https://www.kaggle.com/datasets/rishidamarla/heart-disease-prediction)
- Records: 270
- Features: Age, Sex, Chest pain type, Blood pressure, Cholesterol, etc.

---

## 🧠 Models Used

- Logistic Regression (best performer)
- Random Forest
- XGBoost

---

## 📈 Model Performance

| Model              | Accuracy | ROC AUC |
|-------------------|----------|---------|
| Logistic Regression | 0.87     | 0.87    |
| Random Forest       | 0.80     | 0.80    |
| XGBoost             | 0.83     | 0.83    |

---

## 🚀 How to Run the App

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


