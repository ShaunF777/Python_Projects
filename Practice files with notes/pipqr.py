# After pip install qrcode
import qrcode

img = qrcode.make("https://youtu.be/xvFZjo5PgG0")
img.save("qr.png", "PNG")

# To make code of this url run:
# python3 pipqr.py
# code pipqr.png 

# awesome other fun libraries to make your day
# https://umarfarooquekhan.medium.com/13-fun-python-libraries-to-make-your-day-better-%EF%B8%8F-%EF%B8%8F-6ebe9b58e4f0