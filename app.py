import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import json
from PIL import Image
import gdown
import os

from Diseases_info import DISEASE_INFO

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="AI Plant Doctor",
    page_icon="🌿",
    layout="centered"
)

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>
.stApp {
    background-color: #f4f6f9;
}

/* Hero Section */
.hero {
    text-align:center;
    padding:20px;
}
.hero h1 {
    font-size:2.5rem;
    color:#264653;
}
.hero p {
    color:#6c757d;
}

/* Cards */
.section-card {
    background:white;
    padding:20px;
    border-radius:15px;
    margin-bottom:20px;
    box-shadow:0 6px 15px rgba(0,0,0,0.08);
}

/* Result Styling */
.result-title {
    text-align:center;
    font-size:2rem;
    color:#E76F51;
    font-weight:bold;
}

.footer {
    text-align:center;
    padding:20px;
    color:gray;
}
</style>
""", unsafe_allow_html=True)

# ------------------ HERO ------------------
st.markdown("""
<div class="hero">
    <h1>🌿 AI Plant Doctor</h1>
    <p>Instant disease detection with smart treatment guidance</p>
</div>
""", unsafe_allow_html=True)

# ------------------ MODEL LOAD ------------------
@st.cache_resource
def download_and_load_model():
    MODEL_ID = "1ozwUc7E-CO88WAQaiKXc8eG6G533sVpB"
    MODEL_PATH = "final_model.keras"

    if not os.path.exists(MODEL_PATH):
        with st.spinner("Downloading AI model..."):
            gdown.download(f"https://drive.google.com/uc?id={MODEL_ID}", MODEL_PATH, quiet=False)

    return load_model(MODEL_PATH)

@st.cache_data
def load_labels():
    with open("class_indices.json", "r") as f:
        class_indices = json.load(f)
    return {v: k for k, v in class_indices.items()}

model = download_and_load_model()
labels = load_labels()

# ------------------ PREDICTION ------------------
def predict(img):
    img = img.resize((128, 128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)[0]
    class_index = np.argmax(prediction)
    confidence = float(np.max(prediction))

    return labels[class_index], confidence

# ------------------ LANGUAGE ------------------
language = st.selectbox("🌐 Select Language", ["English", "Hindi"])

# ------------------ UPLOAD SECTION ------------------
st.markdown('<div class="section-card">', unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "📤 Upload a plant leaf image",
    type=["jpg", "jpeg", "png"]
)

st.markdown('</div>', unsafe_allow_html=True)

# ------------------ IMAGE PREVIEW ------------------
if uploaded_file:
    img = Image.open(uploaded_file).convert("RGB")

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.image(img, caption="📷 Uploaded Leaf Image", use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # ------------------ BUTTON ------------------
    if st.button("🔍 Diagnose Plant", use_container_width=True):

        with st.spinner("Analyzing..."):
            label, confidence = predict(img)

        display_label = label.replace('___', ' ').replace('_', ' ').title()

        # Confidence threshold
        if confidence < 0.6:
            st.warning("⚠️ Low confidence. Try a clearer image.")
            st.stop()

        # ------------------ RESULT ------------------
        st.markdown('<div class="section-card">', unsafe_allow_html=True)

        st.markdown(f"<div class='result-title'>{display_label}</div>", unsafe_allow_html=True)

        st.metric("Confidence", f"{confidence*100:.2f}%")
        st.progress(confidence)

        if "healthy" in label.lower():
            st.success("🟢 Plant is Healthy")
        else:
            st.error("🔴 Disease Detected")

        st.markdown('</div>', unsafe_allow_html=True)

        # ------------------ DISCLAIMER ------------------
        st.warning("This is an AI-based prediction. Consult an expert for confirmation.")

        # ------------------ DISEASE INFO ------------------
        info = DISEASE_INFO.get(label)

        if label.endswith("___healthy"):
            if info and info.get("maintenance_tips"):
                st.markdown('<div class="section-card">', unsafe_allow_html=True)
                st.subheader("🌱 Maintenance Tips")
                for tip in info["maintenance_tips"]:
                    st.markdown(f"- {tip}")
                st.markdown('</div>', unsafe_allow_html=True)

        elif info:
            tab1, tab2, tab3 = st.tabs(["📋 Symptoms", "💊 Treatment", "🛡 Prevention"])

            with tab1:
                st.write(info.get("description", "No info"))
                for s in info.get("symptoms", []):
                    st.markdown(f"- {s}")

            with tab2:
                st.markdown("### 🌿 Organic")
                st.info(info.get("treatment", {}).get("organic", "N/A"))

                st.markdown("### 🧪 Chemical")
                st.warning(info.get("treatment", {}).get("chemical", "N/A"))

            with tab3:
                st.info(info.get("prevention", "No info"))

# ------------------ HOW IT WORKS ------------------
st.markdown('<div class="section-card">', unsafe_allow_html=True)

st.subheader("ℹ️ How it works")
st.markdown("""
1. Upload a clear leaf image  
2. Click Diagnose  
3. Get instant AI results  
""")

st.markdown('</div>', unsafe_allow_html=True)

# ------------------ FOOTER ------------------
st.markdown("""
<div class="footer">
    🌿 Built by Aashish Tiwari | Agri AI Solutions
