import cv2
import numpy as np
import matplotlib.pyplot as plt

img_file = "img1.jpg"
cv2.namedWindow("Image With Logo", cv2.WINDOW_NORMAL)
img = cv2.imread(img_file)
img_file2 = "Logo1.png"
img2 = cv2.imread(img_file2)
img_mixed = cv2.addWeighted(img,0.7,img2,0.3,0)
cv2.imshow('Image With Logo',img_mixed)
cv2.waitKey(1000)
cv2.destroyAllWindows()


# THIS CODE HAS A BUG