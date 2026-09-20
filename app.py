import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

st.set_page_config(
    page_title="YOLO Object Detection",
    page_icon="🎯",
    layout="centered",
)

st.title("🎯 YOLO Real-Time Object Detection")
st.write("Take a photo with your camera or upload an image to detect objects.")

@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")

model = load_model()

confidence = st.slider(
    "Detection confidence",
    min_value=0.10,
    max_value=1.00,
    value=0.40,
    step=0.05,
)

camera_image = st.camera_input("📷 Open Camera")

uploaded_image = st.file_uploader(
    "Or upload an image",
    type=["jpg", "jpeg", "png"],
)

image_file = camera_image if camera_image is not None else uploaded_image

if image_file is not None:
    image = Image.open(image_file).convert("RGB")
    image_array = np.array(image)

    results = model.predict(
        source=image_array,
        conf=confidence,
        verbose=False,
    )

    annotated_image = results[0].plot()

    st.subheader("Detection Result")
    st.image(annotated_image, channels="BGR", use_container_width=True)

    detections = results[0].boxes

    if detections is not None and len(detections) > 0:
        st.subheader("Detected Objects")

        counts = {}
        for cls_id in detections.cls.tolist():
            class_name = model.names[int(cls_id)]
            counts[class_name] = counts.get(class_name, 0) + 1

        for name, count in sorted(counts.items()):
            st.write(f"**{name}**: {count}")

        st.success(f"Detected {len(detections)} object(s).")
    else:
        st.warning("No objects detected. Try another image or lower the confidence threshold.")

st.divider()
st.caption("Powered by Ultralytics YOLO + OpenCV/Streamlit")