</div>
""", unsafe_allow_html=True)            text-align: center;
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

        # --- 5. REVISED ADVISORY AND WARNINGS SECTION ---
        st.markdown("---")
        
        # Display a prominent, general disclaimer for ALL diagnoses
        st.warning(
            "**Disclaimer:** This AI diagnosis is for informational purposes only and is not a substitute for professional advice. "
            "Visual symptoms can be misleading. For a definitive diagnosis and treatment plan, consult a local agricultural extension service or certified agronomist."
        )

        info = DISEASE_INFO.get(label)

        # CRITICAL BUG FIX: Check if the plant is healthy before trying to show disease info
        if label.endswith("___healthy"):
            st.balloons()
            st.success(f"**Great news! The model indicates your {display_label.replace(' Healthy', '')} plant is healthy.**")
            if info and info.get('maintenance_tips'):
                st.subheader("Tips for Maintaining Health")
                for tip in info['maintenance_tips']:
                    st.markdown(f"- {tip}")
        elif info:
            # This block now only runs for non-healthy diagnoses
            st.subheader(f"Advisory for {display_label}")
            tab1, tab2, tab3 = st.tabs(["📋 Description & Symptoms", "💊 Treatment Options", "🛡️ Prevention Strategy"])

            with tab1:
                st.write(info.get('description', 'No description available.'))
                st.subheader("Common Symptoms")
                symptoms = info.get('symptoms', [])
                if symptoms:
                    for symptom in symptoms:
                        st.markdown(f"- {symptom}")
                else:
                    st.write("No symptoms listed.")

            with tab2:
                st.subheader("Organic Solutions")
                st.info(info.get('treatment', {}).get('organic', 'No organic treatments listed.'))
                
                st.subheader("Chemical Solutions")
                # SPECIFIC AND DETAILED CHEMICAL USE WARNING
                st.error(
                    "**⚠️ CRITICAL SAFETY WARNING ⚠️**\n\n"
                    "Chemical treatments should be a **last resort** within an Integrated Pest Management (IPM) strategy. "
                    "If you must use chemicals:\n\n"
                    "1.  **Verify the Diagnosis:** Get professional confirmation before you spray.\n"
                    "2.  **Follow Local Laws:** Chemical use is highly regulated. Check regulations for Madhya Pradesh.\n"
                    "3.  **Read the Label:** The label is the law. Follow all instructions for mixing, application, and Personal Protective Equipment (PPE).\n"
                    "4.  **Protect Pollinators:** Do not spray when bees and other beneficial insects are active."
                )
                st.warning(info.get('treatment', {}).get('chemical', 'No chemical treatments listed.'))
                
            with tab3:
                st.subheader("How to Prevent This")
                st.info(info.get('prevention', 'No prevention information available.'))
        else:
            st.error("Could not retrieve advisory information for this diagnosis.")

# --- 6. FOOTER AND FEEDBACK ---
st.markdown("---")
st.subheader("Was this diagnosis helpful?")
feedback_cols = st.columns(2)
with feedback_cols[0]:
    if st.button("👍 Yes, it was helpful", use_container_width=True):
        st.success("Thank you for your feedback!")
with feedback_cols[1]:
    if st.button("👎 No, this was incorrect", use_container_width=True):
        st.warning("We appreciate your feedback. This helps us improve our AI.")

st.markdown('<div class="footer">Developed by Mr. Aashish Tiwari</div>', unsafe_allow_html=True)
