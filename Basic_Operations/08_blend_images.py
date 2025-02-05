import cv2  # Import OpenCV library

# Read two images of the same size
# Here, we use 'lena.jpg' twice for simplicity
image1 = cv2.imread('pig.png')
image2 = cv2.imread('fish.png')

# Blend the two images with equal weights (0.5 each)
# Weight basically mean influence to final product
blended = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)
resize_blended = cv2.resize(blended, (blended.shape[1] // 2, blended.shape[0] // 2))

# Display the blended image in a window
cv2.imshow('Image', resize_blended)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Save the blended image to a new file
cv2.imwrite('pish.png', resize_blended)

# Close all OpenCV windows
cv2.destroyAllWindows()