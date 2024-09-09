# Video-Subtitles-Detector
## Overview
This repository provides a set of tools for detecting and highlighting subtitles in video frames. The project leverages OpenCV for image processing to detect text areas in video frames by drawing bounding boxes around them and save the results. The code performs various preprocessing steps on each frame and segments subtitles using morphological operations.

## Features
* Frame Extraction: Extracts frames from a video file and saves them in different formats.
* Preprocessing: Converts frames to grayscale, applies Gaussian blur, and thresholding.
* Subtitle Segmentation: Detects and highlights subtitle areas using different morphological techniques.
  * Draw red bounding boxes around each line of subtitles.
  * Draw green bounding boxes around each word within the subtitles.
  * Process and apply bounding boxes to all subtitles in the video.
* Video Reconstruction: Compiles segmented frames into a new video file.
## Installation
Ensure you have Python installed along with the required libraries. You can install the necessary libraries using pip:

```bash
    pip install numpy opencv-python matplotlib
```
## Usage
1- Place your video file in the main directory if you will use jupyter or in src file if you will run python files .

2- Modify the base_directory variable to specify where you want to save the output frames and video.

3- Execute video_processing.py to process the video. It will:

* Create directories for storing frames and processed data.
* Extract frames from the video.
* Perform preprocessing on each frame.
* Apply text segmentation techniques.
* Save segmented frames and compile them into a new video.
```bash
    python video_processing.py
```


## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have improvements or bug fixes.

## Acknowledgments
OpenCV for image processing.
NumPy for numerical operations.
Matplotlib for visualization.
