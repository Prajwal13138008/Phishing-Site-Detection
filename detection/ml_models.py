import pickle
import cv2
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

## Load the URL model and vectorizer
with open('C:/Users/ASUS/OneDrive/Desktop/PhishingSiteDetection/phishing_detection/detection/models/url_model.pkl', 'rb') as file:
    url_model = pickle.load(file)

with open('C:/Users/ASUS/OneDrive/Desktop/PhishingSiteDetection/phishing_detection/detection/models/url_vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

## Load the image model
# try:
#     with open('models/image_model.pkl', 'rb') as file:
#         image_model = pickle.load(file)
# except Exception as e:
#     print(f"Error loading image model: {e}")
#     image_model = None  # Handle the case where loading fails

def predict_phishing(url_or_image_path):
    if is_url(url_or_image_path):
        return predict_url(url_or_image_path)
    # elif is_image(url_or_image_path):
    #     return predict_image(url_or_image_path)
    else:
        return 'Unknown input type'

def predict_url(url):
    features = vectorizer.transform([url])
    prediction = url_model.predict(features)
    return 'Phishing' if prediction[0] else 'Legitimate'

# def preprocess_image(img_path):
#     img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
#     img = cv2.resize(img, (128, 128))
#     return img.flatten().reshape(1, -1)

# def predict_image(img_path):
#     if image_model is None:
#         return 'Image model not available'

#     img = preprocess_image(img_path)
#     prediction = image_model.predict(img)
#     return 'Phishing' if prediction[0] else 'Legitimate'

def is_url(input):
    # Logic to determine if input is a URL (e.g., using regex or domain knowledge)
    return True  # Placeholder logic

# def is_image(input):
#     # Logic to determine if input is an image (e.g., checking file extension)
#     return True  # Placeholder logic
