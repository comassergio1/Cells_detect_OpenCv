import cv2
import numpy as np


# Read image.
img = cv2.imread('photos/celdap11.jpg', cv2.IMREAD_COLOR)

# Convert to grayscale.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur using 4 * 4 kernel.
gray_blurred = cv2.blur(gray, (4, 4))
# cv2.imshow('Blur', gray_blurred)

#Blur using 2 * 2 Kernel for positive cells
blur_positive_cells = cv2.blur(gray, (2, 2))


# Apply Hough transform on the blurred image.
detected_circles = cv2.HoughCircles(gray_blurred,
				cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
			param2 = 30, minRadius = 10, maxRadius = 34)
cant_cell = 0

# Apply Hough transform on the blurred image for positive cells.
detected_positive_circles = cv2.HoughCircles(blur_positive_cells,
				cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
			param2 = 30, minRadius = 10, maxRadius = 21)
positive_cell = 0

# Draw circles that are detected.
if detected_circles is not None:

	# Convert the circle parameters a, b and r to integers.
	detected_circles = np.uint16(np.around(detected_circles))
    

	for pt in detected_circles[0, :]:
		a, b, r = pt[0], pt[1], pt[2]

		# Draw the circumference of the circle.
		cv2.circle(img, (a, b), r, (0, 255, 0), 2)

		# Draw a small circle (of radius 1) to show the center.
		cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
		cv2.imshow("Detected Cells", img)
		cant_cell = cant_cell + 1
		# cv2.waitKey(0)

# Draw circles that are detected.
if detected_positive_circles is not None:

	# Convert the circle parameters a, b and r to integers.
	detected_positive_circles = np.uint16(np.around(detected_positive_circles))
    

	for pt in detected_positive_circles[0, :]:
		a, b, r = pt[0], pt[1], pt[2]

		# Draw the circumference of the circle.
		cv2.circle(img, (a, b), r, (0, 0, 255), 20)

		# Draw a small circle (of radius 1) to show the center.
		cv2.circle(img, (a, b), 1, (255, 0, 0), 3)
		cv2.imshow("Detected Positive Cells", img)
		positive_cell = positive_cell + 1
		# cv2.waitKey(0)

print(cant_cell, "Celdas encontradas!")
print(positive_cell, "Celdas positivas encontradas!")
cv2.waitKey(0)
