#getting individual channels, awesome merge effect
from PIL import Image

image = Image.open("taylor_swift.jpg")

#separate the colors from an image
r,g,b = image.split()


'''
r,g.show()
g.show()
b.show()
'''

new_img = Image.merge("RGB",(r,g,b))
new_img.show()



#basic transformation
image1 = Image.open("heart.png")
size_image = image1.resize((250,250))
flip_image = image1.transpose(Image.FLIP_TOP_BOTTOM)
spin_image = image1.transpose(Image.ROTATE_90)

size_image.show()
flip_image.show()
spin_image.show()




#modes and filters
from PIL import ImageFilter
image2 = Image.open("taylor_swift.jpg")

#L stands for luminance
black_white  = image2.convert("L")
black_white.show()

blur = image2.filter(ImageFilter.BLUR)
detail = image2.filter(ImageFilter.DETAIL)
edges = image2.filter(ImageFilter.FIND_EDGES)

blur.show()
detail.show()
edges.show()



