# Python 3.5.2
# Author: Tyler Corum
# Purpose: The Tech Academy Python course drill 52 of 64
#		   Lynda.com course on tkinter and themed tkinter (ttk)
# Tested On: 


# ____________________Table Of Contents____________________
# 1. Basics, tkinter import, and ttk
# 2. Widgets, Geometry manager, and Event handling notes
# 3. Chapter 2 exercise, def a class and methods to change text on button click
# 4. Chapter 3 exercise, using label widget to display text
# 	4.a ch03/01_label.py
# 	4.b ch03/02_button.py
# 	4.c ch03/03_selection_buttons.py
# 	4.d ch03/04_entry.py
# 	4.e ch03/05_selection_boxes.py
# 	4.f ch03/06_progressbar_scale.py
# 5. Chapter 4 exercise, frames and organizational widgets
# 	5.a ch04/01_frame.py
# 	5.b ch04/02_toplevel.py
# 	5.c ch04/03_panedwindow.py
# 	5.d ch04/04_notebook.py
#
# 666. TESTING
#
# /$\ # urgent and important
# /!\ # important
# /;\ # urgency implied but not important
# /?\ # error?/unknown?



# 1. Basics, tkinter import, and ttk
# from tkinter import *
# from tkinter import ttk

# root = Tk()
# button = ttk.Button(root, text = 'Click Me')
# button.pack()
# button['text']
# button['text'] = 'Press Me'
# button.config(text = 'Push Me')
# button.config() # diction of all properties for widget "button"
# str(button) # gives the ID of the widget randomly generated
# str(root) # shows root as '.'
# ttk.Label(root, text = 'Hello, Tkinter!').pack() # no reference


# 2. Widgets, Geometry manager, and Event handling notes
# ------------------------------------------------------
# master / slave widgets.  parent class widget is master.
# pack geometry manager
# define edge of parent to pack widget master
# 
# grid geometry manager = 2D table / row/column
#
# place geometry manager / relative or abs x/y coord
# ^ can get cumbersome with lots
#
# can use many diff geo mgrs
#
# handling user events		# 
# when event occurs:		# execute handler code
# <ButtonPress>				# handle_buttonpress()
# <Key>						# handle_key()
# <Leave>					# handle_leave()
# <Motion>					# handle_motion()
# <Configure>				# handle_configure()

# when you call root.mainloop()
# you enter "Event Loop"
# Event -> appropriate handler code -> returns and waits for Event
# do not handle multiple events at same time
# handler code short/quick

# configuring event handlers
# command callbacks:
#	avail for interactive widgets
# event binding
#	used for events taht do not have a command callback
# 	similar to AHK rebinding :)


# 3. Chapter 2 exercise, def a class and methods to change text on button click
# -----------------------------------------------------------------------------
# ch02/05_hello_local.py


# 4. Chapter 3 exercise, using label widget to display text
# ---------------------------------------------------------
# 	4.a ch03/01_label.py
#	one of the easiest ways to get data to the user is with label
# 
# from tkinter import *
# from tkinter import ttk

# root = Tk()
# label = ttk.Label(root, text = 'Hello, Tkinter!') # constructor method is capitalized
# label.pack() #pack geo mgr
# label.config(text = 'Howdy, Tkinter@')
# label.config(wraplength = 150) #wrap text at 150px.  default justify left
# label.config(justify = CENTER)
# label.config(foreground = 'blue', background = 'yellow')
# label.config(font = ('Courier', 18, 'bold'))

# label.config(text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmodtempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodoconsequat. Duis aute irure dolor in reprehenderit in voluptate velit essecillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat nonproident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
# logo = PhotoImage(file = 'C:\\Projects\\Python\\pythonDrills\\lynda_tkinter\\Exercise Files\\Ch03\\python_logo.gif') # \escape and then \ dir separator
# label.config(image = logo)
# label.config(compound = 'text')
# label.config(compound = 'center')
# label.config(compound = 'left')
# # /!\ # images and other objects/variables get garbage collected if scope is lost.  You should always store the image in an area that won't be garbage collected:
# label.img = logo
# label.config(image = label.img)
# ^ prevent accidental memory leaks


# 	4.b ch03/02_button.py
#	simplest way to have user do things with program.
# from tkinter import *
# from tkinter import ttk

# root = Tk()
# button = ttk.Button(root, text = 'Click Me') #using ttk gives theme of OS, can use older tkinter
# button.pack()
# def callback():
# 	print('Clicked!')

# button.config(command = callback)

# button.invoke() # we can programmatically siumulate button click
# # objects have states
# button.state(['disabled'])
# button.instate(['disabled']) #asking question "is my button in this state, defined as 'disabled'"
# button.state(['!disabled']) # ! == not
# button.instate(['!disabled']) # ask is my button not in disabled state?
# # list of states: http://tcl.tk (focus, not focused, etc)

