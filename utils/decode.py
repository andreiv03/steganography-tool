from PIL import Image
import os

from utils.config import STATIC_IMAGES_DIR


def decode_image(file):
    try:
        with Image.open(file).convert("RGB") as image:
            width, height = image.size
            binary_message = []

            for column in range(width):
                for row in range(height):
                    red, green, blue = image.getpixel((column, row))
                    binary_message.extend([red & 1, green & 1, blue & 1])

            length_bits = "".join(map(str, binary_message[:32]))
            message_length = int(length_bits, 2)
            binary_string = "".join(map(str, binary_message[32 : 32 + message_length]))

            decoded_message = "".join(
                chr(int(binary_string[index : index + 8], 2))
                for index in range(0, len(binary_string), 8)
            )

            decoded_image_path = os.path.join(STATIC_IMAGES_DIR, "decoded.png")
            os.makedirs(os.path.dirname(decoded_image_path), exist_ok=True)
            image.save(decoded_image_path)

            print(f"Decoded image saved at: {decoded_image_path}")
            return decoded_message

    except Exception as exception:
        print(f"Error during decoding: {exception}")
        return "Message could not be decoded!"
