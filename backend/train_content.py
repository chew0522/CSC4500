import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load the dataset
df = pd.read_csv('C:/Users/dcbc0/Desktop/UPM/Sem 4/csc4500/backend/Phishing_Email.csv')

# Combine subject + content into a single text field
df['Text'] = df['content'].fillna('')
label_map = {'Safe Email': 0, 'Phishing Email': 1}
df['label'] = df['label'].map(label_map)

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(df['Text'], df['label'], test_size=0.2, random_state=42)

# Create a text classification pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('clf', RandomForestClassifier())
])

# Train the model
pipeline.fit(X_train, y_train)

# Make predictions
y_pred = pipeline.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))

import pickle
with open('phishing_model.pkl', 'wb') as f:
    pickle.dump(pipeline, f)

