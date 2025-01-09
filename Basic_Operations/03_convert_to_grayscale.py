import cv2  # Import OpenCV library

# Read the original image 'lena.jpg'
image = cv2.imread('lena.jpg')
resized_image = cv2.resize(image, (image.shape[1] // 4, image.shape[0] // 4))

# Convert the image to grayscale
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# Display the image in a new window named 'Image'
cv2.imshow('Image', gray_image)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Save the grayscale image to a new file
cv2.imwrite('lena_gray.jpg', gray_image)

# Close all OpenCV windows to release resources
cv2.destroyAllWindows()