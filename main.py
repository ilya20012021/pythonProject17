import qrcode
from PIL import Image, ImageDraw

img = qrcode.make("https://github.com/VoLuIcHiK/bowhead-whales")
img.save("bowhead-whales.png")
