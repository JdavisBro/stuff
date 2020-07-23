from PIL import Image

image_name = "image.png"

img = Image.open(image_name)

im = Image.new("RGBA",(img.size[0]*2,img.size[1]),(255,0,0,0))

im.paste(img.copy(),(0,0))
im.paste(img.copy(),(img.size[0],0))

sections = int(img.size[0]/10)*-1

images = []
images.append(img)

for i in range(10):
    im = im.transform(im.size, Image.AFFINE, (1, 0, sections, 0, 1, 0))
    im_crop = im.copy().crop((im.size[0]/2,0,im.size[0],im.size[1]))
    images.append(im_crop)

frame = 0
for image in images:
    frame += 1
    image.save(f"frames/{frame}.png")

print("Completed! To create the gif open all of the pngs in the frames folder as layers in GIMP then save as a gif with animation and frame disposal. (because PIL gif exporting is low quality)")