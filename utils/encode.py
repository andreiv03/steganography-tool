from PIL import Image
import os


def encode_image(file, message):
    image = Image.open(file).convert("RGB")
    width, height = image.size
    encode_image = image.copy()

    binary_message = "".join(
        format(character, "08b") for character in message.encode("utf-8")
    )

    index = 0

    for column in range(width):
        for row in range(height):
            if index >= len(binary_message):
                break

            red, green, blue = image.getpixel((column, row))

            if index < len(binary_message):
                red = (red & 0xFE) | int(binary_message[index])
                index = index + 1

            if index < len(binary_message):
                green = (green & 0xFE) | int(binary_message[index])
                index = index + 1

            if index < len(binary_message):
                blue = (blue & 0xFE) | int(binary_message[index])
                index = index + 1

            encode_image.putpixel((column, row), (red, green, blue))

        if index >= len(binary_message):
            break

    encode_image.save(os.path.join("static", "images", "encoded.png"))
