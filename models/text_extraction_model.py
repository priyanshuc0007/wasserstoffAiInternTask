import cv2
import pytesseract
from PIL import Image

# Optionally specify the Tesseract executable path if not in PATH
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_with_otsu(image_path):
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found at path: {image_path}")

    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Otsu's thresholding
    _, processed_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Convert back to PIL format for OCR
    pil_image = Image.fromarray(processed_image)

    return pil_image

def extract_text_with_otsu(image_path):
    try:
        # Preprocess the image using Otsu's thresholding
        processed_image = preprocess_with_otsu(image_path)

        # Run Tesseract OCR on the processed image
        extracted_text = pytesseract.image_to_string(processed_image)

        print(f"Extracted Text with Otsu's Preprocessing:\n{extracted_text}")
        return extracted_text

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except pytesseract.TesseractError as tess_error:
        print(f"Tesseract Error: {tess_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

