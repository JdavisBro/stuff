import os
import shutil
import subprocess
import zipfile

from PIL import Image

colormaps = False # change to true to enable averaging of the colormaps which will make grass white and foliage the same colour in all biomes

transparency = True # change to false to disable transparency which means all textures will be a full square of one colour, text also becomes a square.

removeOverlay = False # change to true to remove grass block side overlay to make the side of the grass block one colour

text = "Starting"
subprocess.run(["clear"])
print(text)

files = []

for di in list(os.walk("assets"))[0][1]:
    for d in os.walk("assets/"+di+"/textures"):
        os.makedirs("out/" + d[0],exist_ok=True)
        if d[0] == "colormap" and colormaps == False:
            continue
        for f in d[2]:
            if f.endswith(".png"):
                files.append(d[0] + "/" + f)

duplicate = 0 # 0 ask 1 replace 2 continue

text += "\nModifying Textures"
number = 0

for f in files:
    number += 1
    subprocess.run(["clear"])
    print(f"{text}\n{f}\n{number}/{len(files)}")
    if os.path.exists("out/"+f):
        if duplicate == 0:
            inp = input("File already exists, do you want to [o]verwrite, [c]ontinue (skip to next texture), [s]kip all (continue without modifying any textures), add [a] after selection to do to all conflicting files. ")
            if inp[0] == "s":
                break
            if inp.endswith("a"):
                if inp[0] == "o":
                    duplicate = 1
                    pass
                elif inp[0] == "c":
                    duplicate = 2
                    continue
            else:
                if inp[0] == "c":
                    continue
                elif inp[0] != "o":
                    continue
        elif duplicate == 2:
            continue
    im = Image.open(f)
    im = im.convert("RGBA")
    pixels = list(im.getdata())
    rgb = [0,0,0]
    nPixels = 0
    trans = False
    for pixel in pixels:
        if pixel[3] <= 10:
            trans = True
            continue
        if pixel[3] < 255:
            trans = True
        rgb[0] += pixel[0]
        rgb[1] += pixel[1]
        rgb[2] += pixel[2]
        nPixels += 1
    if nPixels != 0:
        rgb[0] = round(rgb[0]/nPixels)
        rgb[1] = round(rgb[1]/nPixels)
        rgb[2] = round(rgb[2]/nPixels)
    if trans and transparency:
        newPixels = []
        for pixel in pixels:
            newPixels.append((rgb[0],rgb[1],rgb[2],pixel[3]))
        im2 = Image.new("RGBA", im.size)
        im2.putdata(newPixels)
    else:
        im2 = Image.new("RGB", im.size,(rgb[0],rgb[1],rgb[2]))
    if "overlay" in f and removeOverlay:
        im2 = Image.new("RGBA",im.size,(0,0,0,0))
    im2.save("out/"+f)
    if os.path.exists(f+".mcmeta"):
        shutil.copyfile(f+".mcmeta","out/"+f+".mcmeta")

subprocess.run(["clear"])
print(f"{text}\nZipping File...")

if os.path.exists("1xPack.zip"):
    os.remove("1xPack.zip")
ziph = zipfile.ZipFile('1xPack.zip', 'w', zipfile.ZIP_DEFLATED)
os.chdir("out")
for root, dirs, files in os.walk("."):
    for f in files:
        ziph.write(os.path.join(root, f), os.path.relpath(os.path.join(root,f)))
os.chdir("..")
ziph.close()

print("Done!")
