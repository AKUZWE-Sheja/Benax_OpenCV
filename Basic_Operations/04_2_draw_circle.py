import cv2  # Import OpenCV library

# Read the image 'lena.jpg'
image = cv2.imread('lena.jpg')
resized_image = cv2.resize(image, (image.shape[1] // 4, image.shape[0] // 4))

# Draw a red circle on the image
# Center coordinates: (1125, 1125), Radius: 375
# Color: Red (BGR format: (0, 255, 0)), Thickness: 8 pixels
# cv2.circle(resized_image, (1125, 1125), 375, (0, 0, 255), 8)
cv2.circle(resized_image, (281, 281), 93, (0, 0, 255), 2) # rounded off though

# Display the image in a new window named 'Image'
cv2.imshow('Image', resized_image)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Save the grayscale image to a new file
cv2.imwrite('lena_shapes.jpg', resized_image)

# Close all OpenCV windows to release resources
cv2.destroyAllWindows()