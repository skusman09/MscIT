import numpy as np
import cv2
from google.colab.patches import cv2_imshow

# Read image
img = cv2.imread('/content/drive/MyDrive/DS_PRACTICAL_NOTES/DS_P10_hough.jpg',cv2.IMREAD_COLOR)

cv2_imshow(img)
# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Find the edges in the image using canny detector
edges = cv2.Canny(gray, 50, 200)

# Detect points that form a line
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 68, minLineLength=15, maxLineGap=250)

# Draw lines on the image
for line in lines:
   x1, y1, x2, y2 = line[0]
   cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
# Show result
print("Line Detection using Hough Transform")
from google.colab.patches import cv2_imshow
cv2_imshow(img)
cv2.waitKey(0)
cv2.destroyAllWindows()