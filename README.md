# 🏥 Insurance Charges Prediction App

> Built by Darshan Modi — a polished Streamlit solution for predicting patient insurance costs with PyCaret.

```text
  _____                     _                         _   _                      _   _             _   _
 |_   _|                   | |                       | | (_)                    | | | |           | | (_)
   | |  _ __ ___   ___   __| | ___  _ __ ___   _ __  | |_ _ _ __   ___  _ __   | |_| | ___   ___ | |_ _  ___  _ __
   | | | '_ ` _ \ / _ \ / _` |/ _ \| '_ ` _ \ | '_ \ | __| | '_ \ / _ \| '_ \  |  _  |/ _ \ / _ \| __| |/ _ \| '_ \
  _| |_| | | | | | (_) | (_| | (_) | | | | | || |_) || |_| | | | | (_) | | | | | | | | (_) | (_) | |_| | (_) | | | |
 |_____|_| |_| |_|\___/ \__,_|\___/|_| |_| |_| | .__/  \__|_|_| |_|\___/|_| |_| |_| |_|\___/ \___/ \__|_|\___/|_| |_|
                                                | |                                                           
                                                |_|                                                           
```

---

## 🚀 Project Overview

This repository contains the full source code for an insurance charges prediction application built with:

- **Streamlit** for interactive UI
- **PyCaret** for regression model training and inference
- **Python** for data processing and prediction logic

It supports both:

- **Online prediction** for single records
- **Batch prediction** from CSV files

---

## 🎯 Features

- Predict medical insurance charges using patient demographics
- Clean, modern Streamlit interface with sidebar navigation
- Batch CSV upload and result download
- Fast inference using a pre-trained PyCaret model
- Compatible with Windows, macOS, and Linux

---

## 💻 Built By

**Darshan Modi**

A practical insurance prediction app with a professional user experience and easy deployment.

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/darshanM0di/Insurance-charges-prediction-app-.git
cd insurance-charges-prediction-app/insurance_project_pycaret
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

### Option 1: Use the batch file

```bash
cd "c:\Users\apple\OneDrive\Desktop\new project.worktrees\copilot-clone-repo-insurance-charges-prediction"
./run_app.bat
```

### Option 2: Run directly with Streamlit

```bash
cd insurance_project_pycaret
streamlit run app.py
```

Open the app at `http://localhost:8501`.

---

## 📁 Project Structure

```
insurance-charges-prediction-app/
├── README.md
├── ARCHITECTURE.md
├── DOCUMENTATION_INDEX.md
├── PROJECT_REPORT.md
├── APP_PREVIEW.html
├── run_app.bat
├── insurance_charges.csv
├── assets/
│   ├── streamlit_screenshot.png
│   ├── image.png
│   └── image.jpeg
└── insurance_project_pycaret/
    ├── app.py
    ├── insurance.pkl
    ├── requirements.txt
    ├── README.md
    └── test_app.py
```

---

## ✅ Quick Start

- Use **online mode** for single patient predictions
- Use **batch mode** for CSV scoring
- Download results directly from the app

---

## 📌 Notes

- Keep the `insurance_project_pycaret` folder as the app root for Streamlit runs
- Update `requirements.txt` if you add new Python packages
- Use the provided `test_app.py` to verify app behavior