# logo = PhotoImage(file = 'C:\\Projects\\Python\\pythonDrills\\lynda_tkinter\\Exercise Files\\Ch03\\python_logo.gif') # \escape and then \ dir separator
# button.config(image = logo, compound = LEFT)
# small_logo = logo.subsample(5,5)
# button.config(image = small_logo)


# 	4.c ch03/03_selection_buttons.py
#	check buttons can store binary value
#	radio buttons are not limited in binary

# from tkinter import *
# from tkinter import ttk

# root = Tk()

# checkbutton = ttk.Checkbutton(root, text = 'SPAM?')
# checkbutton.pack()
# # /!\ # Tkinter variable classes
# # BooleanVar
# # DoubleVar
# # IntVar
# # StringVar

# spam = StringVar()
# spam.set('SPAM!')
# spam.get()
# checkbutton.config(variable = spam, onvalue = 'SPAM Please!', offvalue = 'Boo SPAM')
# spam.get() # depending on check or unckeck will ^^^^ display those
# breakfast = StringVar()
# # define the text and variable used with this object, and immediately use pack geo mgr to show
# ttk.Radiobutton(root, text = 'SPAM', variable = breakfast, value = 'SPAM').pack()
# ttk.Radiobutton(root, text = 'Eggs', variable = breakfast, value = 'Eggs').pack()
# ttk.Radiobutton(root, text = 'Sausage', variable = breakfast, value = 'Sausage').pack()
# ttk.Radiobutton(root, text = 'SPAM', variable = breakfast, value = 'SPAM').pack()
# breakfast.get() # check what user has selected
# # this will change the text of the TEXT label of the spam.checkbutton
# checkbutton.config(textvariable = breakfast)


# 	4.d ch03/04_entry.py
#	short text string
#	for example: username & password

# from tkinter import *
# from tkinter import ttk

# root = Tk()
# entry = ttk.Entry(root, width=30)
# entry.pack()
# # enter text... 'asdlakjsdf'
# #entry = ttk.Entry(root, width=50).pack() # testing to see if I get .pack()
# entry.get()
# entry.delete(0,1) # the second # is non-inclusive so it will just del the 1st-index char
# entry.delete(0,END) # clear it
# entry.insert(0, 'Enter Your Password') # first is index to place it.
# entry.config(show = '*') # this is going to have you type your input but will replace with * like a password! :)
# entry.get() # will be real contents not *
# entry.state(['disabled'])
# entry.state(['!disabled'])
# entry.state(['readonly']) # way to allow user to copy but not replace text field


# 	4.e ch03/05_selection_boxes.py
#	combo box/dropdown
#	spin box - cycle through list of options with inherent order

# from tkinter import *
# from tkinter import ttk

# root = Tk()
# month = StringVar()
# combobox = ttk.Combobox(root, textvariable = month)
# combobox.pack()
# combobox.config(values = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# month.get()
# month.set('Dec') # demo that you can pre set
# month.set('Not a month') # demo that you can preset to anything
# # a user currently could input anything and it will be passed as "valid"
# year = StringVar()
# # spinbox not avail under theme'd tk box
# Spinbox(root, from_ = 1990, to = 2014, textvariable = year).pack() # from is a protected keyword, so have to use from_
# year.get() # currently can type in anything such as 1923 or 'dog' shit like that


# 	4.f ch03/06_progressbar_scale.py
#	both avail as themed interface

# from tkinter import *
# from tkinter import ttk

# root = Tk()
# progressbar = ttk.Progressbar(root, orient = HORIZONTAL, length = 200) # HOR/VER and len is in pixels
# progressbar.pack()
# progressbar.config(mode = 'indeterminate')
# progressbar.start() # keep moving back and forth
# progressbar.stop()
# progressbar.config(mode = 'determinate', maximum = 11.0, value = 4.2) # default is 100 # this is perfect for the 25 horse race game
# progressbar.step() # will increase value by 1.0
# progressbar.step(5) # the number to step
# value = DoubleVar() #the value is stored as a double
# progressbar.config(variable = value)
# scale = ttk.Scale(root, orient = HORIZONTAL, length = 400, variable = value, from_ = 0.0, to = 11.0)
# scale.pack()
# scale.set(4.2) # will programmatically set scale
# scale.get()
# label = ttk.Label(root).pack() # to create a label/verbosity of the scale's progress number
# label.config(textvariable = value) # in this example to set the label to the variable "value" which will change dep on scale


# 5. Chapter 4 exercise, frames and organizational widgets
# --------------------------------------------------------
# 	5.a ch04/01_frame.py
#	frames can act as parent and geo mgr to hold and organize other widgets.  sub-regions
# /=============================================\
# |				|								|
# |				|								|
# |				|			frame				|
# |				|	(display information)		|
# |				|								|
# |	 frame		|								|
# | (navigation	|===============================|
# |	controls)	|								|
# |				|								|
# |				|								|
# |				|			frame				|
# |				|		(user controls)			|
# |				|								|
# |				|								|
# \=============================================/

# from tkinter import *
# from tkinter import ttk        
    
