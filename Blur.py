from PIL import Image, ImageFilter
from PIL import Image, ImageChops
import os


def blur_image(input_path, output_path, radius=2):
    with Image.open(input_path) as img:
        # Apply a Gaussian blur filter
        blurred_image = img.filter(ImageFilter.GaussianBlur(radius))

        # Save the blurred image
        blurred_image.save(output_path, "PNG")


"""# Example usage
input_image_path = './static/MapPieces/1-3.png'
output_image_path = 'output.png'
blur_image(input_image_path, output_image_path, radius=3)

"""


from PIL import Image, ImageFilter, ImageChops

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



def convert_all(radius=2):
    f = "./static/MapPieces/"
    to = "./static/BoldedMap/"
    for image in os.listdir("./static/MapPieces"):
        if image.endswith(".png"):
            set_non_transparent_to_blue(f"{f}{image}", f"{to}{image}", radius)


set_non_transparent_to_blue(f"./162-165.png", f"./162-165-2.png", 2)
