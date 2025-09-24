import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load the trained model
model = load_model("model/cnn_model.keras")

# Title
st.title("🧠 Brain Tumor Detection")
st.write("Upload an MRI scan to detect the tumor type:")

# File uploader
uploaded_file = st.file_uploader("Choose an MRI image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded MRI", use_container_width=True)

    # Predict button
    if st.button("🔍 Predict"):
        # Preprocess the image
        img_resized = img.resize((128, 128))
        img_array = image.img_to_array(img_resized)
        img_array = np.expand_dims(img_array, axis=0) / 255.0

        # Make prediction
        preds = model.predict(img_array)
        class_idx = np.argmax(preds)
        confidence = preds[0][class_idx]

        class_labels = ["glioma", "meningioma", "pituitary", "notumor"]
        predicted_class = class_labels[class_idx]

        # Show results in nice boxes
        st.success(f"🧾 Prediction: **{predicted_class}**")
        st.info(f"📊 Confidence: **{confidence*100:.2f}%**")

        # Probability bar chart
        fig, ax = plt.subplots()
        ax.bar(class_labels, preds[0], color="skyblue")
        ax.set_ylabel("Probability")
        ax.set_title("Prediction Probabilities")
        st.pyplot(fig)
