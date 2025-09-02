
import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import json
from PIL import Image
import gdown
import os

# ==============================
# Download Model from Google Drive
# ==============================
MODEL_ID = "1ozwUc7E-CO88WAQaiKXc8eG6G533sVpB"
MODEL_URL = f"https://drive.google.com/uc?id={MODEL_ID}"

if not os.path.exists("final_model.keras"):
    st.info("Downloading model from Google Drive... please wait ⏳")
    gdown.download(MODEL_URL, "final_model.keras", quiet=False)

# ==============================
# Load Model & Labels
# ==============================
model = load_model("final_model.keras")

with open("class_indices.json", "r") as f:
    class_indices = json.load(f)

labels = {v: k for k, v in class_indices.items()}

# ==============================
# Prediction Function
# ==============================
def predict(img):
    img = img.resize((128, 128))  # change if your training size is different
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)[0]
    class_index = np.argmax(prediction)
    confidence = float(np.max(prediction))
    return labels[class_index], confidence

# ==============================
# Streamlit UI
# ==============================
st.title("🌱 Plant Disease Detection")
st.write("Upload a potato or tomato leaf image and get prediction.")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded Image", use_column_width=True)
    label, confidence = predict(img)
    st.success(f"Prediction: {label} ({confidence:.2f} confidence)")
