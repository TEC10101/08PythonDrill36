# Python 3.5.2 IDLE x86/32-bit
# Author: Tyler Corum, 10/14/2016
# Purpose: Design a program that allows a user to choose a directory to copy and a destination directory to copy to.
#
# Tested On: Windows 7 x64


# ____________________Table Of Contents____________________
#
# 1. Import and functions
# 2. Processing
#
# 999. TESTING
#
# /$\ # urgent and important
# /!\ # important
# /#\ # important but not ugent
# /?\ # error?/unknown?


# 1. Import and functions
# ---------
import shutil
import os
import time
import math
import datetime
from tkinter import *
from tkinter import ttk
import pdb

def last_24(unixUTC, source, destination):
	files = os.listdir(source)
	
	for file in files:
		strLength = len(file)
		
		# pdb.set_trace()
		fileNameDisplay = file
		if strLength > 12:
			# truncate = (len(file)-14)
			fileNameDisplay = file[-12:]
		if file.endswith('.txt'):
			timestamp = os.lstat(source + file).st_mtime
			if timestamp >= unixUTC - 86400:
				# print('{}\'s last-modified timestamp: {}.  Difference between timestamp and NOW: {}'.format(file,timestamp, unixUTC - timestamp))
				shutil.copy(source+file, destination, follow_symlinks=False)
				shutil.copystat(source + file, destination + file, follow_symlinks=False)
				# copy success, copystat success as well
				print('{:.>14.12}\t copied to: {:.>35.32}{}'.format(fileNameDisplay,destination[-32:],file,))
			elif timestamp < unixUTC - 86400:
				print('{:.>14.12}\t not copied.  File older than 24 hours.'.format(fileNameDisplay))
		else:
			print('{:.>14.12}\t not copied.  File not *.txt format.'.format(fileNameDisplay))
	return


# 2. Processing
# -------------
# pdb.set_trace()

unixUTC = math.ceil(time.time())
source = 'C:\\Projects\\Python\\pythonDrills\\moveFolder2\\Folder_A\\'
destination = 'C:\\Projects\\Python\\pythonDrills\\moveFolder2\\destination\\'

last_24(unixUTC, source, destination)







# # 999. TESTING
