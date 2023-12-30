from PIL import Image, ImageColor
image = Image.open('img1.jpg')

# Rotate
image_rotate = image.rotate(60, expand = True, fillcolor = ImageColor.getcolor('lightgreen', 'RGB'))

# display
image_rotate.show()
