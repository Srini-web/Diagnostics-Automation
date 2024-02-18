import cv2 
import numpy as np
a = cv2.VideoCapture(0)
def find_object_centroids(a):
    # Read the image
    image = cv2.imread(a)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to obtain binary image
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Find contours of objects
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    centroids = []

    # Iterate over contours
    for contour in contours:
        # Calculate the moments of the contour
        moments = cv2.moments(contour)

        # Avoid division by zero
        if moments["m00"] != 0:
            # Calculate the centroid coordinates
            cx = int(moments["m10"] / moments["m00"])
            cy = int(moments["m01"] / moments["m00"]) 
            # Add centroid to the list
            centroids.append((cx, cy))

            # Draw a circle at the centroid position
            cv2.circle(image, (cx, cy), 3, (0, 255, 0), -1)

    # Display the image with centroid points
    cv2.imshow("Image with Centroids", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return centroids

# Example usage
imp = r"C:\Users\lenovo\OneDrive\Desktop\ttim2.png"
centroids = find_object_centroids(imp)

# Print the centroids
for centroid in centroids:
    print("Centroid:", centroid)