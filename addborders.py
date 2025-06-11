from PIL import Image, ImageOps

# Open your image
img = Image.open('Gerotek 4x4 Cert.png')

# Add border
bordered_img = ImageOps.expand(img, border=10, fill='black')

# Save the image
bordered_img.save('gerotek_border.png')