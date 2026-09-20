# YOLO Computer Vision: Object Detection & Segmentation

A Python-based computer vision project using **Ultralytics YOLO** and **OpenCV** for image-based object detection and segmentation workflows.

## Project Overview

This project demonstrates a practical computer vision pipeline that reads images from an input folder, runs YOLO inference, and saves annotated results to an output folder.

The object detection workflow has been tested locally and successfully processed sample images, detecting classes such as people, cars, dogs, and cows.

## Features

### Object Detection
- Reads `.jpg`, `.jpeg`, and `.png` images from `images_input/`
- Runs YOLO inference on each image
- Draws detected bounding boxes and labels
- Saves annotated images to `images_output/`
- Prints processing information in the terminal

### Image Segmentation
- Includes a YOLO segmentation training workflow in `object_segmentation.py`
- Uses the Ultralytics YOLO segmentation framework
- Accepts a user-supplied YOLO dataset YAML file

> **Current status:** Object detection is working with the included script. Custom segmentation training requires a valid YOLO dataset configuration file such as `data.yaml`.

## Tech Stack

- **Python**
- **Ultralytics YOLO**
- **OpenCV**
- **NumPy**
- **Computer Vision**

## Project Structure

```text
computer-vision-yolo/
│
├── images_input/
│   ├── image2.jpg
│   ├── image3.jpg
│   └── ...
│
├── object_detection.py
├── object_segmentation.py
├── requirements.txt
├── .gitignore
└── README.md
```

Generated folders such as `runs/`, `images_output/`, Python virtual environments, and large model weight files are excluded from Git using `.gitignore`.

## How It Works

```text
Input Image
     │
     ▼
OpenCV Image Loading
     │
     ▼
YOLO Inference
     │
     ▼
Object Detection
     │
     ▼
Bounding Boxes + Labels
     │
     ▼
Annotated Output Image
```

## Installation

Clone the repository:

```bash
git clone https://github.com/kumarakshay7/computer-vision-yolo.git
cd computer-vision-yolo
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

For a cleaner setup, use a Python virtual environment.

## Run Object Detection

Place your test images inside:

```text
images_input/
```

Then run:

```bash
python object_detection.py
```

The script creates `images_output/` when needed and saves annotated images there.

## Example Detection Results

The current test run successfully processed multiple images:

| Image | Detected Objects |
|---|---|
| image6.jpg | 1 dog, 1 cow |
| image7.jpg | 1 person, 3 cars, 3 dogs |
| image8.jpg | 1 dog |
| img1.jpg | 1 dog |

These results demonstrate the end-to-end inference workflow from image input to annotated output.

## Segmentation

The repository includes:

```text
object_segmentation.py
```

For custom segmentation training, prepare a YOLO-compatible dataset with a configuration file similar to:

```yaml
path: /path/to/dataset
train: images/train
val: images/val

names:
  0: class_name
```

Then update `DATA_YAML` in `object_segmentation.py` and run:

```bash
python object_segmentation.py
```

Do not use the placeholder `path_to_your_data.yaml` as an actual dataset path.

## Applications

This computer vision workflow can be adapted for:

- Object monitoring
- Image analytics
- Automated inspection
- Retail and inventory analysis
- Traffic and vehicle detection
- Industrial computer vision

## Future Improvements

- Add a Streamlit web interface
- Add video and webcam inference
- Add confidence and class filters
- Add custom YOLO training datasets
- Add segmentation result examples
- Add precision, recall, mAP, and inference-time reporting
- Add automated deployment

## Author

**Akshay Kumar**

Data Analyst | Data Science | Computer Vision | AI & Analytics

GitHub: https://github.com/kumarakshay7
