import numpy as np
import cv2 
from matplotlib import pyplot as plt

img = cv2.imread('image name',0)
edges = cv2.Canny(img,100,200)
plt.subplot(211),plt.imshow(img)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(212),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Detection using Canny'), plt.xticks([]), plt.yticks([])
plt.show()
