import cv2  # Import OpenCV library
import matplotlib.pyplot as plt

# Read the image file 'lena.jpg'
# Ensure 'lena.jpg' is in the same directory as this script
image = cv2.imread('lena.jpg') # this is basically a copy of the image

if image is None:
    print("Error: Image not found")
else:
    print("Image loaded successfully")

# Convert the image from BGR (OpenCV format) to RGB (matplotlib format)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the image using matplotlib
plt.imshow(image_rgb)
plt.axis('off')  # Hide the axis
plt.show()

# Using cv2 which is filling up the screen for a reason I do not know yet & I tried resizing
# import cv2
#
# # Load the image
# image = cv2.imread('lena.jpg')
#
# # Check if the image is loaded successfully
# if image is None:
#     print("Error: Image not found")
# else:
#     # Resize the image to fit the screen at least
#     resized_image = cv2.resize(image, (image.shape[1] // 4, image.shape[0] // 4))
#
#     # Display the resized image
#     cv2.imshow('Image Window', resized_image)
#
#     # Wait for a key press
#     cv2.waitKey(0)
#
#     # Close all windows
#     cv2.destroyAllWindows()

