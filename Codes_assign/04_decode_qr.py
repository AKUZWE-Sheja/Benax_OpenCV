from pyzbar.pyzbar import decode
from PIL import Image

# Load the QR Code image
qr_image = Image.open("ASS_IMG_4.jpg")

# Decode the QR Code
decoded_data = decode(qr_image)

# Print the decoded data without saving it
for obj in decoded_data:
    raw_data = obj.data
    print(f"Raw Data: {raw_data}")  # Byte data

    try:
        # Decode as UTF-8 (supports non-English characters)
        decoded_text = raw_data.decode("utf-8")
        print(f"Decoded Data: {decoded_text}")
    except UnicodeDecodeError as e:
        print(f"UTF-8 Decode Error: {e}")



# OpenCV was less accurate for low-resolution and damaged QR codes.