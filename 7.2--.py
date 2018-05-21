from PIL import Image
im = Image.open("1.jpg")
w,h = im.size
c = 5
im.resize((w//c,h//c)).save("1--.jpg","JPEG")