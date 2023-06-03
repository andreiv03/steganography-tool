from PIL import Image
import os


def decode_image(file):
    image = Image.open(file).convert("RGB")
    width, height = image.size

    binary_message = ""
    decoded_message = ""

    for column in range(width):
        for row in range(height):
            red, green, blue = image.getpixel((column, row))

            binary_message = binary_message + str(red & 1)
            binary_message = binary_message + str(green & 1)
            binary_message = binary_message + str(blue & 1)

    for index in range(0, len(binary_message), 8):
        byte = binary_message[index : index + 8]
        character = chr(int(byte, 2))

        if ord(character) <= 127:
            decoded_message = decoded_message + character
        else:
            break

    image.save(os.path.join("static", "images", "decoded.png"))
    return decoded_message
