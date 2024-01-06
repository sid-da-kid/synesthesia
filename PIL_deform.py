from PIL import Image, ImageOps

class Deformer():
    def getmesh(self, img):
    # define a shape in the original image
    source_shape = (8)
    # define a rectangle in the new image
    target_rect = (0, 0, 100, 200) # left, top, right, bottom
    # return all the shapes
    




image = Image.open('img1.jpg')

ImageOps.deform(image, Deformer())









