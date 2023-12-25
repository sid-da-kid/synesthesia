import cv2
from matplotlib import pyplot as plt
img = cv2.imread('img1.jpeg')
plt.imshow(img, cmap = 'Spectral', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()