from PIL import Image

image = Image.open('img1.jpg')

width, height = image.size
print(width, height)

left = 20
top = height / 4
right = 164
bottom = 3 * height / 4

image1 = image.crop((left, top, right, bottom))

image1.show()
