# Python 3.5.2
# Author: Tyler Corum
# Purpose: The Tech Academy Python course drill 49 of 64
# Tested On: Written and tested to work with Win 7 x64


# _____Table Of Contents_____
# 1. Drill overview
# 2. Import
# 3. Class + Function defs
# 4. Database Manipulation
# /!\
# 5. Run time pass


# 1. Drill overview
# Creating a phone book database in python.  Using tkinter for the first time.


# 2. Import
import os
from tkinter import *
import tkinter as tk
import sqlite3

import phonebook_main
import phonebook_gui


# 3. Class + Function defs
def centerWindow(self, w, h): # pass in the tkinter frame (master) reference and teh w and h
	# get user's screen w and h
	screen_width = self.master.winfo_screenwidth()
	screen_height = self.master.winfo_screenheight()
	x = int((screen_width/2) - (w/2))
	y = int((screen_height/2) - (h/2))
	centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
	return centerGeo

#catch if user's click on upper X and ask are you sure?
def askQuit(self):
	if messagebox.askokcancel("Exit program", "Okay to exit application?"):
		#this closes app
		self.master.destroy()
		os._exit(0)

# 4. Database Manipulation
def create_db(self):
	conn = sqlite3.connect('phonebook.db')
	with conn:
		cur = conn.cursor()
		cur.execute("""CREATE TABLE if not exists tbl_phonebook 
			(ID INTEGER PRIMARY KEY AUTOINCREMENT, 
			col_fname TEXT,
			col_lname TEXT,
			col_fullname TEXT,
			col_phone TEXT,
			col_email TEXT);""")
		conn.commit()
	conn.close()
	first_run(self)

def first_run(self):
	data = ('John','Doe','John Doe','111-111-1111','jdoe@email.com')
	conn = sqlite3.connect('phonebook.db')
	with conn:
		cur = conn.cursor()
		cur,count = count_records(cur)
		if count < 1:
			cur.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""", data)
			conn.commit()
	conn.close()

def count_records(cur):
	count = ""
	cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
	count = cur.fetchone()[0]
	return cur,count

#select item in ListBox
def onSelect(self,event):
	#calling the event is the self.lstList1 widget
	varList = event.widget
	select = varList.curselection()[0]
	value = varList.get(select)
	conn = sqlite3.connect('phonebook.db')
	with conn:
		cursor = conn.cursor()
		cursor.execute("""SELECT col_fname,col_lname,col_phone,col_email FROM tbl_phonebook WHERE col_fullname = (?)""", [value])
		varBody = cursor.fetchall()
		for data in varBody:
			self.txt_fname.delete(0,END)
			self.txt_fname.insert(0,data[0])
			self.txt_lname.delete(0,END)
			self.txt_lname.insert(0,data[1])
			self.txt_phone.delete(0,END)
			self.txt_phone.insert(0,data[2])
			self.txt_email.delete(0,END)
			self.txt_email.insert(0,data[3])
	conn.close()

def addToList(self):
	var_fname = self.txt_fname.get()
	var_lname = self.txt_lname.get()
	# normalize the data to keep ti consistent in the dB
	var_fname = var_fname.strip() #rem any blank space b4/aft user entry
	var_lname = var_lname.strip() #ensure first char in each wrod is caps
	var_fname = var_fname.title()
	var_lname = var_lname.title()
	var_fullname = ("{} {}".format(var_fname,var_lname)) #combine normalized names into fullname
	print("var_fullname: {}".format(var_fullname))
	var_phone = self.txt_phone.get().strip()
	var_email = self.txt_email.get().strip()
	if not "@" or not "." in var_email: # not implemented yet, checks input ensures email address
		print("Incorrect email format!")
	if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0): #each field at least 1 char
		conn = sqlite3.connect('phonebook.db')
		with conn:
			cursor = conn.cursor()
			#check the dB for exist of fullname if so we will alert user and disregard req
			cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_fullname))
			count = cursor.fetchone()[0]
			chkName = count
			if chkName == 0: # if this is 0 then no exist of fullname and we can add new data
				print("chkName: {}".format(chkName))
				cursor.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""", (var_fname,var_lname,var_fullname,var_phone,var_email))
				self.lstList1.insert(END, var_fullname) # update listbox with new fullname
				conn.commit()
				onClear(self) #call function to clear all textboxes
			else:
				messagebox.showerror("Name Error","'{}' already exists in the dB! Please choose a different name.".format(var_fullname))
				onClear(self) #call function to clear all txtboxes
		conn.commit()
		conn.close()
	else:
		messagebox.showerror("Missing Text Error","Please ensure data is in all 4 fields.")

