#!/usr/bin/env python

from PIL import Image, ImageDraw, ImageFont

text = "Ar šis tekstas yra matomas?"

dpi = 300

def cm_to_px(cm):
  return int(cm / 2.54 * dpi)

width, height = (8.8, 4.4)

img = Image.new('RGB', (cm_to_px(width), cm_to_px(height)), (237,28,36))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("Palem3.2.05-nm.ttf", 18)
# Aiškus tekstas / Clear text
draw.text((0,0), text, (0,0,0), font=font)
img.save('Image-with-text.png', dpi=(dpi, dpi))

img = Image.new('RGB', (cm_to_px(width), cm_to_px(height)), (237,28,36))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("Palem3.2.05-nm.ttf", 18)
# Skirtumas per pikselį / Difference by pixel
draw.text((0,0), text, (236,29,35), font=font)
img.save('Image-with-text-2.png', dpi=(dpi, dpi))

img = Image.new('RGB', (cm_to_px(width), cm_to_px(height)), (237,28,36))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("Palem3.2.05-nm.ttf", 18)
# Blankus skirtumas / Blank difference
draw.text((0,0), text, (230,22,31), font=font)
img.save('Image-with-text-3.png', dpi=(dpi, dpi))
