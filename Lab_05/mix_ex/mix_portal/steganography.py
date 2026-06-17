from pathlib import Path

from PIL import Image


SENTINEL = "1111111111111110"


def encode_image(image_path: Path, message: str, output_path: Path):
    img = Image.open(image_path).convert("RGB")
    width, height = img.size
    binary_message = "".join(format(ord(char), "08b") for char in message) + SENTINEL

    capacity = width * height * 3
    if len(binary_message) > capacity:
        raise ValueError("Message is too long for this image")

    data_index = 0
    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col, row)))
            for color_channel in range(3):
                if data_index < len(binary_message):
                    pixel[color_channel] = int(
                        format(pixel[color_channel], "08b")[:-1] + binary_message[data_index],
                        2,
                    )
                    data_index += 1
            img.putpixel((col, row), tuple(pixel))
            if data_index >= len(binary_message):
                output_path.parent.mkdir(parents=True, exist_ok=True)
                img.save(output_path)
                return output_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(output_path)
    return output_path


def decode_image(image_path: Path):
    img = Image.open(image_path).convert("RGB")
    binary_message = ""

    for row in range(img.height):
        for col in range(img.width):
            pixel = img.getpixel((col, row))
            for color_channel in range(3):
                binary_message += format(pixel[color_channel], "08b")[-1]
                if binary_message.endswith(SENTINEL):
                    payload = binary_message[: -len(SENTINEL)]
                    return _binary_to_text(payload)

    return _binary_to_text(binary_message)


def _binary_to_text(binary_message: str):
    chars = []
    for index in range(0, len(binary_message), 8):
        chunk = binary_message[index : index + 8]
        if len(chunk) < 8:
            break
        chars.append(chr(int(chunk, 2)))
    return "".join(chars)
