from PIL import Image, ImageEnhance

image = Image.open('img1.jpg')

width, height = image.size
print(width, height)

# create an enhancer
color_enhancer = ImageEnhance.Color(image)
contrast_enhancer = ImageEnhance.Contrast(image)
brightness_enhancer = ImageEnhance.Brightness(image)
sharpness_enhancer = ImageEnhance.Sharpness(image)

# enhance image
enhanced_image = color_enhancer.enhance(2)
#enhanced_image = brightness_enhancer.enhance(2)
#enhanced_image = contrast_enhancer.enhance(2)
#enhanced_image = sharpness_enhancer.enhance(2)


enhanced_image.show()



