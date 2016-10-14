# Python 3.5.2 IDLE x86/32-bit
# Author: Tyler Corum, 10/14/2016
# Purpose: Move files from last 24 hours into a new folder called "destination"
#
# Tested On: Windows 7 x64


# ____________________Table Of Contents____________________
#
# 1. Import
# 2. Processing
#
# 999. TESTING
#
# /$\ # urgent and important
# /!\ # important
# /#\ # important but not ugent
# /?\ # error?/unknown?


# 1. Import
# ---------
import shutil
import os
import time
import math
import datetime
# import pdb


def last_24(unixUTC):
	source = 'C:\\Projects\\Python\\pythonDrills\\moveFolder2\\Folder_A\\'
	destination = 'C:\\Projects\\Python\\pythonDrills\\moveFolder2\\destination\\'

	files = os.listdir(source)
	
	for file in files:
		if file.endswith('.txt'):
			timestamp = os.lstat(source + file).st_mtime
			if timestamp >= unixUTC - 86400:
				print('{}\'s timestamp: {}.  Difference between timestamp and NOW: {}'.format(file,timestamp, unixUTC - timestamp))
				shutil.copy(source+file, destination)
				shutil.copystat(source + file, destination + file)
				# copy success, copystat success as well
				print('{} copied to:\t{}{}\ncopystat: {}\n'.format(file,destination,file,shutil.copystat(source + file, destination)))
		# else:
		# 	print('{}\tnot moved'.format(file))
	return

def time_now():
	# pdb.set_trace()
	unixUTC = math.ceil(time.time())
	date = str(datetime.datetime.fromtimestamp(unixUTC).strftime('%Y-%m-%d %H:%M:%S'))

	print('unix timestamp right NOW: {}\nconverted into time: {}'.format(unixUTC, date))

	last_24(unixUTC)
	return

time_now()

# 2. Processing
# -------------
# pdb.set_trace()












# # 999. TESTING


# for file in files:
# 	if file.endswith('.txt'):
# 		timestamp = os.lstat().st_mtime
# 		print('{}\tmoved to {}{}\n\ntimestamp: {}'.format(file,destination,file,timestamp))
# 		shutil.copystat(source + file, destination)



# t1 = os.lstat('test.txt').st_mtime

# shutil.copystat
