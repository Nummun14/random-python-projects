import cv2

# Read an image from file
img = cv2.imread("N.jpg")
img = cv2.resize(img, (500, 500))
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cropped_img = img[100:450, 100:450]

# Display the image in a window
cv2.imshow('image', img)
cv2.imshow('croppedImage', cropped_img)

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
