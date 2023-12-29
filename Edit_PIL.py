from PIL import Image
img = Image.open('img1.jpg')

# Rotate
img_rotate = img.rotate(90, expand = True)



# display
img_rotate.show()