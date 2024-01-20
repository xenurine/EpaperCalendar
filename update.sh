#!/bin/bash
cd calendar/src
echo "Downloading Calender"
wget !!DOWNLOAD LINK TO CALENDAR!!
## Rename File
cp *export calendar.ics
rm *export
cd ..
echo "Converting calendar"
python3 convert-Cal.py
echo "Pulling data"
python3 pullData.py
echo "Updating Events"
python3 calendarEvents.py
echo "Creating Calender"
python3 calendarDate.py
echo "Creating Sidebar"
python3 calendarSidebar.py
echo "Generating calendar file"
python3 generate.py
echo "Pushing to Screen"
python3 ePaper.py

