import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import json
from PIL import Image, UnidentifiedImageError
import gdown
import os

from Diseases_info import DISEASE_INFO

# ---------------- CONFIG ----------------
st.set_page_config(page_title="AI Plant Doctor", page_icon="🌿", layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>
.stApp { background: linear-gradient(135deg, #eef2f3, #dfe9f3); }
.header { text-align:center; padding:20px; }
.header h1 { font-size:2.5rem; color:#1d3557; }
.header p { color:#6c757d; }
.card {
    background: rgba(255,255,255,0.92);
    border-radius:16px;
    padding:20px;
    box-shadow:0 8px 25px rgba(0,0,0,0.1);
    margin-bottom:20px;
}
.result {
    text-align:center;
    font-size:1.5rem;
    color:#e63946;
    font-weight:bold;
}
.footer {
    text-align:center;
    color:gray;
    padding:20px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="header">
<h1>🌿 AI Plant Doctor</h1>
<p>Smart disease detection with instant advisory</p>
</div>
""", unsafe_allow_html=True)

# ---------------- MODEL ----------------
@st.cache_resource
def load_model_file():
    MODEL_ID = "1ozwUc7E-CO88WAQaiKXc8eG6G533sVpB"
    PATH = "model.keras"

    if not os.path.exists(PATH):
        with st.spinner("Downloading AI model..."):
            gdown.download(f"https://drive.google.com/uc?id={MODEL_ID}", PATH)

    return load_model(PATH)

@st.cache_data
def load_labels():
    with open("class_indices.json") as f:
        data = json.load(f)
    return {v: k for k, v in data.items()}

model = load_model_file()
labels = load_labels()

# ---------------- PREDICT ----------------
def predict(img):
    img = img.resize((128,128))
    arr = image.img_to_array(img)/255.0
    arr = np.expand_dims(arr,0)

    pred = model.predict(arr)[0]
    idx = np.argmax(pred)
    conf = float(np.max(pred))

    return labels[idx], conf

# ---------------- SAFE HELPERS ----------------
def show_list_or_text(data):
    if isinstance(data, list):
        for item in data:
            st.markdown(f"- {item}")
    elif isinstance(data, str):
        st.markdown(f"- {data}")
    else:
        st.write("No data available.")

def show_treatment(treatment):
    st.subheader("🌿 Organic")
    if isinstance(treatment, dict):
        st.info(treatment.get("organic", "N/A"))
    elif isinstance(treatment, str):
        st.info(treatment)
    else:
        st.info("N/A")

    st.subheader("🧪 Chemical")
    if isinstance(treatment, dict):
        st.warning(treatment.get("chemical", "N/A"))
    else:
        st.warning("No chemical treatment needed.")

def show_prevention(prevention):
    if isinstance(prevention, str):
        st.info(prevention)
    else:
        st.write("No prevention info available.")

# ---------------- LAYOUT ----------------
col1, col2 = st.columns(2)

# -------- LEFT --------
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📤 Upload Leaf Image")
    file = st.file_uploader("", type=["jpg","jpeg","png"])
    st.markdown('</div>', unsafe_allow_html=True)

    if file:
        if file.size > 5 * 1024 * 1024:
            st.error("❌ File too large (max 5MB)")
            st.stop()

        try:
            img = Image.open(file).convert("RGB")
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.image(img, caption="Uploaded Image", use_column_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        except UnidentifiedImageError:
            st.error("❌ Invalid image file")
            st.stop()

# -------- RIGHT --------
with col2:
    if file:
        if st.button("🔍 Diagnose", use_container_width=True):

            with st.spinner("Analyzing plant..."):
                label, conf = predict(img)

            if conf < 0.6:
                st.warning("⚠️ Low confidence. Try clearer image.")
                st.stop()

            name = label.replace("___"," ").replace("_"," ").title()

            st.markdown('<div class="card">', unsafe_allow_html=True)

            st.markdown(f"<div class='result'>{name}</div>", unsafe_allow_html=True)
            st.metric("Confidence", f"{conf*100:.2f}%")
            st.progress(conf)

            if "healthy" in label.lower():
                st.success("🟢 Plant is Healthy")
            else:
                st.error("🔴 Disease Detected")

            st.markdown('</div>', unsafe_allow_html=True)

            # -------- INFO --------
            info = DISEASE_INFO.get(label)

            if not info:
                st.error("No data available for this disease.")
                st.stop()

            tab1, tab2, tab3 = st.tabs(["📋 Info","💊 Treatment","🛡 Prevention"])

            with tab1:
                st.write(info.get("description", "No description available."))
                st.subheader("Symptoms")
                show_list_or_text(info.get("symptoms"))

            with tab2:
                show_treatment(info.get("treatment"))

            with tab3:
                show_prevention(info.get("prevention"))

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
🌿 Built by Aashish Tiwari | AI Plant Doctor
</div>
""", unsafe_allow_html=True)
