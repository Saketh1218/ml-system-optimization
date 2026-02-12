import os
import numpy as np
from PIL import Image


def load_image(image_path):
    """Load an image from the given path."""
    return Image.open(image_path)


def preprocess_image(image, target_size=(224, 224)):
    """Resize and normalize the image for model input."""
    image = image.resize(target_size)
    image_array = np.array(image) / 255.0  # Normalize to [0, 1]
    return image_array


def load_imagenet_data(data_dir):
    """Load the ImageNet dataset from the specified directory."""
    images = []
    labels = []
    for label in os.listdir(data_dir):
        label_dir = os.path.join(data_dir, label)
        if os.path.isdir(label_dir):
            for image_file in os.listdir(label_dir):
                image_path = os.path.join(label_dir, image_file)
                image = load_image(image_path)
                image_array = preprocess_image(image)
                images.append(image_array)
                labels.append(label)
    return np.array(images), np.array(labels)
