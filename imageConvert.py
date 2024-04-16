from PIL import Image, ImageFilter

from PIL import Image, ImageFilter

import os


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


def removeWhiteBackgrounds():
    folder_path = "./tempMapStuff/"

    for image in os.listdir(folder_path):
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
        img.save("./static/MapPieces/" + image[-3] + ".png", "PNG")


def convertImage():
    folder_dir = "./static/tempMapStuff/relabeledImages"
    for image in os.listdir(folder_dir):
        if image.endswith(".jpg"):
            image_path = os.path.join(folder_dir, image)
            imageName = image[:-4]

            img = Image.open(image_path)
            img = img.convert("RGBA")

            datas = img.getdata()

            newData = []

            for item in datas:
                if item[0] == 255 and item[1] == 255 and item[2] == 255:
                    newData.append((255, 255, 255, 0))
                else:
                    newData.append(item)

            img.putdata(newData)

            # Create a mask to identify non-white pixels
            mask = Image.new("L", img.size, 0)
            mask.putdata([255 if pixel[3] != 0 else 0 for pixel in newData])

            # Paste the original image onto a new transparent background
            new_img = Image.new("RGBA", img.size, (0, 0, 0, 0))
            new_img.paste(img, mask=mask)

            new_img.save(f"./static/tempMapStuff/Converted/{imageName}.png",
                         "PNG")
            new_img.save(f"./static/tempMapStuff/Converted/{imageName}.png",
                         "PNG")
            img.close()  # Close the original image file
            new_img.close()  # Close the new image file
            print("Successful")


convertImage()
