import cv2

# Read an image from file
img = cv2.imread("N.jpg")
img = cv2.resize(img, (0, 0), fx=1.1, fy=1.1)
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)


# Display the image in a window
cv2.imshow('image', img)


# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
