from PIL import Image, ImageOps

# Open your image
img = Image.open('Hotrod.png')

# Add border
bordered_img = ImageOps.expand(img, border=10, fill='black')

# Save the image
bordered_img.save('Hotrod1.png')