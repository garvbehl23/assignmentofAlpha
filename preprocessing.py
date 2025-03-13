import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# Load the dataset
data = pd.read_csv("data.xlsx")

# Handle missing values
data.fillna(method='ffill', inplace=True)

# Encode categorical variables
label_encoders = {}
for column in ['Speciality', 'Region']:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le

# Extract hour from login/logout times
data['Login_Hour'] = pd.to_datetime(data['Login Time']).dt.hour
data['Logout_Hour'] = pd.to_datetime(data['Logout Time']).dt.hour

# Define target variable (e.g., attended survey: 1 or 0)
data['Attended_Survey'] = (data['Time spent'] > data['Time spent'].median()).astype(int)

# Features and target
X = data[['Speciality', 'Region', 'Login_Hour', 'Logout_Hour', 'Count of Attempts']]
y = data['Attended_Survey']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save preprocessed data and encoders
joblib.dump(X_train, "X_train.pkl")
joblib.dump(y_train, "y_train.pkl")
joblib.dump(label_encoders, "label_encoders.pkl")