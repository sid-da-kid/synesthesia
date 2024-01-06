from PIL import Image, ImageOps

class Deformer():
    def getmesh(self, img):
        w,h = img.size
        # define a shape in the original image
        # source_shape = (0,0,0,h,w,h,w,0 ) 
        # define a rectangle in the new image
        # target_rect = (0,0,w,h) # top left, bottom right

        topleft = ((0, 0, w // 2, h // 2),(0, 0, 0, h, w // 2, h, w // 2, 0))
        topright = ((w // 2, 0, w, h // 2),(w // 2, 0, w // 2, h, 0, h, 0, 0))
        bottomleft = ((0, h // 2, w // 2, h),(0, h, 0, 0, w // 2, 0, w // 2, h))
        bottomright = ((w // 2, h // 2, w, h),(w // 2, h, w // 2, 0, 0, 0, 0, h))

        # return all the shapes
        return [topleft, topright, bottomleft, bottomright]
# image import
image = Image.open('img1.jpg')
deform = ImageOps.deform(image, Deformer())
deform.show()

