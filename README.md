# KbacCV

**KbacCV** is a Python library for analyzing and processing images and videos. It allows you to load a dataset of images and compare them with other frames or video sources to detect similar objects. The library supports both image and video files and provides basic drawing functionality for detected objects.

## Features

- Load and process both images and videos.
- Compare frames against a dataset of reference images.
- Draw bounding boxes and labels on detected objects.
- Adjustable similarity threshold for detection.

## Installation

You can install this package using pip:


pip install kbaccv
Usage
Here’s a quick example of how to use the KbacCV library.

1. Load a dataset of images:
2. 
from kbaccv import KbacCV

# Initialize the KbacCV object
kbac = KbacCV(similarity_threshold=0.7)

# Set the dataset (list of image paths)
dataset_paths = ["path_to_image1.png", "path_to_image2.jpg"]
kbac.set_dataset(dataset_paths)
2. Process an image:

# Load and process an image
image_path = "path_to_image.jpg"
processed_image = kbac.process(image_path)

# The processed_image now contains the objects with bounding boxes
3. Process a video:

# Load and process a video
video_path = "path_to_video.mp4"
processed_frames = kbac.process(video_path)

# processed_frames will contain the first 100 frames with detected objects
4. Draw bounding boxes and labels:
The library automatically draws bounding boxes around detected objects and adds a label. The bounding boxes are red by default.

Requirements
This library depends on the following packages:

Pillow
imageio
numpy
These will be installed automatically when you install the library via pip.
