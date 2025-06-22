from flask import Flask, request, jsonify
import pickle
import re
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow requests from frontend

# Load the email phishing detection model
with open('C:\\Users\\dcbc0\\Desktop\\UPM\\Sem 4\\csc4500\\backend\\phishing_model.pkl', 'rb') as f:
    email_model = pickle.load(f)

# Load the URL phishing detection model (expects only 'URL' as input)
with open('C:\\Users\\dcbc0\\Desktop\\UPM\\Sem 4\\csc4500\\backend\\url_model.pkl', 'rb') as f:
    url_model = pickle.load(f)

# Preprocess email subject and content
def preprocess_text(subject, content):
    combined_text = f"{subject} {content}"
    combined_text = re.sub(r'http\S+|www\S+', '', combined_text)  # remove URLs
    combined_text = re.sub(r'[^a-zA-Z0-9 ]', '', combined_text)    # remove special characters
    combined_text = combined_text.lower()
    return combined_text

# Extract first URL found in subject/content
def extract_url(subject, content):
    combined_text = f"{subject} {content}"
    urls = re.findall(r'https?://\S+|www\.\S+', combined_text)
    if urls:
        return urls[0].strip().lower()
    return ''

# Prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    subject = data.get('subject', '')
    content = data.get('content', '')

    # Email model prediction
    cleaned_text = preprocess_text(subject, content)
    email_prediction = email_model.predict([cleaned_text])[0]
    email_label = 'phishing' if email_prediction == 1 else 'safe'

    # URL model prediction
    url = extract_url(subject, content)
    if url:
        url_prediction = url_model.predict([url])[0]
    else:
        url_prediction = 'no_url_found'

    url_label = 'phishing' if url_prediction == 1 else 'safe'

    return jsonify({
        'email_prediction': email_label,
        'url_prediction': url_label
    })

if __name__ == '__main__':
    app.run(debug=True)
