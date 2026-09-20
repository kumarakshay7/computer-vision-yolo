from ultralytics import YOLO


def train_segmentation(data_yaml, epochs=5, image_size=640):
    """Train a YOLO segmentation model using a YOLO dataset YAML file."""
    model = YOLO("yolov8n-seg.pt")
    model.train(data=data_yaml, epochs=epochs, imgsz=image_size)


if __name__ == "__main__":
    # Replace this with the path to your YOLO segmentation dataset YAML file.
    DATA_YAML = "path_to_your_data.yaml"
    train_segmentation(DATA_YAML)
