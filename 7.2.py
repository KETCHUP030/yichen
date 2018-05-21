from PIL import Image
im = Image.open("1.jpg")
w,h = im.size
c = 5
im.thumbnail((w//c, h//c))
im.save("1-.jpg","JPEG")