# utils/postprocessing.py
import os
import numpy as np
from PIL import Image, ImageDraw
import setuptools
import tensorflow as tf


def save_segmented_objects(original_image, boxes, classes, save_dir):
    segmented_images = []
    width, height = original_image.size

    for i, (box, cls) in enumerate(zip(boxes, classes)):
        ymin, xmin, ymax, xmax = box

        (left, right, top, bottom) = (xmin * width, xmax * width, ymin * height, ymax * height)

        # Crop the original image based on the bounding box
        tf.experimental.numpy.experimental_enable_numpy_behavior()

        obj_image = original_image.crop((left, top, right, bottom))

        # Save the segmented object with a filename format "i_c.png"
        save_path = os.path.join(save_dir, f"{i}_{cls}.png")
        obj_image.save(save_path)
        segmented_images.append(save_path)

    return segmented_images
