# Python 3.5.2 IDLE x86/32-bit
# Author: Tyler Corum, 10/13/2016
# Purpose: Practice with Unix time.
#
# Tested On: Windows 7 x64


# ____________________Table Of Contents____________________
#
# 1. Introduction to the program
# 2. Import and Functions
# 3. Commented out notes 
# 4. Processing
#
# 999. TESTING
#
# /$\ # urgent and important
# /!\ # important
# /#\ # important but not ugent
# /?\ # error?/unknown?


# 1. Introduction to the problem
# ------------------------------
# 	Scenario: The company you work for just opened two new branches. One is in New York City,
# the other in London. They need a very simple program to find out if the branches are open or
# closed based on the current time of the Headquarters here in Portland. The hours of both
# branches are 9:00AM - 9:00PM in their own time zone.


# 2. Import and Functions
# -----------------------
import time
import datetime
import math
import pdb

def time_now():
	# pdb.set_trace()
	unix = math.ceil(time.time())
	date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))

	print('unix time: {}\nconverted time: {}'.format(unix, date))

	timeNowLondonSec = (unix + 3600) % 86400 # london is -1 GMT right now
	timeNowNYCSec = (unix - (3600 * 4)) % 86400
	timeNowPDXSec = (unix - (3600 * 7)) % 86400
	if timeNowNYCSec == 0:
		timeNowNYCSec = 86400
	if timeNowLondonSec == 0:
		timeNowLondonSec = 86400
	time_now_lon(timeNowLondonSec)
	time_now_nyc(timeNowNYCSec)
	return
	
def time_now_lon(timeNowLondonSec):
	timeNowLonHoursPastMidnight = math.floor(timeNowLondonSec / 3600)
	remainingMinutesLon = math.floor((timeNowLondonSec % 3600) / 60)
	londonAMPM = "AM"

	if timeNowLonHoursPastMidnight > 12 and timeNowLonHoursPastMidnight < 24:
		timeNowLonHoursPastMidnight = timeNowLonHoursPastMidnight - 12
		londonAMPM = "PM"
	elif timeNowLonHoursPastMidnight >= 24:
		timeNowLonHoursPastMidnight = timeNowLonHoursPastMidnight - 12

	if timeNowLondonSec > 75600 or timeNowLondonSec < 32400:
		print('London Branch Closed.  Time there is: {:2d}:{:02d}{}'.format(timeNowLonHoursPastMidnight,remainingMinutesLon,londonAMPM))
	else:
		print('London Branch Open.  Time there is: {:2d}:{:02d}{}'.format(timeNowLonHoursPastMidnight,remainingMinutesLon,londonAMPM))
	return

def time_now_nyc(timeNowNYCSec):
	# pdb.set_trace()
	timeNowNYCHoursPastMidnight = math.floor(timeNowNYCSec / 3600)
	remainingMinutesNYC = math.floor((timeNowNYCSec % 3600) / 60)
	NYCAMPM = "AM"

	if timeNowNYCHoursPastMidnight > 12 and timeNowNYCHoursPastMidnight < 24:
		timeNowNYCHoursPastMidnight = timeNowNYCHoursPastMidnight - 12
		NYCAMPM = "PM"
	elif timeNowNYCHoursPastMidnight >= 24:
		timeNowNYCHoursPastMidnight = timeNowNYCHoursPastMidnight - 12

	if timeNowNYCSec > 75600 or timeNowNYCSec < 32400:
		print('NYC Branch Closed.  Time there is: {:2d}:{:02d}{}'.format(timeNowNYCHoursPastMidnight, remainingMinutesNYC,NYCAMPM))
	else:
		print('NYC Branch Open.  Time there is: {:2d}:{:02d}{}'.format(timeNowNYCHoursPastMidnight, remainingMinutesNYC,NYCAMPM))
	return

def debug_time():
	unix = math.ceil(time.time())
	date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))

	print('\n\n********DEBUGGGGGGGGGG**********\nunix time: {}\nconverted time: {}'.format(unix, date))
	for i in range(0,25):
		debugInput = i
		daySplit = (3600 * debugInput) # the remainder is how many seconds after 00:00, the start of the day
		timeNowLondonSec = (daySplit + 3600) % 86400 # london is -1 GMT right now
		timeNowNYCSec = (daySplit - (3600 * 4)) % 86400
		timeNowPDXSec = (daySplit - (3600 * 7)) % 86400
		if timeNowNYCSec == 0:
			timeNowNYCSec = 86400
		if timeNowLondonSec == 0:
			timeNowLondonSec = 86400
		time_now_lon(timeNowLondonSec)
		time_now_nyc(timeNowNYCSec)
	

	# time_now_lon(timeNowLondonSec)
	# time_now_nyc(timeNowNYCSec)


# 3. Commented out notes 
# ----------------------
# NYC = +3 hours.  3 * 60 = how many minutes * 60 = how many +s ahead == +10800.

# 10/13/2016 == 1476316800
# 10/14/2016 == 1476403200
# 24 hours == 86400 s per day.
# /24 = 3600s per hour
# 9am 10/13 = 1476349200

# daySplit is set to how many seconds into the day it is in UTC.  
# London = daySplit + 3600
# NYC = daySplit - (3600 * 4)
# Portland = daySplit - (3600 * 7)

# 10/13/2016 @ 12PM = 1476316800 + (86400 * 12)

# 9PM = how many seconds into the day? 21 hours, so 3600*21 = 75600
# 9AM = 9 * 3600 = 32400

# floor(timenow / 3600) = how many hours in
# timenow % 3600 = how many seconds after that many hours in


# 4. Processing
# -------------
time_now()
debug_time()


# 999. TESTING
# ------------
