from icalendar import Calendar

from datetime import datetime

fileOut = open('src/Event.txt', 'w')

with open('src/calendar.ics', 'rb') as i:
	cal = Calendar.from_ical(i.read())

	for event in cal.walk('vevent'):
		description = event.get('description')
		date = event.decoded('dtstamp')
		summery = event.get('SUMMARY')
		start = event.decoded('DTSTART')
		end = event.decoded('DTEND')

		# -= Start Date & Time =- #
		# = Date = #
		stYear = start.strftime('%Y')
		stMonth = start.strftime('%m')
		stDay = start.strftime('%d')

		# -= Time =- #
		stTime = start.strftime('%H:%M')

		# -= End Date & Time =- #
		# = Time = #
		edTime = end.strftime('%H:%M')

		#stYear, stMonth, stDay = start.split("-")

		output = stYear + "," + stMonth + "," + stDay + ", " + stTime + ", " + edTime + ", " + summery
		print (output)

		fileOut.writelines(output + "\n")




		


