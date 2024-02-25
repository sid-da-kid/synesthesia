from PIL import Image
import numpy as np

img = Image.open('img1.jpg')

# Get picture information 
width, height = img.size
print(width, height)
print(img.getpixel((0,0)))

print(img.mode)
print(img.getbands())

# display image
img.show()




















