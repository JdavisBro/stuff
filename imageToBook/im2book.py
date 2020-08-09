from PIL import Image
import os

title = input("Title: ")
author = input("Author: ")
imageName = input("Image Name: ")
imageExtension = "." + input("Image Extension: .")

colourCharacter = "⬛"

transparancyCharacter = "⬜"

image = Image.open(imageName+imageExtension)

image = image.resize((14,14))

pixels = list(image.getdata())

hexPixels = []

for pixel in pixels:
    if pixel[3] != 0:
        rgb = []
        for i in range(3):
            value = hex(pixel[i])[2:]
            if len(value) < 2:
                value = f"0{value}" 
            rgb.append(value)
        hexPixels.append(f"#{rgb[0]}{rgb[1]}{rgb[2]}")
    else:
        hexPixels.append(transparancyCharacter)

pages = []
page = []
previousPixel = ""
previousColour = ""

for i in range(len(hexPixels)):
    pixel = hexPixels[i]
    if pixel == previousColour:
        previousPixel["text"] += transparancyCharacter if pixel == transparancyCharacter else colourCharacter
        os.system("clear")
        print(f"{round((i+1)/len(hexPixels)*100,2)}%\n[{'#'*(round((i+1)/len(hexPixels)*100/4))}{'-'*(25-round((i+1)/len(hexPixels)*100/4))}]")
        continue
    if previousPixel:
        page.append(previousPixel)
    previousColour = pixel
    colour = pixel if pixel.startswith("#") else "#FFFFFF"
    previousPixel = {"color": f"{colour}", "text": transparancyCharacter if pixel == transparancyCharacter else colourCharacter}
    os.system("clear")
    print(f"{round((i+1)/len(hexPixels)*100,2)}%\n[{'#'*(round((i+1)/len(hexPixels)*100/4))}{'-'*(25-round((i+1)/len(hexPixels)*100/4))}]")
pages.append(f'{page}')

bookNBT = {"title": title,"author": author,"pages": pages}

command = f"/give @p written_book{bookNBT}"

if not os.path.exists("output.txt"):
    open("output.txt","x")

with open("output.txt","w") as f:
    f.write(str(command))