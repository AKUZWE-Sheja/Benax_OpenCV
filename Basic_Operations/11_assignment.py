import cv2  # Import OpenCV library

# Read the image 'assignment-001-given.jpg'
image = cv2.imread('assignment-001-given.jpg')
resized_image = cv2.resize(image, (image.shape[1] // 2, image.shape[0] // 2))

# Get image dimensions
height, width = resized_image.shape[:2]

print(height, width)

# Draw the rectangle
cv2.rectangle(resized_image, (130, 90), (495, 465), (0, 255, 0), 4)

# Define text properties
text = 'RAH972U'
font = cv2.FONT_ITALIC
font_scale = 1
font_thickness = 2
text_color = (0, 255, 0)

# Text position (based on your values)
x, y = 445, 75

# Padding around the text like in result.jpg
padding_x = 0
padding_y = 12

overlay = resized_image.copy() # to not modify resized_image
cv2.rectangle(
    overlay,
    (x - padding_x, y - (25 + padding_y)),  # Top-left corner with padding
    (x + 140 + padding_x, y + padding_y),  # Bottom-right corner with padding
    (0, 0, 0),  # Rectangle color (black)
    -1  # Fill the rectangle
)
alpha = 0.5  # Transparency factor
cv2.addWeighted(overlay, alpha, resized_image, 1 - alpha, 0, resized_image)

# Add text
cv2.putText(resized_image, text, (x, y), font, font_scale, text_color, font_thickness)
# cv2.putText(resized_image, 'RAH972U', (445, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

# Display the image in a new window named 'Image'
cv2.imshow('Image', resized_image)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Save the grayscale image to a new file
cv2.imwrite('assignment-result.jpg', resized_image)

# Close all OpenCV windows to release resources
cv2.destroyAllWindows()