from PIL import Image

image = Image.open('img1.jpg')

width, height = image.size
print(width, height)

image_flip_hor = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

image_flip_hor.show()
