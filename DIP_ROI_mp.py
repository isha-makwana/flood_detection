import cv2
import numpy as np
from matplotlib import pyplot as plt

 
#if __name__ == '__main__' :
 
    # Read image
im = cv2.imread(r'C:\Users\ISHA\Downloads\waterlevel.jpg')
 
    # Select ROI
r = cv2.selectROI(im)
 
    # Crop image
imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
 
    # Display cropped image
cv2.imshow("Image", imCrop)

edges = cv2.Canny(imCrop,40,75)

plt.subplot(121),plt.imshow(imCrop,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

threshold = cv2.threshold(img, 45, 70, cv2.THRESH_BINARY)
 
plt.show()

cv2.waitKey(0)