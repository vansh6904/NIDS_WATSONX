(I HAVE ADDED AN ADDITIONAL PYTHON FILE FOR FRONTEND USING STREAMLIT (WHICH CANNOT BE DONE IN JUPYTER NOTEBOOK)
# 🛡️ Network Intrusion Detection System (NIDS) using Machine Learning

This project presents a Machine Learning-based Network Intrusion Detection System (NIDS) that classifies network traffic as either normal or a type of intrusion. It leverages the Random Forest algorithm and is deployed using IBM Cloud tools for scalable model development and deployment.

---

## 🚀 Project Overview

The goal of this system is to detect potential intrusions in network traffic using supervised learning. The model is trained on a labeled dataset containing various types of attacks and normal traffic.

---

## 🧠 Tech Stack

- **Machine Learning**: Random Forest Classifier
- **Data Preprocessing**: Pandas, Scikit-learn
- **Class Balancing**: SMOTE (Synthetic Minority Oversampling Technique)
- **Cloud Tools**: IBM Watson Studio, IBM Cloud Object Storage
- **Deployment Ready**: Real-time or batch predictions with confidence score support

---

## 📊 Dataset

The dataset used includes multiple network traffic samples labeled as:
- Normal
- Intrusion types (e.g., DoS, Probe, R2L, U2R)

---

## ⚙️ Features

- Feature selection and encoding
- Class balancing using SMOTE
- Hyperparameter tuning with GridSearchCV
- Real-time prediction support
- Cloud deployment-ready architecture

---

## 🧪 Training Process

1. **Preprocessing**: Categorical encoding, dropping constant columns, normalizing features
2. **Balancing**: SMOTE applied to handle class imbalance
3. **Split**: Train-test split (80:20)
4. **Model**: Random Forest Classifier with Grid Search for tuning
5. **Validation**: 5-fold Cross Validation to ensure generalization

---

## 🔮 Prediction

- Inputs preprocessed using same training pipeline
- Outputs:
  - Class label (e.g., normal, DoS, etc.)
  - Confidence score for alert thresholds

---

## 🌐 Deployment

The model and pipeline can be deployed using:
- **IBM Watson Machine Learning**
- **Streamlit or Flask** for frontend visualization
- **Cloud Object Storage** for managing input/output logs

---
## 📌 Future Scope

- Integrate with live traffic sniffers like Wireshark or Scapy
- Extend support to multiple cloud platforms (Azure, AWS)
- Optimize latency for edge deployment
- Incorporate Deep Learning for packet-level analysis

---

## 📁 Project Structure

```bash
├── data/
│   └── nids_dataset.csv
├── models/
│   └── random_forest_model.pkl
├── notebooks/
│   └── training_pipeline.ipynb
├── app/
│   └── predict.py
├── README.md
└── requirements.txt
