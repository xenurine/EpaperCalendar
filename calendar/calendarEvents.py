#!/usr/bin/env python
from PIL import Image, ImageDraw, ImageFont
from datetime import timedelta, datetime
#import datetime
img = Image.new('RGB', (398,480), color = 'white')

#x = datetime.datetime.now()
x = datetime.now()
y = x + timedelta(days=10)
m = x + timedelta(days=5)

# set date range to show on cal
staDate = x.strftime("%m%d")
endDate = y.strftime("%m%d")
midDate = m.strftime("%m%d")

# font types / sizes
font30 = ImageFont.truetype('fonts/FreeSansBold.otf', 30)
font20 = ImageFont.truetype('fonts/FreeSans.ttf', 25)
fontB20 = ImageFont.truetype('fonts/FreeSansBold.otf', 25)
fontI20 = ImageFont.truetype('fonts/RemixIcon.ttf', 25)

# set current date
week = x.strftime("%A")
date = x.strftime("%-d")
month = x.strftime("%B")
monthNo = x.strftime("%m")

draw = ImageDraw.Draw(img)
draw.text((10,10), "Upcoming Events", font=font30,  fill="black")

# set event height
titleH = 75
subteH = 105

# load text file

with open('calendar.txt') as file:
  lines = [i.strip() for i in file]


# loop through the events
for x in lines:
	#print(x)
	# split the string up into usable data
	prYear, prMonth, prDate, prTime, prTitle, calType = x.split(",")

	#subTitle = 
	#Set current date for date range
	curDate = prMonth + prDate
	# generate the currend date of the week
	subDate = datetime(int(prYear), int(prMonth), int(prDate))
	subDay = subDate.strftime("%A")
	#Only display relevent data
	#if int(monthNo) <= int(prMonth) and int(date) <= int(prDate):
	if int(curDate) >= int(staDate) and int(curDate) <= int(endDate) :
        #draw text onto image
		if int(curDate) == int(staDate) :
			subTitle = "Today" + prTime
			print (subTitle)
		elif int(curDate) == int(staDate) + 1 :
			subTitle = "Tomorrow" + prTime
		elif int(curDate) > int(staDate) and int(curDate) < int(midDate) :
			subTitle = "This " + subDay + prTime
			print (subTitle)
		else :
			subTitle = "Next " + subDay + prTime
			print (subTitle)



		print(x)
		print(endDate)
		print(calType)
		if calType == " Event" :
			draw.text((15,titleH), "ɐ", font=fontI20,  fill="black")
		elif calType == " Birthday" :
			draw.text((15,titleH), "ɑ", font=fontI20,  fill="black")
		elif calType == " Star" :
			draw.text((15,titleH), "ɓ", font=fontI20, fill="black")
		elif calType == " Holiday" :
			draw.text((15,titleH), "ɒ", font=fontI20,  fill="black")
		elif calType == " BnkHol" :
			draw.text((15,titleH), "ɔ", font=fontI20,  fill="black")
		draw.text((45,titleH), prTitle, font=fontB20,  fill="black")
		draw.text((10,subteH), subTitle, font=font20,  fill="black")

		# set new draw hight
		titleH = titleH + 80
		subteH = subteH + 80

	# break loop when program runs out of space on image
	if titleH > 460:
		break


img.save("main.png", "PNG")

