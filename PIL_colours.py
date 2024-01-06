from PIL import Image, ImageEnhance

example_image1 = Image.open('img1.jpg')

###############################
# Analyse picture information #
###############################

width, height = example_image1.size
print(width, height)

print(example_image1.getpixel((0,0)))



# display image
example_image1.show()




















