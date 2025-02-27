import os


def ensure_directory_exists(directory):
    os.makedirs(directory, exist_ok=True)


STATIC_IMAGES_DIR = "static/images"
ensure_directory_exists(STATIC_IMAGES_DIR)
