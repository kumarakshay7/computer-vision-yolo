from ultralytics import YOLO

def train_model():
    model = YOLO("yolov8n.pt")  # Load YOLO pre-trained model
    data = ("D:\CV_training\cv\images_input")
    model.train(data="path_to_your_data.yaml", epochs=5, imgsz=640)

if __name__ == "__main__":
    train_model()
