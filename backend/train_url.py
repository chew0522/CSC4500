import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import pickle

# Load the dataset
df = pd.read_csv('C:\\Users\\dcbc0\\Desktop\\UPM\\Sem 4\\csc4500\\backend\\Phishing_URL.csv')

# Drop missing values in URL or Label
df.dropna(subset=['URL', 'Label'], inplace=True)

# Define features and labels
X = df['URL'].astype(str)
y = df['Label']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build pipeline: TF-IDF vectorizer + classifier
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(analyzer='char_wb', ngram_range=(3, 5))),
    ('clf', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Train model
pipeline.fit(X_train, y_train)

# Evaluate
y_pred = pipeline.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Save model
with open('url_model.pkl', 'wb') as f:
    pickle.dump(pipeline, f)
