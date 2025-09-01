import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="🎨 Pencil Sketch App", layout="centered")
st.title("🖋️ Realistic Pencil Sketch Generator")
st.markdown("Upload an image and use the slider to control sketch intensity!")

# Upload the image
uploaded_file = st.file_uploader("📤 Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        # Load and convert the image
        image = Image.open(uploaded_file).convert("RGB")
        img = np.array(image)

        # Show original image
        st.subheader("Original")
        st.image(img, use_column_width=True)

        # Blur strength slider
        blur_strength = st.slider("🌀 Adjust Blur Strength", min_value=5, max_value=75, value=25, step=2)

        # Step 1: Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        # Step 2: Invert the grayscale image
        inverted = 255 - gray

        # Step 3: Apply Gaussian Blur
        blur_value = blur_strength | 1  # make sure it's odd
        blurred = cv2.GaussianBlur(inverted, (blur_value, blur_value), sigmaX=0, sigmaY=0)

        # Step 4: Color dodge blend (for sketch effect)
        sketch = cv2.divide(gray, 255 - blurred, scale=256.0)

        # Step 5: Optional - enhance contrast for more realistic shading
        sketch = cv2.equalizeHist(sketch)

        # Show the result
        st.subheader("Pencil Sketch")
        st.image(sketch, use_column_width=True, channels="GRAY", clamp=True)

        # Download sketch button
        result_img = Image.fromarray(sketch)
        st.download_button("📥 Download Sketch", result_img.tobytes(), "pencil_sketch.png", mime="image/png")

    except Exception as e:
        st.error(f"⚠️ Error processing image: {e}")

else:
    st.info("Please upload an image to get started.")
