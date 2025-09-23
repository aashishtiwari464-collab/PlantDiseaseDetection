import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import json
from PIL import Image
import gdown
import os

# --- 1. SETUP AND CONFIGURATION ---

# Set page configuration - This MUST be the first Streamlit command
st.set_page_config(
    page_title="Plant Disease Diagnosis",
    page_icon="🌿",
    layout="centered"
)

# Inject custom CSS for a professional look
st.markdown("""
    <style>
        .stApp {
            background-color: #F0F2F6;
        }
        .result-card {
            background-color: #FFFFFF;
            border-radius: 12px;
            padding: 25px;
            margin-top: 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        h1 {
            color: #264653;
            text-align: center;
        }
        .stMarkdown p {
            text-align: center;
            color: #2A9D8F;
        }
        .diagnosis-header {
            font-size: 2.2rem;
            font-weight: bold;
            color: #E76F51;
            text-align: center;
        }
        .confidence-text {
            text-align: center;
            font-size: 1.1rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- 2. MODEL AND LABELS LOADING ---
# IMPROVEMENT: Caching the model and labels for better performance.
# This prevents reloading the model every time the script reruns.

@st.cache_resource
def download_and_load_model():
    """
    Downloads the model from Google Drive if it doesn't exist,
    then loads and returns the Keras model.
    """
    MODEL_ID = "1ozwUc7E-CO88WAQaiKXc8eG6G533sVpB"
    MODEL_PATH = "final_model.keras"
    
    if not os.path.exists(MODEL_PATH):
        with st.spinner("Downloading the AI model... this may take a moment ⏳"):
            gdown.download(f"https://drive.google.com/uc?id={MODEL_ID}", MODEL_PATH, quiet=False)
    
    model = load_model(MODEL_PATH)
    return model

@st.cache_data
def load_labels():
    """
    Loads and returns the class labels from the JSON file.
    """
    with open("class_indices.json", "r") as f:
        class_indices = json.load(f)
    labels = {v: k for k, v in class_indices.items()}
    return labels

# Load the resources
model = download_and_load_model()
labels = load_labels()

# --- 3. PREDICTION LOGIC ---
# Your original prediction function, unchanged.
def predict(img):
    img = img.resize((128, 128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)[0]
    class_index = np.argmax(prediction)
    confidence = float(np.max(prediction))
    return labels[class_index], confidence

# --- 4. USER INTERFACE ---
st.title("Plant Disease Diagnosis")
st.markdown("<p>Your digital assistant for a healthier harvest.</p>", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Upload a clear image of a plant leaf",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is None:
    st.info("Please upload an image to get started.")
else:
    # Display the image in a controlled column
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        img = Image.open(uploaded_file).convert("RGB")
        st.image(img, caption='Your Uploaded Leaf', use_column_width=True)

    # IMPROVEMENT: A clear call-to-action button instead of auto-predicting.
    if st.button('Diagnose My Plant', use_container_width=True, type="primary"):
        # IMPROVEMENT: A spinner provides feedback during the prediction process.
        with st.spinner('The AI is analyzing the leaf...'):
            label, confidence = predict(img)

        # IMPROVEMENT: Cleaning the raw label for a human-readable display.
        display_label = label.replace('___', ' ').replace('_', ' ').title()

        # Display the result in our custom-styled card
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="diagnosis-header">{display_label}</div>', unsafe_allow_html=True)
        st.progress(confidence)
        st.markdown(f'<div class="confidence-text">Confidence: <strong>{confidence*100:.2f}%</strong></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
