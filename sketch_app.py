import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="🎨 Pencil Sketch App", layout="centered")
st.title("🖋️ Realistic Pencil Sketch Generator")
st.markdown("Upload an image to get a soft, hand-drawn pencil sketch.")

uploaded_file = st.file_uploader("📤 Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        # Load image
        image = Image.open(uploaded_file).convert("RGB")
        img = np.array(image)

        # Show original
        st.subheader("Original")
        st.image(img, use_column_width=True)

        # Grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        # Invert
        inverted = 255 - gray

        # Bilateral filter instead of heavy Gaussian blur for more realism
        smooth = cv2.bilateralFilter(inverted, d=9, sigmaColor=75, sigmaSpace=75)

        # Dodge blend
        def dodge_blend(front, back):
            result = cv2.divide(front, 255 - back, scale=256)
            return np.clip(result, 0, 255)

        sketch = dodge_blend(gray, smooth).astype(np.uint8)

        # Optional: Apply a very light Gaussian blur for realism
        sketch = cv2.GaussianBlur(sketch, (3, 3), 0)

        st.subheader("Pencil Sketch")
        st.image(sketch, use_column_width=True, clamp=True, channels="GRAY")

        result_img = Image.fromarray(sketch)
        st.download_button("📥 Download Sketch", result_img.tobytes(), "pencil_sketch.png", mime="image/png")

    except Exception as e:
        st.error(f"⚠️ Error: {e}")
else:
    st.info("Please upload an image to begin.")
