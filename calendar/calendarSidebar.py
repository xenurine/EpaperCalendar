#!/usr/bin/env python
from PIL import Image, ImageDraw, ImageFont
import datetime

W, H = (250,480)

x = datetime.datetime.now()

# font types / sizes
font30 = ImageFont.truetype('fonts/FreeSans.ttf', 30)
font40 = ImageFont.truetype('fonts/FreeSans.ttf', 40)
font90 = ImageFont.truetype('fonts/FreeSansBold.otf', 99)

# set current date
week = x.strftime("%A")
date = x.strftime("%-d")
month = x.strftime("%B")

im = Image.open('cal.png')
#im = Image.new("RGBA",(W,H),"white")
draw = ImageDraw.Draw(im)
Ww = draw.textlength(week, font=font40)
draw.text(((W-Ww)/2,10), week, font=font40,  fill="black")
Dw = draw.textlength(date, font=font90)
draw.text(((W-Dw)/2,50), date, font=font90,  fill="black")
Mw = draw.textlength(month, font=font30)
draw.text(((W-Mw)/2,160), month, font=font30,  fill="black")
im.save("sidebar.png", "PNG")

