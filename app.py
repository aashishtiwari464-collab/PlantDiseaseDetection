import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import json
from PIL import Image
import gdown
import os

# NEW IMPORT: This is required for the new advisory section
from disease_info import DISEASE_INFO

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
        .footer {
            text-align: center;
            padding: 10px;
            color: grey;
            font-size: 0.9rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- 2. MODEL AND LABELS LOADING ---

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
def predict(img):
    """
    Takes a PIL image and returns the prediction label and confidence.
    """
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

    # A clear call-to-action button to trigger the diagnosis
    if st.button('Diagnose My Plant', use_container_width=True, type="primary"):
        # A spinner provides feedback during the prediction process
        with st.spinner('The AI is analyzing the leaf...'):
            label, confidence = predict(img)

        # Clean the raw label for a human-readable display
        display_label = label.replace('___', ' ').replace('_', ' ').title()

        # Display the result in our custom-styled card
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="diagnosis-header">{display_label}</div>', unsafe_allow_html=True)
        st.progress(confidence)
        st.markdown(f'<div class="confidence-text">Confidence: <strong>{confidence*100:.2f}%</strong></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # FULLY INTEGRATED ADVISORY SECTION
        st.markdown("---")
        info = DISEASE_INFO.get(label) # 'label' is the raw output from the model

        if info:
            tab1, tab2, tab3 = st.tabs(["📋 Description", "💊 Treatment", "🛡️ Prevention"])

            with tab1:
                st.subheader("What is this disease?")
                st.write(info['description'])
                st.subheader("Common Symptoms")
                for symptom in info['symptoms']:
                    st.markdown(f"- {symptom}")

            with tab2:
                st.subheader("Organic Solutions")
                st.success(info['treatment']['organic'])
                st.subheader("Chemical Solutions")
                st.warning(info['treatment']['chemical'])
                
            with tab3:
                st.subheader("How to Prevent This")
                st.info(info['prevention'])

# --- 5. FOOTER ---
st.markdown("---")
st.markdown('<div class="footer">Developed by Mr. Aashish Tiwari</div>', unsafe_allow_html=True)
