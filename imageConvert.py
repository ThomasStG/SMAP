from PIL import Image  
from PIL import ImageFilter  
import os
def removeWhiteBackgrounds():
    folder_path = "./static/images"
    filename = "CS233.jpg"
    file_path = os.path.join(folder_path, filename)
    img = Image.open(file_path)
    img = img.convert("RGBA")
    pixdata = img.load()
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            r, g, b, a = pixdata[x, y]
            if r > 200 and g > 200 and b > 200:
                pixdata[x, y] = (255, 255, 255, 0)  # Set white pixels to transparent
    img.save(os.path.splitext(file_path)[0] + ".png", "PNG")

removeWhiteBackgrounds()
