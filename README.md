# 🔍 CreditLens: Enterprise Credit Risk Assessment & Model Validation Pipeline

<p align="center">
  <b>An end-to-end automated credit risk scoring and validation framework designed for Model Risk Management (MRM) and Operational Risk Oversight.</b>
</p>

---

## 🚀 Overview
**CreditLens** is a lightweight, high-performance credit default risk assessment engine. Built specifically to handle portfolio stress-testing and Probability of Default (PD) calculations, it provides real-time model interpretability, statistical model validation, and an interactive executive intelligence portal.

---

## 🛠️ Key Features
* **Automated Risk Scoring Engine:** Predicts live borrower default probabilities based on credit limits, repayment histories, and statement balances.
* **Model Validation Metrics:** Computes out-of-sample performance metrics including **ROC-AUC scores** and detailed classification reports.
* **Interactive MI Dashboard:** Built via Streamlit to enable real-time risk parameter stress-testing.
* **Lightweight Architecture:** Optimized for low-footprint execution (<50MB total disk allocation, highly memory-efficient for 8GB RAM systems).

---

## 📂 Project Structure
```text
CreditLens/
│
├── data/
│   └── credit_data.csv        # Primary credit default client dataset
├── models/
│   └── trained_model.pkl      # Serialized machine learning model artifact
├── app.py                     # Streamlit web application interface
├── train.py                   # Model training and validation script
└── requirements.txt           # Project dependencies
