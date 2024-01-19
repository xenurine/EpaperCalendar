from PIL import Image, ImageDraw, ImageFont
import datetime
from datetime import date
from calendar import monthrange 

import calendar

w, h = 250, 480

font10 = ImageFont.truetype('fonts/FreeSansBold.ttf', 11)
#font10 = ImageFont.truetype('fonts/MetropolisBold.ttf', 10)
font15 = ImageFont.truetype('fonts/MetropolisBold.ttf', 15)

img = Image.new("RGB",(w,h), (255,255,255))
draw = ImageDraw.Draw(img)

boarder = 9
h_start= int(h/2)
h_end = int(h-boarder)
w_start = boarder
w_end = w-boarder
stepsizeV = int((w-2*boarder)/7)
stepsizeH = int((h_start-boarder)/5)

#draw.rectangle((10,h_start,w-10,h_end),outline=1,width=5,)
cols=[]
rows=[]
days = { 0:'Sun', 1:'Mon', 2:'Tue', 3:'Wed', 4:'Thu', 5:'Fri', 6:'Sat'}
i=0
for x in range (boarder,w,stepsizeV):
    #line = ((x,h_start),(x,h_end))
   # draw.line(line,fill=1,width=3)
    cols.append(x+stepsizeV/2)
    if i<7:
        draw.text((x+stepsizeV/2 -10, h_start-stepsizeV/2), days[i], font=font10,  fill=(0,0,0))
        i+=1

for x in range (h_start,h,stepsizeH):
    line = ((w_start,x),(w_end,x))
    ####draw.line(line,fill=100, width=3)
    rows.append(x+stepsizeH/2)

Curdate = date.today() 
date =int(Curdate.strftime('%d'))
month = int(Curdate.strftime('%m'))
year = int(Curdate.strftime('%y'))

monthlen = calendar.monthrange(year,month)

k = monthlen[0] + 1
i=1
j=0
r = rows[j]
while i<= monthlen[1]:
    c = cols[k]
    if date == i:
        print("good!")
        cx = c + 25
        rx = r + 25
        cy = c - 7
        ry = r - 7
        draw.ellipse((cy, ry, cx, rx), fill=(0, 0, 0), outline=(0, 0, 0))
        draw.text((c,r), str(i), font=font15, fill=(255,255,255))
    else:
        print(str(i), "/", date, "/", i )
        draw.text((c,r), str(i), font=font15, fill=(0,0,0))
    i+=1
    k = (k+1)%7
    if not k:
        j+=1
        r = rows[j]
img.save('cal.png')
