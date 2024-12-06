from pathDisplay import get_path
from pathing import Graph
import re
import os

#from PIL import Image, ImageFilter


def convert1(image):
    folder_path = "./tempMapStuff/"
    file_path = f"{folder_path}{image}"
    img = Image.open(file_path)
    img = img.convert("RGBA")
    pixdata = img.load()
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            r, g, b, a = pixdata[x, y]
            if r > 200 and g > 200 and b > 200:
                # Set white pixels to transparent
                pixdata[x, y] = (255, 255, 255, 0)
    img.save("./" + image[:-4] + ".png", "PNG")


#from PIL import Image, ImageFilter, ImageChops


def set_non_transparent_to_blue(input_path, output_path, radius=2):
    with Image.open(input_path) as img:
        # Convert the image to RGBA mode if it's not already
        blurred_image = img.filter(ImageFilter.GaussianBlur(radius))
        img = blurred_image.convert('RGBA')

        # Create a new image with fully transparent background
        mask = Image.new('RGBA', img.size, (0, 0, 0, 0))

        # Iterate over each pixel in the image
        for x in range(img.width):
            for y in range(img.height):
                # Get the pixel color at the current position
                pixel = img.getpixel((x, y))

                # If the pixel is not fully transparent, set it to blue in the mask
                if pixel[3] != 0:
                    mask.putpixel((x, y), (0, 0, 255, 255))

        # Composite the original image onto the inverted mask
        result = Image.alpha_composite(mask, img)

        # Save the result
        result.save(output_path, "PNG")


def find():
    g = Graph(171)
    p = []
    nodes = [
        80, 24, 54, 150, 78, 111, 136, 65, 20, 117, 153, 115, 167, 127, 116,
        10, 113, 63, 64, 168, 165, 158, 32, 86, 38, 136, 17
    ]
    for x in range(170):
        for y in range(x + 1, 170):
            p.append(g.dijkstra(x, y))

    for path in p:
        get_path(path)


# find()
with open('out.txt', 'r') as file:
    warnings = file.readlines()

unique_warnings = set(warnings)
"""
missing = [
'Warning: Image not found for path between 161 and 160\n', 
'Warning: Image not found for path between 13 and 19\n', 
'Warning: Image not found for path between 91 and 78\n', 
'Warning: Image not found for path between 33 and 31\n', 
'Warning: Image not found for path between 85 and 98\n', 
'Warning: Image not found for path between 52 and 41\n', 
'Warning: Image not found for path between 48 and 62\n', 
'Warning: Image not found for path between 56 and 48\n', 
'Warning: Image not found for path between 149 and 155\n', 
'Warning: Image not found for path between 41 and 39\n', 
'Warning: Image not found for path between 75 and 85\n', 
'Warning: Image not found for path between 162 and 165\n', 
'Warning: Image not found for path between 32 and 33\n', 
'Warning: Image not found for path between 66 and 72\n', 
'Warning: Image not found for path between 97 and 85\n', 
'Warning: Image not found for path between 130 and 112\n',
'Warning: Image not found for path between 21 and 33\n', 
'Warning: Image not found for path between 22 and 35\n',

'Warning: Image not found for path between 102 and 90\n'}
'Warning: Image not found for path between 103 and 118\n',
"""
missing = unique_warnings
pattern = r'between (\d+) and (\d+)'

# Extract the numbers from the paths using regular expressions
numbers = [[match.group(1), match.group(2)] for item in missing
           if (match := re.search(pattern, item))]
output = []
for item in numbers:
    item.sort()
    
    output.append(f"{item[0]}-{item[1]}")
for item in output:
    directory = os.listdir("./static/BoldedMap/")
    if not directory.count(item + ".png"):
        if os.path.isfile("./tempMapStuff/" + item + ".jpg"):
            convert1(item + ".jpg")
            set_non_transparent_to_blue(f"./{item}.png",
                                        f"./static/BoldedMap/{item}.png", 2)

print(output)
