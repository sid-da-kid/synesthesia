from PIL import Image, ImageOps

img = Image.open('img1.jpg')

# colour changes
image_greyscale = ImageOps.grayscale(image = img)
image_contrast = ImageOps.autocontrast(image = img, cutoff = 2)
# colour inversion of an image
image_invert = ImageOps.invert(img)



image_greyscale.show()