def onDelete(self):
	var_select = self.lstList1.get(self.lstList1.curselection())
	conn = sqlite3.connect('phonebook.db')
	with conn:
		cur = conn.cursor()
		#check count to ensure that this is not the last record in
		#the dB.  cannot delete last record or we will get an error
		cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
		count = cur.fetchone()[0]
		if count > 1:
			confirm = messagebox.askokcancel("Delete Confirmation", "All information associated with, ({}) \nwill be permanently deleted".format(var_select))
			if confirm:
				conn = sqlite3.connect('phonebook.db')
				with conn:
					cursor = conn.cursor()
					cursor.execute("""DELETE FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_select))
				onDeleted(self) #note DELETE*D*... call func to clear all textboxes and the selected index of listbox
				conn.commit()
		else:
			confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the dB and cannot be deleted at this time.")
	conn.close()

def onDeleted(self):
	#clear the text in these textboxes
	self.txt_fname.delete(0,END)
	self.txt_lname.delete(0,END)
	self.txt_phone.delete(0,END)
	self.txt_email.delete(0,END)
	try:
		index = self.lstList1.curselection()[0]
		self.lstList1.delete(index)
	except IndexError:
		psss

def onClear(self):
	# clear the text in these textboxes
	self.txt_fname.delete(0,END)
	self.txt_lname.delete(0,END)
	self.txt_phone.delete(0,END)
	self.txt_email.delete(0,END)

def onRefresh(self):
	# populate the listbox with names from dB
	self.lstList1.delete(0,END)
	conn = sqlite3.connect('phonebook.db')
	with conn:
		cur = conn.cursor()
		cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")  # /!\ removed. I had to add the ID because otherwise it wasn't counting??! int <> string
		count = cur.fetchone()[0]
		i = 0
		while i < count:
			cur.execute("""SELECT col_fullname FROM tbl_phonebook""")
			varList = cur.fetchall()[i]
			for item in varList:
				self.lstList1.insert(0,str(item))
				i += 1
	conn.close()

def onUpdate(self):
	try:
		var_select = self.lstList1.curselection()[0] # index of the list selection
		var_value = self.lstList1.get(var_select)
	except:
		messagebox.showinfo("Missing selection","No name was selected from the listbox. \nCancelling the update request.")
		return
	# the user will only be allowed to update changes to phone and email
	# for name changes the user will need to del and readd
	var_phone = self.txt_phone.get().strip() # normalize data entry
	var_email = self.txt_email.get().strip()
	if (len(var_phone) > 0) and (len(var_email) > 0): #ensure that there is SOME data
		conn = sqlite3.connect('phonebook.db')
		with conn:
			cur = conn.cursor()
			# count records to see if the user's changes are already in the database; meaning no update req
			cur.execute("""SELECT COUNT(col_phone) FROM tbl_phonebook WHERE col_phone = '{}'""".format(var_phone))
			count = cur.fetchone()[0]
			print(count)
			cur.execute("""SELECT COUNT(col_email) FROM tbl_phonebook WHERE col_email = '{}'""".format(var_email))
			count2 = cur.fetchone()[0]
			print(count2)
			if count == 0 or count2 == 0: # if proposed changes are not already in dB...
				response = messagebox.askokcancel("Update Request","The following changes ({}) and ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_phone,var_email,var_value))
				print(response)
				if response:
					with conn:
						cursor = conn.cursor()
						cursor.execute("""UPDATE tbl_phonebook SET col_phone = '{0}',col_email = '{1}' WHERE col_fullname = '{2}'""".format(var_phone,var_email,var_value))
						onClear(self)
						conn.commit()
				else:
					messagebox.showinfo("Cancel request","No changes have been made to ({}).".format(var_value))
			else:
				messagebox.showinfo("No changes detected","Both ({}) and ({}) \nalready exists in the dB for this name. \n\nYour request has been cancelled".format(var_phone, var_email))
			onClear(self)
		conn.close()
	else:
		messagebox.showerror("Missing information","Please select a name from the list.  \nThen edit the phone or email information.")
	onClear(self)


# 5. Run time pass
if __name__ == "__main__":
	pass





