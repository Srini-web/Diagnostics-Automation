import cv2
import numpy as np

# Load the image
image_path = 'C:\\Users\\lenovo\\OneDrive\\Desktop\\tray2.png'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
dl = []

# Apply Gaussian blur to reduce noise
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Apply Canny edge detection
edges = cv2.Canny(blurred_image, threshold1=50, threshold2=150)

# Detect circles using Hough Circle Transform
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1, minDist=40,
                           param1=100, param2=20, minRadius=10, maxRadius=25)

# Convert circles to integer coordinates
if circles is not None:
    circles = np.uint16(np.around(circles))
    colored_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    # Iterate through detected circles and append centroids to the list
    for circle in circles[0, :]:
        cX, cY = circle[0], circle[1]
        dl.append((cX, cY))
        cv2.circle(colored_image, (cX, cY), circle[2], (0, 255, 0), 2)  # Draw circle
        cv2.circle(colored_image, (cX, cY), 2, (0, 0, 255), 3)  # Draw centroid

# Sort the list of tuples based on y-coordinate first and then x-coordinate
sorted_tuples = sorted(dl, key=lambda t: (t[1], t[0]))

# Reshape the sorted list into a 4x12 matrix
rows = [sorted_tuples[i:i+12] for i in range(0, len(sorted_tuples), 12)]

# Print the arranged matrix
for row in rows:
    for tuple_val in row:
        print(tuple_val, end=' ')
    print()

# Display the image with circles and centroids
cv2.imshow('Detected Circles and Centroids', colored_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
