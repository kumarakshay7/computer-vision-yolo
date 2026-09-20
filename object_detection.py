from ultralytics import YOLO
import cv2
import os


def detect_objects(input_folder="images_input", output_folder="images_output"):
    """Run YOLO object detection on images in an input folder."""
    model = YOLO("yolov8n.pt")
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith((".jpg", ".png", ".jpeg")):
            image_path = os.path.join(input_folder, file_name)
            image = cv2.imread(image_path)

            if image is not None:
                results = model(image)
                output_path = os.path.join(output_folder, file_name)
                cv2.imwrite(output_path, results[0].plot())
                print(f"Processed: {file_name}")

    print("All images processed.")


if __name__ == "__main__":
    detect_objects()
