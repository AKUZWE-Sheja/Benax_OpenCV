import cv2  # Import OpenCV library

# Read the image 'lena.jpg'
image = cv2.imread('lena.jpg')
resized_image = cv2.resize(image, (image.shape[1] // 2, image.shape[0] // 2))

# Draw a green rectangle on the image
# Rectangle coordinates: top-left (750, 750), bottom-right (1500, 1500)
# Color: Green (BGR format: (0, 255, 0)), Thickness: 8 pixels

cv2.rectangle(resized_image, (375, 375), (750, 750), (0, 255, 0), 4)

# Draw a red circle on the image
# Center coordinates: (1125, 1125), Radius: 375
# Color: Red (BGR format: (0, 255, 0)), Thickness: 8 pixels
cv2.circle(resized_image, (562, 562), 187, (0, 0, 255), 4)

# Crop a region from the image
# Format: image[y0:y1, x0:x1]
#e.g. Crop height (i.e. y) from y0=750 to y1=1500, width (i.e x) from x0=750 to x1=1500
cropped_image = resized_image[375:750, 375:750]

# Display the cropped image in a window
cv2.imshow('Image', cropped_image)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Save the cropped region as a new image
cv2.imwrite('lena_cropped.jpg', cropped_image)

# Close all OpenCV windows
cv2.destroyAllWindows()
