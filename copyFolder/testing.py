# Python 3.5.2 IDLE x86/32-bit
# Author: Tyler Corum, 10/14/2016
# Purpose: Design a program that allows a user to choose a directory to copy and a destination directory to copy to.
#
# Tested On: Windows 7 x64


# ____________________Table Of Contents____________________
#
# 1. Learning Resources
# 2. Import and Var Decs
# 3. Processing
#
# 999. TESTING
#
# /$\ # urgent and important
# /!\ # important
# /#\ # important but not ugent
# /?\ # error?/unknown?


# 1. Learning Resources
# ---------------------
# 	http://tkinter.unpythonic.net/wiki/tkFileDialog


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



# 3. Processing
# -------------



class Gui:

	def __init__(self, master):
		self.master = master
		self.master.title('For Your Automation | TEC10101')
		self.master.configure(bg="#F0F0F0")
		self.master.maxsize(550,200)
		self.master.minsize(550,200)

		# defining source/destination
		self.source = StringVar()
		self.destination = StringVar()

		# gui labels
		self.label_FT = tk.Label(self.master,text='File Transfer')
		self.label_FT.grid(row=0,column=0,columnspan=2,padx=(27,0),pady=(10,0))
		self.label_FT.config(font = ('Courier', 18, 'bold'))
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
		pdb.set_trace()

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
	files = os.listdir(source)
	unixUTC = math.ceil(time.time())
	source = source + '/'
	destination = destination + '/'
	
	for file in files:
		strLength = len(file)
		
		fileNameDisplay = file
		if strLength > 12:
			# truncate = (len(file)-14)
			fileNameDisplay = file[-12:]
		if file.endswith('.txt'):
			timestamp = os.lstat(source + file).st_mtime
			if timestamp >= unixUTC - 86400:
				# print('{}\'s last-modified timestamp: {}.  Difference between timestamp and NOW: {}'.format(file,timestamp, unixUTC - timestamp))
				shutil.copyfile(source + file, destination + file)
				shutil.copystat(source + file, destination + file)

				# copy success, copystat success as well
				print('{:.>14.12}\t copied to: {:.>35.32}{}'.format(fileNameDisplay,destination[-32:],file,))
			elif timestamp < unixUTC - 86400:
				print('{:.>14.12}\t not copied.  File older than 24 hours.'.format(fileNameDisplay))
		else:
			print('{:.>14.12}\t not copied.  File not *.txt format.'.format(fileNameDisplay))
	return




root = Tk()
my_gui = Gui(root)
# transfer_last_24(my_gui.source,my_gui.destination)




root.mainloop()












# 999. TESTING
# checkAdv = StringVar()
# checkAdv.set('disabled')

# notebook = ttk.Notebook(root)
# notebook.pack()

# default = ttk.Frame(notebook)
# options = ttk.Frame(notebook)
# notebook.add(default, text = 'File Transfer')
# notebook.add(options, text = 'Adv Options')



# checkbutton = ttk.Checkbutton(default, text = 'Show Advanced Options')
# checkbutton.pack()

# # if checkAdv.get() == 0:
# notebook.tab(1, state = checkAdv)


# checkbutton.config(variable = checkAdv, onvalue = 'normal', offvalue = 'disabled')



# transferButton = ttk.Button(default, text = 'Transfer Now -->')
# transferButton.pack()



# checkbutton.config(textvariable = breakfast)









# if len(tempdir) > 0:
#     print "You chose %s" % tempdir
