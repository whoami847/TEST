# utils/image_randomizer.py

import os
import random

def get_random_image(directory):
    """
    Load a random image from the specified directory.
    Returns the path to the image or None if directory is empty.
    """
    if not os.path.exists(directory):
        return None
    
    images = [f for f in os.listdir(directory) if f.endswith(('.png', '.jpg', '.jpeg'))]
    if not images:
        return None
    
    return os.path.join(directory, random.choice(images))
