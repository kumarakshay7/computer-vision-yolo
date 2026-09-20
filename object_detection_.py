from ultralytics import YOLO
import cv2
import os

def detect_objects(input_folder, output_folder):
    model = YOLO('yolov8n.pt')  # Load YOLO model
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith(('.jpg', '.png', '.jpeg')):
            img = cv2.imread(os.path.join(input_folder, file_name))
            if img is not None:
                results = model(img)
                cv2.imwrite(os.path.join(output_folder, file_name), results[0].plot())
                print(f"Processed: {file_name}")

    print("All images processed.")

if __name__ == "__main__":
    detect_objects("images_input", "images_output")
