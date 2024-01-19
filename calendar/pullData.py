#!/usr/bin/env python
from datetime import timedelta, datetime
#import datetime

#=========================#
# Pull Data from Sources  #
#=========================#

# === Functions === #

# This funcation Pulls Data from the diffrent text files 
def convertText(dataSource, data, currentArr):

	for x in dataSource: 

		## date Time stuff ##

		date = datetime.now()
		crYear = date.strftime("%Y")

		prYear, prMonth, prDate, prSrTm, prEnTm, prTitle = x.split(",")


		#check to see time string is populated (if so display at & -)
		if(len(prSrTm) == 0):
			StTime = ""
		else :
			StTime = " at" + prSrTm
		if(len(prEnTm) == 0):
			EnTime = ""
		else :
			EnTime = " -" + prEnTm

		## add some checks to make the year change for nextyear
		# Replace 0000 with current year
		if(prYear=="0000"): 
			prYear = crYear

		# combine the data to the new fomat
		csvData = prYear + "," + prMonth + "," + prDate + "," + StTime + EnTime + "," + prTitle + "," + data

		#store data in a array (using append)
		currentArr.append(csvData)

	return currentArr
	#for x in csvEventArr:
	#	print(x)

# === main code === # 

fileOut = open('calendar.txt', 'w')

with open('src/Event.txt') as file:
  calEvent = [i.strip() for i in file]

with open('src/Birthday.txt') as file:
  calBirthday = [i.strip() for i in file]

with open('src/BnkHol.txt') as file:
  calBnkHol = [i.strip() for i in file]

with open('src/Star.txt') as file:
  calStar = [i.strip() for i in file]

with open('src/Holiday.txt') as file:
  calHoliday = [i.strip() for i in file]

# Declare Array for the calenders 
csvCallArr = []

# Get data from Event cal File
csvCallArr = convertText(calEvent, " Event", csvCallArr )

# Get data from Birthday Cal File
csvCallArr = convertText(calBirthday, " Birthday", csvCallArr )

# Get data from Event cal File
csvCallArr = convertText(calBnkHol, " BnkHol", csvCallArr )

# Get data from Event cal File
csvCallArr = convertText(calStar, " Star", csvCallArr )

# Get data from Event cal File
csvCallArr = convertText(calHoliday, " Holiday", csvCallArr )

sorted_rows = sorted(csvCallArr);


for x in sorted_rows:
		print(x)
		fileOut.writelines(x + "\n")

fileOut.close()
	#print(csvData)

#[DEBUG: Print Output]
#for x in myArr:
#	print(x)



