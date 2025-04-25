# 🏡 Predictive Modeling of House Prices Using Machine Learning

---

## 📌 Project Overview

Accurate house price prediction is crucial for buyers, sellers, and investors in the real estate market. This project applies machine learning models to analyze and predict house prices based on various features like location, size, amenities, and market indicators.

The study compares multiple ML models and identifies the best-performing one for accurate house price prediction.

---

## 📊 Dataset

- **Total Records:** 13,603 training samples, 6,700 testing samples
- **Total Features:** 14 influencing variables

### 🔑 Key Features:

- `Date` – Date of home sale  
- `Price` – Target variable (house price)  
- `Bedrooms`, `Bathrooms` – Number of rooms  
- `Living Area (m²)` – Size of the apartment  
- `Nice View`, `Perfect Condition` – Property condition  
- `Grade` – Construction quality (1-5)  
- `Has Basement`, `Renovated`, `Has Lavatory` – Additional features  
- `Single Floor` – Boolean for single-story homes  
- `Month` – Month of sale  
- `Quartile Zone` – Economic zone based on zip codes (1–4)

---

## 🤖 Machine Learning Models Used

- ✅ Ordinary Least Squares (OLS) Regression  
- ✅ K-Nearest Neighbors (KNN)  
- ✅ Decision Tree Regression  
- ✅ Support Vector Regression (SVR)  
- ✅ Neural Networks (NN)

---

## 📈 Evaluation Metrics

| Metric | Description |
|--------|-------------|
| **RMSE** | Root Mean Square Error - measures prediction error |
| **MAE**  | Mean Absolute Error - average error |
| **MSE**  | Mean Squared Error - penalizes large errors |
| **R²**   | Coefficient of Determination - predictive strength |

---

## 📊 Model Performance Comparison

| Model                   | RMSE (Test) | MAE (Test) | Best Fit? |
|------------------------|-------------|------------|-----------|
| OLS Regression         | 203,877     | 165,355    | ❌        |
| KNN (k=11)             | 215,942     | 175,190    | ❌        |
| Decision Tree          | 203,721     | 165,277    | ❌ (Overfitting) |
| Support Vector Regression (SVR) | 206,546     | 161,300    | ✅        |
| Neural Network         | 203,901     | 165,313    | ❌        |

📌 **Insight:** SVR showed the best performance, balancing accuracy and generalization.

---

## 🚀 Future Improvements

- Tune hyperparameters for SVR  
- Try advanced models like **Random Forest** and **XGBoost**  
- Enhance **feature engineering** and **data preprocessing**  

---

## 🛠 Installation & Usage

### 🔹 Clone the Repository

```bash
git clone https://github.com/PragyaP04/House-Price-Prediction.git
cd House-Price-Prediction