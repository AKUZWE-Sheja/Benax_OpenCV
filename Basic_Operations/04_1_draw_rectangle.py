import cv2  # Import OpenCV library

# Read the image 'lena.jpg'
image = cv2.imread('lena.jpg')
resized_image = cv2.resize(image, (image.shape[1] // 4, image.shape[0] // 4))

# Draw a green rectangle on the image
# Rectangle coordinates: top-left (750, 750), bottom-right (1500, 1500)
# Color: Green (BGR format: (0, 255, 0)), Thickness: 8 pixels

# cv2.rectangle(resized_image, (750, 750), (1500, 1500), (0, 255, 0), 8)
cv2.rectangle(resized_image, (185, 185), (375, 375), (0, 255, 0), 2) # divided everything by 4 & it worked

# Display the image in a new window named 'My Image'
cv2.imshow('My Image', resized_image)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Save the grayscale image to a new file
cv2.imwrite('lena_shapes.jpg', resized_image)

# Close all OpenCV windows to release resources
cv2.destroyAllWindows()