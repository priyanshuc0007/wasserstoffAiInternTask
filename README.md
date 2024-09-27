# Image Segmentation and Object Processing Pipeline

## Project Overview

This project implements a comprehensive pipeline for **image segmentation**, **object extraction**, **identification**, **text/data extraction**, and **summarization** of object attributes. The goal is to process an image, identify objects, extract textual data from these objects, summarize their attributes, and generate a final annotated report. The key components used include a TensorFlow-based model for image segmentation, Tesseract OCR for text extraction, and the Salesforce BLIP Replicate API for image summarization.

## Key Features

- **Image Segmentation:** Utilizes a pre-trained Faster R-CNN model (trained on the COCO2017 dataset) to segment and identify objects in an image.
- **Object Extraction:** Segmented objects are cropped and saved as separate images.
- **Text/Data Extraction:** Implements Tesseract OCR with Otsu's preprocessing to extract text from the segmented objects. (Each image has a dedicated button for individual text extraction.)
- **Image Summarization:** Employs the Salesforce BLIP model via Replicate API to generate descriptions or captions for each object image. (Each image also has a separate button for individual summarization.)
- **Final Report Generation:** Generates a report containing the original image, segmented objects, and a table summarizing attributes such as descriptions, extracted text, and metadata for each object.

## Setup Instructions

### 1. Install Dependencies

This project requires the following dependencies:

- **TensorFlow** for model inference.
- **Tesseract-OCR** for text extraction.
- **huggingface** for image summarization.
- **Streamlit** for building the web interface.
- **PIL**, **OpenCV**, and **Matplotlib** for image processing and visualization.

To install the dependencies, run:

```bash
pip install -r requirements.txt
```

### 2. Install Tesseract OCR

Tesseract is used for extracting text from segmented images. Install Tesseract on your machine:

- **Windows:** Download and install from [here](https://github.com/UB-Mannheim/tesseract/wiki).
- **macOS:** Install via Homebrew:
  ```bash
  brew install tesseract
  ```
- **Linux:** Install via apt:
  ```bash
  sudo apt-get install tesseract-ocr
  ```

### 3. Add Tesseract-OCR to Your PATH

Make sure Tesseract is accessible from your command line by adding it to your system's PATH.

### 4. Set Up hugging_face API for Image Summarization

Create an account on [https://huggingface.com) and obtain your API key. Then, export the API key to your environment:

```bash
export hf_token=<your_api_token>
```

### 5. Set Up TensorFlow Model

The image segmentation model is pre-trained on the COCO2017 dataset and will be automatically downloaded when running the project.

### 6. Run the Application

You can run the project using Streamlit. Navigate to the project directory and run:

```bash
streamlit run app.py
```

## Usage Guidelines

### Step 1: Image Segmentation

- Upload an image through the Streamlit interface.
- The Faster R-CNN model segments the objects in the image.
- Each segmented object is identified using the Faster R-CNN Model labels.
- Segmented objects are visually displayed and labeled, with each extracted and stored with a unique ID.

### Step 2: Text Extraction from Objects

- Each displayed segmented object can be processed for "Text Extraction" by clicking the button under each image. 
- Tesseract OCR extracts text from the segmented object images.
- Advanced preprocessing (Otsu’s thresholding) is applied to enhance text extraction accuracy.

### Step 3: Object Summarization

- Each displayed segmented object can be summarized by clicking the button under each image. 
- Each segmented object image is captioned using the Salesforce Blip Model (Replicate API).
- The model generates a caption or description for each object image.

### Step 4: Report Generation

- The application generates a final report that contains:
  - The original image.
  - Annotated segmented objects.
  - A table summarizing extracted text, descriptions, and unique IDs for each object.

## File Structure

```bash
├── data
│   ├── input_images
│   └── output
│       ├── report
│       ├── segmented_objects
│       ├── summarization
│       └── text_extraction
├── models
│   ├── segmentation_model.py
│   ├── summarization_model.py
│   ├── test.py
│   └── text_extraction_model.py
├── utils
│   ├── data_mapping.py
│   ├── postprocessing.py
│   └── preprocessing.py
├── coco_labels.txt
├── presentation.pptx
├── README.md
├── requirements.txt
└── app.py
```
