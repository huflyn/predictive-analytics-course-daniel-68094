# 1. Export labels from labelstudio using the "YOLO" export format
# 1a. Run 03a-convert-labelstudio-labels.py to convert label-studio class ids to COCO class ids
# 2. Separate the image and label files into train and validation sets
# 2a. Create train.txt/val.txt that contain a list of images, paths are relative from file position
# 3. Create a dataset.yaml with a similar format as https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/coco.yaml
'''e.g.:

path: ./custom
train: train.txt
val: val.txt

names:
  0: person
  1: bicycle
  2: car
  3: motorcycle
  4: airplane
  5: bus
  6: train
  7: truck
  8: boat
  9: traffic light
  10: fire hydrant
'''
# 4. Run this script and check the error message for the path where ultralytics expects the dataset directory to be located
#    (The logic behind this seems rather complex and system-dependent, so this is the most reliable option)

from ultralytics import YOLO
import torch

# Check if MPS is available and set the device
if not torch.backends.mps.is_available():
    if not torch.backends.mps.is_built():
        print("MPS not available because the current PyTorch install was not built with MPS enabled.")
    else:
        print("MPS not available because the current MacOS version is not 12.3+ and/or you do not have an MPS-enabled device on this machine.")
    device = torch.device("cpu")
else:
    device = torch.device("mps")
    print(f"Using device: {device}")

# Load a model and move it to the device
model = YOLO("yolov8n.pt").to(device)  # load a pretrained model and move it to the device

# Define a function to move data to the device
def move_data_to_device(data, device):
    if isinstance(data, torch.Tensor):
        return data.to(device)
    elif isinstance(data, dict):
        return {key: move_data_to_device(value, device) for key, value in data.items()}
    elif isinstance(data, list):
        return [move_data_to_device(value, device) for value in data]
    else:
        return data

# Train the model
results = model.train(data="trainingdata/dataset-sample.yaml", epochs=100, imgsz=640, device=device)
