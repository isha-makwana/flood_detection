import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r'C:\Users\ISHA\Downloads\waterlevel.jpg',0)
edges = cv2.Canny(img,40,75)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

threshold = cv2.threshold(img, 45, 70, cv2.THRESH_BINARY)
 
plt.show()

    # Select ROI
r = cv2.selectROI(threshold)
 
    # Crop image
imCrop = threshold[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
 
    # Display cropped image
cv2.imshow("Image", imCrop)