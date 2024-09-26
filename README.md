Image Segmentation and Object Processing Pipeline
Project Overview
This project implements a comprehensive pipeline for image segmentation, object extraction, identification, text/data extraction, and summarization of object attributes. The goal is to process an image, identify objects, extract textual data from these objects, summarize their attributes, and generate a final annotated report. Key components include:

TensorFlow for image segmentation.
Tesseract OCR for text extraction.
Salesforce BLIP Replicate API for image summarization.
Key Features
Image Segmentation: Utilizes a pre-trained Faster R-CNN model (trained on the COCO2017 dataset) to segment and identify objects within an image.
Object Extraction: Segmented objects are cropped and saved as separate images for further processing.
Text/Data Extraction: Employs Tesseract OCR alongside Otsu's preprocessing to extract text from segmented objects. A button is provided below each image to run Tesseract and extract text individually.
Image Summarization: Utilizes the Salesforce BLIP model via the Replicate API to generate descriptions or captions for each object image, with a button for individual execution.
Final Report Generation: Compiles a report that includes the original image, segmented objects, and a summary table of attributes (e.g., descriptions, extracted text, and metadata) for each object.
Setup Instructions
1. Install Dependencies
This project requires the following dependencies:

TensorFlow for model inference.
Tesseract-OCR for text extraction.
Replicate API for image summarization.
Streamlit for building the web interface.
PIL, OpenCV, and Matplotlib for image processing and visualization.
To install the dependencies, run:

bash
Copy code
pip install -r requirements.txt
2. Install Tesseract OCR
Tesseract is used for extracting text from segmented images. Install Tesseract on your machine:

Windows: Download and install from here.

macOS: Install via Homebrew:

bash
Copy code
brew install tesseract
Linux: Install via apt:

bash
Copy code
sudo apt-get install tesseract-ocr
3. Add Tesseract-OCR to Your PATH
Make sure to add the Tesseract-OCR executable to your system's PATH.

4. Set Up Replicate API for Image Summarization
Create an account on Replicate and obtain your API key. Then, export the API key to your environment:

bash
Copy code
export REPLICATE_API_TOKEN=<your_replicate_api_token>
5. Set Up TensorFlow Model
The image segmentation model is pre-trained on the COCO2017 dataset and will be automatically downloaded when you run the project.

6. Run the Application
Navigate to the project directory and run the application using Streamlit:

bash
Copy code
streamlit run app.py
Usage Guidelines
Step 1: Image Segmentation
Upload an image through the Streamlit interface.
The Faster R-CNN model segments the objects in the image, which are visually displayed and labeled.
Each segmented object is extracted and stored with a unique ID.
Step 2: Text Extraction from Objects
For "Text Extraction," click the button under each displayed segmented object.
Tesseract OCR will extract text from the segmented object images.
Advanced preprocessing (Otsu’s thresholding) enhances text extraction accuracy.
Step 3: Object Summarization
To summarize an object, click the button under the displayed segmented object.
Each object image is captioned using the Salesforce BLIP Model via the Replicate API, generating a description for each object.
Step 4: Report Generation
The application generates a final report containing:
The original image.
Annotated segmented objects.
A summary table of extracted text, descriptions, and unique IDs for each object.

directory
Copy code
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

