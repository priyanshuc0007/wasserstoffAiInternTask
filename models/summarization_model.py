import os
import torch
from PIL import Image, UnidentifiedImageError
from transformers import BlipProcessor, BlipForConditionalGeneration
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Hugging Face token from .env file
hf_token = os.getenv("HF_TOKEN")

# Load Hugging Face's BLIP model and processor with the token
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large", use_auth_token=hf_token)
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large", use_auth_token=hf_token)

# Check if CUDA is available (for GPU support)
device = "cuda" if torch.cuda.is_available() else "cpu"
model = model.to(device)

def summarize_text(image_path):
    try:
        # Open and process the image
        try:
            image = Image.open(image_path)
        except UnidentifiedImageError:
            return "Error: Invalid image file."

        inputs = processor(image, return_tensors="pt").to(device)

        # Generate caption
        with torch.no_grad():
            output = model.generate(**inputs)

        description = processor.decode(output[0], skip_special_tokens=True)
        return description

    except FileNotFoundError:
        return "Error: Image file not found."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"
