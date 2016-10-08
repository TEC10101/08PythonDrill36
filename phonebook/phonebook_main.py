# Python        3.5.2
#
# Author:       Tyler Corum
#
# Purpose:      The Tech Academy Python course drill 49 of 64
#
# Tested On:    Written and tested to work with Win 7 x64
#
#
# _____Table Of Contents_____
# 1. Drill overview
# 2. Import
# 3. Class + Function defs
# 4. 
# /!\ # just grab <- unknown syntax/logistical error!


# 1. Drill overview
# Creating a phone book database in python.  Using tkinter for the first time.


# 2. Import
from tkinter import *
import tkinter as tk

import phonebook_gui # this is the name dan used for his gui file
import phonebook_func # the name dan used for functions in the code


# 3. Class + Function defs
# Frame is the Tkinter frame class that our own class will inherit from
class parentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500,300) # (width, height) / (x, y)
        self.master.maxsize(500,300)
        #this centerwindow method will center our app on the user's screen
        phonebook_func.centerWindow(self,500,300)
        self.master.title("The Tkinter Phonebook Demo - Tyler Wuz Here")
        self.master.configure(bg="#F0F0F0")
        # this protocol method is a tkinter built in method to catch
        # if the user clicks the upper corner "X" in Windows OS
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.askQuit(self))
        

# /!\ the next line arg = self.master was erased without explaination /!\ ##
        arg = self.master
        # load in the GUI widgets from a sep module,
        # keeping code compartmentalized and clutter free
        phonebook_gui.loadGui(self)

if __name__ == "__main__":
    root = tk.Tk()
    App = parentWindow(root)
    root.mainloop()  # <-- this keeps the window persistent on the screen!