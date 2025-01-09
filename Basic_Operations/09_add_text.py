import cv2  # Import OpenCV library

# Read the image 'lena.jpg'
image = cv2.imread('lena.jpg')
resized_image = cv2.resize(image, (image.shape[1] // 4, image.shape[0] // 4))

# Add text to the image
# Text: 'Hello OpenCV!', Location (x,y): (100, 200)
# Font: FONT_HERSHEY_SIMPLEX, Scale: 1, Color: Green (BGR: (0, 255, 0)), Thickness: 14
cv2.putText(resized_image, 'Lena, the famous!', (25, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

# Display the image with text in a window
cv2.imshow('Image', resized_image)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Save the image with text to a new file
cv2.imwrite('lena_text.jpg', resized_image)

# Close all OpenCV windows
cv2.destroyAllWindows()