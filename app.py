import streamlit as st
import tensorflow as tf
import numpy as np
import cv2

# Load the trained model
model = tf.keras.models.load_model('models/happysadmodel.h5')

# Streamlit UI
st.title("Happy or Sad Classifier")
st.write("Upload an image to classify whether it represents a 'Happy' or 'Sad' emotion.")

# Upload an image
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load the image
    file_bytes = np.frombuffer(uploaded_file.read(), np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Display the uploaded image
    st.image(img, caption="Uploaded Image", channels="BGR")

    # Preprocess the image
    resized_img = tf.image.resize(img, (256, 256))
    resized_img = resized_img.numpy() / 255.0
    reshaped_img = np.expand_dims(resized_img, axis=0)

    # Make prediction
    prediction = model.predict(reshaped_img)
    label = "Sad" if prediction >= 0.99 else "Happy"

    # Display the result
    st.subheader(f"Prediction: {label}")

