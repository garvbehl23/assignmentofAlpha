

# Doctor Survey Attendance Predictor

## Overview
This project predicts doctors (based on NPIs) likely to attend a survey at a specific time. It uses machine learning and provides a web app for user input and CSV export.

---

## Dataset
The dataset contains doctor details like Speciality, Region, Login/Logout Time, Time spent, and Count of Attempts.  
[Dataset Link](https://drive.google.com/drive/folders/1O4uMxC9hVE9Y_T3A1E4DvJpEQM38yj6m?usp=sharing)

---

## Features
- Input: Time of day (hour, e.g., 6 for 6:00 AM).
- Output: List of doctors (NPIs) likely to attend the survey.
- Download: Export results as a CSV file.
- Polished UI with progress bar and dynamic feedback.

---

## Installation
1. Clone the repository:
   
2. Install dependencies:
   
   pip install pandas numpy scikit-learn streamlit joblib
   
3. Run the app:
   
   streamlit run app.py
  

---



## Project Structure
```
project/
├── README.md          # Documentation
├── preprocessing.py   # Data preprocessing
├── train_model.py     # Model training
├── app.py             # Web app code
├── data.csv           # Dataset
├── model.pkl          # Trained model
└── label_encoders.pkl # Encoders
```

---

## How It Works
1. Input: User enters a specific hour (0–23).
2. Processing: Filters doctors and predicts likelihood using a trained model.
3. Output: Displays and exports predicted NPIs as a CSV file.

---

## Future Enhancements
- Add more features for better accuracy.
- Integrate email functionality for direct invites.

---

## Contact
For questions, contact:  
Email: your-email@example.com  
GitHub: 
(https://github.com/garvbehl23)

--- 

Let me know if you need further adjustments! 😊
