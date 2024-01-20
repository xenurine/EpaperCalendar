# E-Paper Calendar 
This project is for a 5.83" (648x480) inch display. 

## About This Project

This project displays a monthly calender with 5 upcoming events, pulled form a ics file.   
This is still in early development, so is not practically well written or efficient. My main aim is to get all the core features working before writing better code. 

## How it works

This project is written in python using Pillow. The program generates an image file, which is then pushed to the display. 

My setup uses a Waveshare 5.83 E-Ink Display (648x480) Connected to a raspbery Pi Zero. At midnight i have a secdulaed task to run the code so it updates the calender to the next day. 

ain an event which is formated like a csv file. 

For Event.txt the program generates this form a ICS file (working on a way to get this from a remote server) 

## Setup 

For setup you need to install the appropiate software for your epaper display. After this install the following. 

- Python3
  - pillow
  - icalender
 
 (Under Development - More coming soon ) 
