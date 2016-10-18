# Python 3.5.2 IDLE x86/32-bit
# Author: Tyler Corum, 10/17/2016
# Purpose: Design a program that allows a user to choose a directory to copy and a destination directory to copy to.  This checks any files created in the last 24 hours.  After the first run, store a timestamp for when the file transfer was ran inside a database.  The next time the transfer app is ran, display that timestamp.  This time, if it has been more than 24 hours since last file transfer, allow it up until the last time the file transfer ran.
#
# Tested On: Windows 7 x64


# ____________________Table Of Contents____________________
#
# 1. Learning and Resources
# 2. Import and Var Decs
# 3. Processing
#
# 999. TESTING
#
# /$\ # urgent and important
# /!\ # important
# /#\ # important but not ugent
# /?\ # error?/unknown?


# 1. Learning and Resources
# ---------------------
# 	http://tkinter.unpythonic.net/wiki/tkFileDialog
#	https://www.draw.io/#G0Bw6ibnXqghl4ZGVrRnB6c05RV2c


# 2. Import and Var Decs
# ----------------------
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import shutil
import os
import time
import math
import datetime
import pdb
import sqlite3
global timeStampLastRan
global sinceLastRan



# 3. Processing
# -------------
conn = sqlite3.connect('lastTransfer.db')
c = conn.cursor()


class Gui:
	def __init__(self, master):
		self.master = master
		self.master.title('For Your Automation | TEC10101')
		self.master.configure(bg="#F0F0F0")
		self.master.maxsize(600,200)
		self.master.minsize(600,200)

		# defining source/destination
		self.source = StringVar()
		self.destination = StringVar()

		# gui labels
		self.label_FT = tk.Label(self.master,text='File Transfer')
		self.label_FT.grid(row=0,column=0,columnspan=2,padx=(27,0),pady=(10,0))
		self.label_FT.config(font = ('Courier', 18, 'bold'))

		# the words "Last Ran:"
		self.label_lastRan = tk.Label(self.master,text='Last Ran:')
		self.label_lastRan.grid(row=0,column=2,columnspan=1,padx=(27,0),pady=(10,0),sticky=W)

		# prints the timestamp pulled from the db
		self.label_lastRanTimeStamp = tk.Label(self.master,text=timeStampLastRan[1])
		self.label_lastRanTimeStamp.grid(row=0,column=3,columnspan=3,padx=(27,0),pady=(10,0),sticky=E)
		# self.label_defaults = tk.Label(self.master,text='Defaults Prefilled')
		# self.label_defaults.grid(row=1,column=0,columnspan=1,padx=(27,0),pady=(10,0))
		self.label_clickBrowse = tk.Label(self.master,text='Click Browse To Choose Alternative Folders')
		self.label_clickBrowse.grid(row=1,column=1,columnspan=2,padx=(27,0),pady=(10,0),sticky=W)
		self.label_from = tk.Label(self.master,text='From:')
		self.label_from.grid(row=3,column=0,columnspan=1,padx=(27,0),pady=(10,0),sticky=E)
		self.label_to = tk.Label(self.master,text='To:')
		self.label_to.grid(row=6,column=0,columnspan=1,padx=(27,0),pady=(10,0),sticky=E)

		# browse buttons
		self.browseFromDir = ttk.Button(self.master,text='Browse',command=lambda: self.source.set(filedialog.askdirectory(parent=self.master, initialdir=self.source, title='Choose Dir You Want To Copy FROM')))
		self.browseFromDir.grid(row=3,column=3)
		self.browseToDir = ttk.Button(self.master,text='Browse',command=lambda: self.destination.set(filedialog.askdirectory(parent=self.master, initialdir=self.destination, title='Choose Dir You Are Copying TO')))
		self.browseToDir.grid(row=6,column=3)

		# from/to directory location labels
		self.chosenFromDir = tk.Label(self.master,textvariable=self.source)
		self.chosenFromDir.grid(row=3,column=1,columnspan=2,padx=(27,0),pady=(10,0),sticky=W)
		self.chosenToDir = tk.Label(self.master,textvariable=self.destination)
		self.chosenToDir.grid(row=6,column=1,columnspan=2,padx=(27,0),pady=(10,0),sticky=W)

		# transfer/launch button
		self.launchButton = ttk.Button(self.master,text='>> Transfer Now >>', command=lambda: transfer_last_24(self.source.get(),self.destination.get()))
		self.launchButton.grid(row=7,column=2,columnspan=2,padx=(27,0),pady=(10,0),sticky=W)

		#optional/advanced options:
		# self.checkbutton_txt = ttk.Checkbutton(self.master, text='.txt?')
		# self.checkbutton_txt.grid(row=8,column=0,sticky=W)
		# self.checkbutton_bmp = ttk.Checkbutton(self.master, text='.bmp?')
		# self.checkbutton_bmp.grid(row=8,column=1,sticky=E)
		# self.checkbutton_all = ttk.Checkbutton(self.master, text='*.ALL FILES?')
		# self.checkbutton_all.grid(row=8,column=2,sticky=W)
		# self.

def transfer_last_24(source, destination):
	
	unixUTC = math.ceil(time.time())
	date = str(datetime.datetime.fromtimestamp(unixUTC).strftime('%Y-%m-%d %H:%M:%S'))
	c.execute("CREATE TABLE IF NOT EXISTS tbl_lastTransfer(unix REAL, datestamp TEXT)")
	files = os.listdir(source)
	source = source + '/'
	destination = destination + '/'
	count = 0
	for file in files:
		strLength = len(file)
		
		fileNameDisplay = file
		if strLength > 14:
			# truncate = (len(file)-14)
			fileNameDisplay = file[-12:]
		if file.endswith('.txt'):
			timestamp = os.lstat(source + file).st_mtime
			if timestamp >= timeStampLastRan[0]:
				# print('{}\'s last-modified timestamp: {}.  Difference between timestamp and NOW: {}'.format(file,timestamp, unixUTC - timestamp))
				shutil.copyfile(source + file, destination + file)
				shutil.copystat(source + file, destination + file)

				# copy success, copystat success as well, count
				print('{:.>14.12}\t copied to: {:.>35.32}{}\t{}'.format(fileNameDisplay,destination[-32:],file))
				count += 1
			elif timestamp < timeStampLastRan[0]:
				print('{:.>14.12}\t not copied.  Only includes files since last run.\ttimestamp: {}'.format(fileNameDisplay))
		else:
			print('{:.>14.12}\t not copied.  File not *.txt format.\ttimestamp: {}'.format(fileNameDisplay))
	if count == 0:
		print('\nNo files copied, retaining previous timestamp of completion.')
	elif count > 0:
		c.execute("DELETE FROM tbl_lastTransfer")
		c.execute("INSERT INTO tbl_lastTransfer (unix, datestamp) VALUES (?,?)", (unixUTC, date))
		conn.commit()
		c.close()
	return


root = Tk()
# pdb.set_trace()
c.execute("SELECT unix, datestamp FROM tbl_lastTransfer")
timeStampLastRan = c.fetchone()
my_gui = Gui(root)
root.mainloop()












# 999. TESTING
