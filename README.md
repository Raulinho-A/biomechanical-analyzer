# Biomechanical Analyzer

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)

A computer vision and machine learning-based system designed to evaluate the biomechanical precision of strength exercises. This application helps gym users improve their technique and reduce the risk of injuries through pose estimation and feedback.

---

## 🚀 Project Overview

**Purpose:**  
To develop a web-based prototype capable of analyzing exercise performance and providing visual and textual feedback based on biomechanical standards.

---

## 🧠 Key Features

- 2D pose estimation using **MediaPipe**
- Biomechanical analysis of the **squat** exercise
- Trained machine learning model to classify correct vs incorrect execution
- Visual (skeleton overlay) and textual feedback

---

## 🛠 Tech Stack

- **Python 3.10+**
- **MediaPipe** – Pose estimation
- **OpenCV** – Video processing
- **scikit-learn / -** – ML model training
- **Jupyter Notebooks** – EDA, model training & evaluation

---

## 📁 Project Structure

```
├── LICENSE            <- License of the project
├── HISTORY.md         <- The HISTORY changes track
├── README.md          <- The top-level README for developers using this project.
|
├── .gitignore
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
├── Dockerfile
├── main.py            <- Main script for running the processing pipeline
|
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── models/            <- Trained and serialized models, model predictions, or model summaries
│   ├── trained/       <- Final machine learning models ready for inference (e.g., .pkl, .joblib)
│   ├── checkpoints/   <- Intermediate model weights saved during training (e.g., for resuming)
│   └── mediapipe/     <- Pretrained task models used by MediaPipe (e.g., pose_landmarker.task)
│
├── notebooks          <- Jupyter notebooks for exploration, training, and evaluation
│                         Naming: <order>-<initials>-<description>.ipynb, e.g. 1.0-lea-exploration.ipynb
│
│
├── references         <- Background material and references.
│   ├── biomechanics.md       # Biomechanics notes and theory
│   └── papers/               # Academic sources or research papers (PDF, links)
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
└── analyzer           <- Source code for use in this project.
    │
    ├── __init__.py             <- Marks this directory as a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Data loading and preprocessing logic
    │
    ├── features.py             <- Feature extraction functions
    │
    ├── plots.py                <- Visualization utilities
    │
    ├── modeling                <- Machine learning pipeline 
    │   ├── __init__.py 
    │   ├── train.py            <- Model training script
    │   └── predict.py          <- Model inference and predictions
    |
    ├── vision                  <- OpenCV + MediaPipe
    |   ├── extract_keypoints.py
    │   └── preprocess_video.py
    |
    └── api                     <- FastAPI backend module (to be implemented)
```

---

## 🚧 Scope of the Project (v0.1.0)

**Included:**
- Evaluation of a single exercise (squat) in controlled environments
- 2D analysis and model feedback
- Functional prototype and notebooks

**Excluded:**
- Real-time multi-user detection
- 3D pose estimation
- Database integration or user login

---

## 📊 Metrics & Objectives

- Reduce technical errors during squat execution
- Improve similarity with optimal biomechanical patterns
- Increase the percentage of properly executed repetitions

---

## 📦 Installation

```bash
git clone https://github.com/Raulinho-A/biomechanical-analyzer.git
cd biomechanical-analyzer
pip install -r requirements.txt
```

## 🧪 Run
```bash
python main.py
```
Or explore the system via the Jupyter notebooks under notebooks/.

## 📄 License
This project is licensed under the MIT License.

