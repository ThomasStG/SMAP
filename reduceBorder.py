from PIL import Image
import os

def reduce_border(image_path, output_path):
    # Load the image and convert it to RGBA mode
    img = Image.open(image_path).convert("RGBA")
    
    # Find the bounding box of the non-white pixels
    non_white_pixels = [(x, y) for x in range(img.width) for y in range(img.height) if img.getpixel((x, y))[:3] != (255, 255, 255)]
    if not non_white_pixels:
        return  # Image is entirely white, no need to crop
    
    min_x = min(non_white_pixels, key=lambda p: p[0])[0]
    max_x = max(non_white_pixels, key=lambda p: p[0])[0]
    min_y = min(non_white_pixels, key=lambda p: p[1])[1]
    max_y = max(non_white_pixels, key=lambda p: p[1])[1]
    
    # Crop the image using the bounding box
    cropped_img = img.crop((min_x, min_y, max_x + 1, max_y + 1))
    
    # Save the cropped image
    cropped_img.save(output_path)

# Example usage
for image in os.listdir("./static/MapPieces"):
    reduce_border(f"./static/MapPieces/{image}", f"./static/MapPieces/{image}")