# root = Tk()
# frame = ttk.Frame(root) # root is parent of this frame
# frame.pack() # default value is 0,0
# frame.config(height = 100, width = 200)
# # 6 diff types of relief: flat (no border), raised, sunken, solid, ridge, groove
# # ALL CAPS
# frame.config(relief = RIDGE)
# # prior we used "root" but now we make parent "frame"
# ttk.Button(frame, text = 'Click Me').grid()
# frame.config(padding = (30, 15))
# # LabelFrame (Cap L/F) is for dispaying a frame with the following:
# # cannot modify relief property of LabelFrame
# ttk.LabelFrame(root, height = 100, width = 200, text = 'My Frame').pack()
# /=============================================\
# |				|								|
# |				|								|
# |				|			frame				|
# |				|	(display information)		|
# |				|								|
# |	 frame		|								|
# | (navigation	|==My Frame Here================|
# |	controls)	|								|
# |				|								|
# |				|								|
# |				|		LabelFrame Example		|
# |				|		 						|
# |				|								|
# |				|								|
# \=============================================/


# 	5.b ch04/02_toplevel.py
# 	
# from tkinter import *      
    
# root = Tk()

# window = Toplevel(root) # this is a slave to "root" window but at this point cannot tell them apart
# window.title('New Window')
# # by default puts new window on top of stack
# window.lower() # puts it down a layer
# window.lift(root) # lift it to just above the () window, in this case root

# window.state('zoomed') # maximize
# window.state('withdrawn') # completely hides from user.  display: none;-type.
# window.state('iconic') # this is std minimize
# window.state('normal') # returns to prior state
# print(window.state())
# window.state('normal') # return again, this time back to 200x200 or whatever size

# window.iconify() # same as state('inconic')
# window.deiconify() # same as state('normal')

# #<variable>.geometry('<WIDTH IN PX>x<HEIGHT IN PX>+<X>+<Y>') # x and y coordinates of upper left.  these are relative to screen size.
# window.geometry('640x480+50+100')
# print(window.geometry())
# window.resizable(False, False) # resizable X and resiable Y
# window.maxsize(640, 480) # two parameters, x and y
# window.minsize(200, 200) # min allowable: x and y
# window.resizable(True, True)
# # root would destroy window because it's the parent and window inherits properties
# root.destroy()


# 	5.c ch04/03_panedwindow.py
# 	paned window holds other geometry.  several frames next to each other to easily resize

# from tkinter import *
# from tkinter import ttk        
    
# root = Tk()

# panedwindow = ttk.Panedwindow(root, orient = HORIZONTAL) # stack side-by-side
# panedwindow.pack(fill = BOTH, expand = True)
# # uses largest height of the two frames: in this case 400
# frame1 = ttk.Frame(panedwindow, width = 100, height = 300, relief = SUNKEN)
# frame2 = ttk.Frame(panedwindow, width = 400, height = 400, relief = SUNKEN)
# panedwindow.add(frame1, weight = 1) # expand at a ratio of 1:4
# panedwindow.add(frame2, weight = 4) # expand at a ratio of 1:4
# frame3 = ttk.Frame(panedwindow, width = 50, height = 400, relief = SUNKEN)
# # add new widget to specific location
# # this frame doesn't have a weight so it will stay at width = 50
# # user can select frame to resize
# panedwindow.insert(1, frame3) # first param = index (zero index) where you want it to be added
# panedwindow.forget(1) # takes 1 param, = index of display: none type thing.


# 	5.d ch04/04_notebook.py
#	using tabs.  notebook is similar to excel tabs
from tkinter import *
from tkinter import ttk        
    
root = Tk()

notebook = ttk.Notebook(root)
notebook.pack()
frame1 = ttk.Frame(notebook) # child of notebook to add to
frame2 = ttk.Frame(notebook) # child of notebook to add to
frame3 = ttk.Frame(notebook) # child of notebook to add to
frame4 = ttk.Frame(notebook) # child of notebook to add to
notebook.add(frame1, text = 'One')
notebook.add(frame2, text = 'Two')
notebook.add(frame3, text = 'Three')
notebook.add(frame4, text = 'Four')
# you can add other widgets not just frames to notebook
ttk.Button(frame1, text = 'Click Me').pack()
frame5 = ttk.Frame(notebook)
notebook.insert(1, frame5, text = 'TEST FRAME 5') # place it in position... 1
notebook.forget(1) # woops it's out of order, remove aka display: none
notebook.add(frame5, text = 'TEST FRAME 5') #add it back to the end of the stack
notebook.select()
notebook.index(notebook.select())

notebook.select(2)

notebook.tab(1, state = 'disabled')
notebook.tab(1, state = 'hidden') #same as forget???
notebook.tab(1, state = 'normal')
notebook.tab(1, 'text')
# if you don't specifcy it will give a list
notebook.tab(1)
























# 666. TESTING
roundVar = round(value, 2)
label.config(textvariable = (value.Decimal(round(value, 2))))
decValue = value.Decimal

value = decimal.Decimal(value)