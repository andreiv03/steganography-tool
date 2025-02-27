from PIL import Image
import os

from utils.config import STATIC_IMAGES_DIR


def encode_image(file, message):
    try:
        with Image.open(file).convert("RGB") as image:
            width, height = image.size
            encoded_image = image.copy()

            binary_message = "".join(format(char, "08b") for char in message.encode("utf-8"))
            length_prefix = f"{len(binary_message):032b}"
            binary_message = length_prefix + binary_message
            message_length = len(binary_message)

            index = 0
            for column in range(width):
                for row in range(height):
                    if index >= len(binary_message):
                        break

                    red, green, blue = image.getpixel((column, row))

                    if index < message_length:
                        red = (red & 0xFE) | int(binary_message[index])
                        index += 1

                    if index < message_length:
                        green = (green & 0xFE) | int(binary_message[index])
                        index += 1

                    if index < message_length:
                        blue = (blue & 0xFE) | int(binary_message[index])
                        index += 1

                    encoded_image.putpixel((column, row), (red, green, blue))

                if index >= message_length:
                    break

            encoded_image_path = os.path.join(STATIC_IMAGES_DIR, "encoded.png")
            os.makedirs(os.path.dirname(encoded_image_path), exist_ok=True)
            encoded_image.save(encoded_image_path)

            print(f"Encoded image saved at: {encoded_image_path}")

    except Exception as exception:
        print(f"Error during encoding: {exception}")
