from PIL import Image, ImageFilter

image = Image.open('img1.jpg')

width, height = image.size
print(width, height)

image_blur = image.filter(ImageFilter.BLUR)
image_contour = image.filter(ImageFilter.CONTOUR)
image_detail = image.filter(ImageFilter.DETAIL)
image_edge = image.filter(ImageFilter.EDGE_ENHANCE)
image_edge_more = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
image_find_edges = image.filter(ImageFilter.FIND_EDGES)
image_emboss = image.filter(ImageFilter.EMBOSS)
image_sharp = image.filter(ImageFilter.SHARPEN)
image_smooth = image.filter(ImageFilter.SMOOTH)
image_smooth_more = image.filter(ImageFilter.SMOOTH_MORE)

image_boxblur = image.filter(ImageFilter.BoxBlur(radius = 5))


image_boxblur.show()



