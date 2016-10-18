# Python 3.5.2 IDLE x86/32-bit
# Author: Tyler Corum, 10/11/2016
# Purpose: Move files from Folder A to Folder B and print the directory to the screen.
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
# import pdb


# 2. Processing
# -------------
# pdb.set_trace()

source = 'C:\\Projects\\Python\\pythonDrills\\moveFolder\\Folder_A\\'
destination = 'C:\\Projects\\Python\\pythonDrills\\moveFolder\\Folder_B\\'

files = os.listdir(source)

for file in files:
	if file.endswith('.txt'):
		print('{}\tmoved to {}{}'.format(file,destination,file))
		shutil.move(source + file, destination)
	else:
		print('{}\tnot moved'.format(file))
