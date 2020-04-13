from PIL import Image
import sys,os

#  |        |‾‾‾‾‾‾‾‾|  |         Hey welcome to use the thing change the filename variable below to the name and also
#  |        |        |  |         change the fileextension to . the extension (keep the .) example: ".png"         
#  |        |        |  |         PYTHON 3 IS REQUIRED YOU MUST HAVE PYTHON3 GOOGLE IT!!!!!!
#  |        |        |  |         Pillow is required it can be gained with:  
#  |        |        |  |         Windows | py -m pip install Pillow - Linux | python -m pip install Pillow - Mac | fuck knows
#  |______  |________|  |_______  The TAB stuff will be outputted to imagetominecraftcolourcodething.txt and as an image 

if sys.version_info[0] != 3:
    print("Python 3 is required! If you already have it installed make sure you're running with the correct install!")
    exit()

fileName = "IMAGE" # DEFAULT IMAGE NAME
fileExtension = ".png" # DEFAULT IMAGE EXTENSION


colourCharacter = "⬛" # ⬛ is default 
transparancyCharacter = "⬜" # space can be weird sometimes - " " or "⬜" is reccomended

outputFileName = "imagetominecraftcolourcodething.txt" # DEFAULT OUTPUT TXT
outputImage = True # TRUE = OUTPUT IMAGE | FALSE = NO
outputImageName = fileName + "2" # Default image output name

tabPlugin = False # TRUE = DO TAB MINECRAFT PLUGIN | FALSE = NO
animation = False # TRUE = DO TAB ANIMATION | FALSE = NO
animationText = ["b","i","g","c","h","u","n","g","u","s"]
animationInterval = 750 # ms

args = sys.argv[1:]

def sendHelp():
    print("  _    _ ______ _      _____  \n | |  | |  ____| |    |  __ \ \n | |__| | |__  | |    | |__) |\n |  __  |  __| | |    |  ___/ \n | |  | | |____| |____| |     \n |_|  |_|______|______|_|     \n\n")
    print(f"""{'-'*9}{'-'*len(sys.argv[0])}{'-'*30}
| python {sys.argv[0]} <imageInputFileName> [args] |
{'-'*9}{'-'*len(sys.argv[0])}{'-'*30}
 --help - Shows this!
 --output - Text - Text file output for tellraw and TAB plugin
 --image - File name for image input (no extension) - Default: IMAGE
 --outputImage - True/False - If an image should be outputted - Default: true
 --outputImageName - Text - File name for image output (no extension) - Default imageInputFileName2
 --extension - Text - File extension for image input and output - Default: png
 --tabOutput - True/False - Output config for the TAB server plugin
 --tabAnimation - True/False - Output config for a TAB animation using animationText as the characters to switch between
 --animationText - Text - Characters for the image to switch between in a TAB animation.

To use the output in TAB copy the stuff underneeth # CONFIG STUFF # in the output text file into the tab menu part of TAB config.yml and for animations paste the stuff under # ANIMATION STUFF # into the animations.yml (make sure to copy the config stuff too!)
""")
    exit()

if not args:  #NOT ARGUMENTS!
    print("\n\n----------------- NO ARGUMENTS FOUND -----------------\n")
    sendHelp()
else: #ARGUMENTS
    argNumber = -1
    ignoreNext = False
    for arg in args:
        argNumber += 1
        if ignoreNext:
            ignoreNext = False
            continue
        if arg.startswith("--"):
            arg = arg[2:]
            #print(args,arg)
            if arg == "output": # TEXT OUTPUT
                outputFileName = args[argNumber + 1]
                print(f"Text Output File: '{outputFileName}'")
            elif arg == "image": # IMAGE INPUT
                fileName = args[argNumber + 1]
                print(f"Image Input File Name: '{fileName}'")
            elif arg == "extension": # IMAGE FILE EXTENSION
                fileExtension = "." + args[argNumber + 1]
                print(f"Image File Extensions: '{fileExtension}")
            elif arg == "outputImage": # OUTPUT IMAGE
                if args[argNumber+1].lower() in ["true","yes","y"]:
                    outputImage = True
                    print("Output Image: True")
                elif args[argNumber+1].lower() in ["false","no","n"]:
                    outputImage = False
                    print("Output Image: False")
            elif arg == "outputImageName": # OUTPUT IMAGE NAME
                outputImageName = args[argNumber + 1]
                print(f"Image Output File Name: '{outputImageName}'")
            elif arg == "tabOutput": # TAB OUTPUT
                if args[argNumber+1].lower() in ["true","yes","y"]:
                    tabPlugin = True
                    print("Output TAB: True")
                elif args[argNumber+1].lower() in ["false","no","n"]:
                    tabPlugin = False
                    print("Output TAB: False")
            elif arg == "tabAnimation": # TAB ANIMATION
                if args[argNumber+1].lower() in ["true","yes","y"]:
                    animation = True
                    print("Output TAB Animation: True")
                elif args[argNumber+1].lower() in ["false","no","n"]:
                    animation = False
                    print("Output TAB Animation: False")
            elif arg == "animationText": # TAB ANIMATION TEXT
                animationText = list(args[argNumber+1])
                print(f"Animation Text: '{args[argNumber+1]}' ({animationText})")
            elif arg == "animationInterval": # ANIMATION INTERVAL
                animationInterval = args[argNumber+1]
                print(f"Animation Interval: {animationInterval}")
            elif arg == "colourCharacter": # COLOUR CHARACTER
                colourCharacter = args[argNumber+1]
                print(f"Colour Character: '{colourCharacter}'")
            elif arg == "transparancyCharacter": # TRANSPARANCY CHARACTER
                transparancyCharacter = args[argNumber+1]
                print(f"Transparancy Character: '{transparancyCharacter}'")
            elif arg == "help": # HELP
                sendHelp()
            ignoreNext = True
        else:
            fileName = arg
            print(f"Image Input File Name: '{fileName}'")

