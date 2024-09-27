import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
from PIL import Image

# Load the Faster R-CNN model from TensorFlow Hub
def load_segmentation_model():
    model = hub.load("https://tfhub.dev/tensorflow/faster_rcnn/resnet50_v1_640x640/1")
    return model

def preprocess_image(image_path):
    image = Image.open(image_path)
    image = image.resize((640, 640))  # Resize to the input size the model expects
    image_np = np.array(image)
    image_tensor = tf.convert_to_tensor(image_np, dtype=tf.float32)
    image_tensor = tf.image.convert_image_dtype(image_tensor, dtype=tf.float32)
    image_tensor = tf.expand_dims(image_tensor, axis=0)  # Add batch dimension
    return image_tensor

def segment_image(model, image_tensor):
    # Run the model to get the predictions
    output = model(image_tensor)

    # Extract scores, bounding boxes, and classes
    unfiltered_classes = output['detection_classes'][0].numpy()
    unfiltered_boxes = output['detection_boxes'][0].numpy()
    unfiltered_scores = output['detection_scores'][0].numpy()

    # Set a confidence threshold
    confidence_threshold = 0.5

    # Filter out boxes with low confidence scores using boolean masking
    high_confidence_mask = unfiltered_scores > confidence_threshold

    boxes = unfiltered_boxes[high_confidence_mask]
    scores = unfiltered_scores[high_confidence_mask]
    classes = unfiltered_classes[high_confidence_mask]

    # Print debugging information to verify extraction
    print("Boxes in segment_image function:", boxes)
    print("Classes in segment_image function:", classes)
    print("Scores in segment_image function:", scores)

    return scores, boxes, classes
