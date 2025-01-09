import cv2  # Import OpenCV library

# Read the image 'lena.jpg'
image = cv2.imread('lena.jpg')
resized_image = cv2.resize(image, (image.shape[1] // 4, image.shape[0] // 4))

# Display the original image in a window
cv2.imshow('Image', resized_image)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Save the image in PNG format
cv2.imwrite('lena_image.png', resized_image)

# Save the image in BMP format
cv2.imwrite('lena_image.bmp', resized_image)

# Close all OpenCV windows
cv2.destroyAllWindows()