print("\nChecking for any file issues")

if outputImage:
    if os.path.isfile(outputImageName+fileExtension):
        try:
            input(f"WARNING: {outputImageName+fileExtension} is already a file and will be overwritten.\nPress ENTER to continue and CTRL + C to cancel.\n")
        except KeyboardInterrupt:
            print("Cancelled")
            exit()

print("Making sure output file exists.")
try:
    open(outputFileName,"x")
except:
    pass

def nearest_colour( subjects, query ):
    return min( subjects, key = lambda subject: sum( (s - q) ** 2 for s, q in zip( subject, query ) ) )

im = Image.open(fileName+fileExtension)

colours = (
    (0,0,0,"&0"),
    (0,0,170,"&1"),
    (0,170,0,"&2"),
    (0,170,170,"&3"),
    (170,0,0,"&4"), 
    (170,0,170,"&5"),
    (255,170,0,"&6"),
    (170,170,170,"&7"),
    (85,85,85,"&8"),
    (85,85,255,"&9"),
    (85,255,85,"&a"), 
    (85,255,255,"&b"),
    (255,85,85,"&c"), 
    (255,85,255,"&d"),
    (255,255,85,"&e"),
    (255,255,255,"&f")
)

pixels = list(im.getdata())
colourcodes = []
newpixels = []

print("\nGetting Minecraft Colours")

for pixel in pixels:
    try:
        if pixel[3] != 0:
            pixel = tuple(list(pixel)[:-1])
            colourcodes.append(nearest_colour(colours,pixel)[3])
            newpixels.append(tuple(list(nearest_colour(colours,pixel))[:-1]))
        else:
            pixel = tuple(list(pixel)[:-1])
            colourcodes.append("space")
            newpixels.append(tuple(list(nearest_colour(colours,pixel))[:-1]))
    except:
        colourcodes.append(nearest_colour(colours,pixel)[3])
        newpixels.append(tuple(list(nearest_colour(colours,pixel))[:-1]))

# CREATE IMAGE AND SAVE
print("\nCreating Image")

im2 = Image.new("RGB", im.size)
im2.putdata(newpixels)

im2.save(outputImageName+fileExtension)

print("Image Saved")

textToWrite = ""

# TAB PLUGIN
if tabPlugin:
    lines = []
    line = ""
    number = 0
    previous = ""
    if not animation: # NOT ANIMATION
        print("\nMaking TAB Stuff")
        for colourcode in colourcodes:
            number += 1
            if colourcode != "space":
                if previous != colourcode:
                    line += f"{colourcode}{colourCharacter}"
                else:
                    line += colourCharacter
            else:
                if previous != colourcode:
                    line += f"&r{transparancyCharacter}"
                else:
                    line += transparancyCharacter
            previous = colourcode
            if number >= im.size[0]:
                number = 0
                lines.append(line)
                line = ""
                previous = ""
        for liners in lines:
            textToWrite += f'\n\n{"#"*60}\nTAB CONFIG STUFF\n{"#"*60}\n\n  - "{liners}"\n'
        print("TAB Stuff Made")

    else: # ANIMATION
        print("\nMaking TAB Animation")
        animations = {}
        lines = {}
        for colourCharacter in animationText:
            print(f"Creating image for {colourCharacter} frame.")
            linenumber = 1
            for colourcode in colourcodes:
                number += 1
                if colourcode != "space":
                    if previous != colourcode:
                        line += f"{colourcode}{colourCharacter}"
                    else:
                        line += colourCharacter
                else:
                    if previous != colourcode:
                        line += f"&r{transparancyCharacter}"
                    else:
                        line += transparancyCharacter
                previous = colourcode
                if number >= im.size[0]:
                    number = 0
                    if linenumber not in lines:
                        lines[linenumber] = []
                    lines[linenumber].append(line)
                    linenumber += 1
                    line = ""
                    previous = ""
            configStuff= ""
            print("Creating config.yml and animation.yml text.")
            for i in range(1,len(list(lines.keys()))+1):
                textToWrite += f'  {fileName}{i}:\n    change-interval: {animationInterval}\n    texts:\n'
                for line in lines[i]:
                    textToWrite += f'      - "{line}"\n'
                configStuff += f'  - "%animation:{fileName}{i}%"\n'
            textToWrite += f"\n\n{'#'*60}\nTAB CONFIG STUFF\n{'#'*60}\n\n"
            textToWrite += configStuff
        print("Animation Stuff Complete")

if textToWrite:
    print(f"Saving to {outputFileName}.")
    with open(outputFileName,"w+",encoding="utf-8") as f:
        f.write(textToWrite)

print(f"\n\nFinished!")