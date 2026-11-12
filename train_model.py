import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# 1. Load the dataset
print("Loading dataset...")
df = pd.read_csv('student_performance_dataset.csv')

# 2. Preprocess the data
# Drop identifying columns that don't affect predictions
if 'Student_ID' in df.columns:
    df = df.drop(columns=['Student_ID'])

# The image shows the last column contains the 'Pass'/'Fail' status. 
# We will isolate this as our target variable (y).
target_col = df.columns[-1]

# Encode categorical (text) columns into numbers for the ML model
label_encoders = {}
for column in df.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le

# Separate features (X) from the target outcome (y)
X = df.drop(columns=[target_col])
y = df[target_col]

# 3. Split data into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Initialize and train the model
print("Training Random Forest model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Evaluate model performance
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy on Test Data: {accuracy * 100:.2f}%")

# 6. Export the trained model for the FastAPI backend
model_filename = 'exam_predictor_model.pkl'
joblib.dump(model, model_filename)
print(f"Success! Model exported as {model_filename}")