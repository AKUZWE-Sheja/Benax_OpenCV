from pylibdmtx.pylibdmtx import decode
from PIL import Image

# Load the ECC 200 Data Matrix image
image = Image.open("ASS_IMG_2.jpg")

# Decode the ECC 200 Data Matrix
decoded = decode(image)

if decoded:
    print("Decoded Data:", decoded[0].data.decode('utf-8'))
else:
    print("No Data Matrix found.")