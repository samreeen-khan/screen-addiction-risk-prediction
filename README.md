# Screen Addiction Risk Prediction System

## Project Overview
The **Screen Addiction Risk Prediction System** is a beginner-friendly machine learning project developed using Python and Scikit-learn.

It predicts a person's screen addiction risk level based on daily digital habits, including screen time, social media usage, gaming hours, sleep duration, phone pickups, study/work hours, and notifications.

The model classifies the predicted risk into three categories:

- **Low**
- **Medium**
- **High**

## Technologies Used
- Python
- Scikit-learn
- CSV dataset
- Pickle (for saving and loading the trained model)

## Machine Learning Algorithm
This project uses the **Random Forest Classifier**, an ensemble learning algorithm that combines multiple decision trees to make predictions.

## Dataset Features

| Feature | Description |
|---|---|
| Daily_Screen_Time | Total daily screen time in hours |
| Social_Media_Hours | Daily social media usage |
| Gaming_Hours | Daily gaming time |
| Sleep_Hours | Daily sleep duration |
| Phone_Pickups | Number of daily phone pickups |
| Study_Work_Hours | Daily study or work hours |
| Notifications | Number of daily notifications |

**Target:** `Risk_Level` — Low, Medium, or High.

## Project Structure

```text
Screen_Addiction_Prediction/
│
├── screen_addiction.py
├── predict.py
├── screen_addiction_risk_dataset.csv
├── screen_addiction_model.pkl
├── README.md
├── requirements.txt
└── .gitignore
```

## How to Run the Project

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd Screen_Addiction_Prediction
```

### 3. Install the required library

```bash
pip install -r requirements.txt
```

### 4. Train the model

```bash
python screen_addiction.py
```

### 5. Make a prediction

```bash
python predict.py
```

Enter the requested information to receive a predicted risk category.

## Project Features
- Reads a dataset from a CSV file.
- Separates input features and target labels.
- Splits data into training and testing sets.
- Trains a Random Forest classification model.
- Evaluates model accuracy.
- Saves the trained model.
- Predicts risk levels for new user inputs.

## Important Note
This project uses a **synthetic educational dataset**. Its predictions are for machine learning practice and are not a medical diagnosis or a clinically validated assessment of screen addiction.

## Learning Objectives
- Understand basic machine learning concepts.
- Learn classification using Scikit-learn.
- Practice training and testing a model.
- Evaluate model accuracy.
- Save and reuse a trained machine learning model.

## Author
**Samreen Inayat**

Software Engineering Student  
University of Swat
