import setuptools
import tensorflow as tf
import models
import cv2
import numpy as np


def preprocess_image(image):

    # Resize the image

    # Convert the image to a NumPy array
    image_np = np.array(image)
    # Normalize pixel values to the range [0.0, 1.0]
    image_np = image_np.astype(np.float32) / 255.0
    print(f"Image shape:  ", image_np.shape)

    image_tensor = tf.convert_to_tensor(image_np)
    image_tensor = tf.image.convert_image_dtype(image_tensor, dtype=tf.uint8)
    # image_tensor = tf.image.resize(image_tensor, input_size)
    image_tensor = tf.expand_dims(image_tensor, axis=0)

    return image_tensor
