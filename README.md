# 🔐 AI-Powered Data Protection & Sensitive Data Governance System

A complete enterprise-grade Infosec system that detects, classifies, protects, and governs sensitive data using **BERT**, **Regex**, **Encryption**, **Policy Validation**, and **Anomaly Detection**. Designed for real-world PII/PCI protection including Aadhaar, PAN, phone numbers, email IDs, and transaction metadata.

---

## 🚀 Features

### 🧠 BERT-Based Sensitivity Classification
- Fine-tuned BERT model
- Categorizes text as **Public**, **Sensitive**, or **Highly Sensitive**
- Learns contextual patterns beyond regex

### 🔍 Hybrid Regex + ML Detection
- Aadhaar identification  
- PAN number extraction  
- Email detection  
- Phone number detection  
- Combines deep learning + deterministic rules for maximum accuracy

### 🔐 Data Protection Layer
- Aadhaar masking  
- Phone masking  
- AES-based encryption (Fernet) for highly sensitive fields  
- Ensures no plaintext PII is stored

### 📜 Policy Governance Engine
- YAML-based enterprise rules  
- Validates encryption requirements  
- Flags plaintext violations  
- Auto-generates compliance violations report

### 🚨 Anomaly Detection
- Isolation Forest model detects suspicious user behavior  
- Identifies unusual access times, spikes, or risky events  
- Generates anomaly report

### 📊 Interactive Streamlit Dashboard
- Sensitivity distribution charts  
- Protected data preview  
- Anomaly visualization  
- Policy violations summary  
- Downloadable compliance reports  

---

## 🧩 Tech Stack

- Python  
- Transformers  
- PyTorch  
- Scikit-learn  
- Pandas  
- Cryptography (Fernet AES)  
- YAML  
- Streamlit  

---

## 📁 Project Structure

```
BERT_pjct/
│
├── Complete_Data_Protection_Project.ipynb # Main pipeline notebook
├── data/ # Dataset
├── models/ # BERT + anomaly model
├── reports/ # Compliance outputs
├── dashboards/ # Streamlit app
├── src/
│ ├── detection/ # Regex + hybrid detection
│ ├── protection/ # Masking + encryption
│ ├── policy_engine/ # Rule validator
│ ├── anomaly_detection/ # Isolation Forest model
│ └── reporting/ # Report generator
└── config/ # YAML policies
```

---

