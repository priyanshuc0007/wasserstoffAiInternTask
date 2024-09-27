# AI Pipeline for Image Segmentation and Object Analysis

This project is an AI-driven pipeline designed for image segmentation and object analysis. It leverages deep learning models to perform segmentation, text extraction, and summarization, providing a comprehensive tool for image analysis tasks.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Image Upload**: Upload images for analysis.
- **Segmentation**: Identify and segment objects within images using pretrained models.
- **Text Extraction**: Extract text from segmented images.
- **Summarization**: Generate descriptive summaries for segmented objects.
- **Final Report Generation**: Compile extracted data into a structured report.

## Installation
To run this project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/priyanshuc0007/wasserstoffAiInternTask.git

### 1. Install Dependencies

This project requires the following dependencies:

- **TensorFlow** for model inference.
- **Tesseract-OCR** for text extraction.
- **Replicate API** for image summarization.
- **Streamlit** for building the web-based interface.
- **PIL**, **OpenCV**, and **Matplotlib** for image processing and visualization.

To install the dependencies, run:

```bash
pip install -r requirements.txt
```

### 3. Install Tesseract OCR

Tesseract is used for extracting text from segmented images. Install Tesseract on your machine:

## File Structure

```bash
├── data
│    ├── input_images
│    └── output
│          ├── report
│          ├── segmented_objects
│          ├── summarization
│          └── text_extraction
├── models
│     ├── segmentation_model.py
│     ├── summarization_model.py
│     ├── test.py
│     └── text_extraction_model.py
├── utils
│     ├── data_mapping.py
│     ├── postprocessing.py
│     └── preprocessing.py
├── coco_labels.txt
├── presentation.pptx
├── README.md
├── requirements.txt
└── app.py

![Annotation 2024-04-30 113731](https://github.com/user-attachments/assets/7baff430-2c8c-494c-b699-218ae4d3fe8d)


   
   

   
