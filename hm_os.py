from tkinter import *
import sys
import time 
import os
import tkinter.messagebox 

root = Tk()
root.title('HyoMinSystem')
def openCalcu():
    import sub

def terminateOS():
    sys.exit()

def showTime():
    Current_Time =  str(time.time()) 
    tkinter.messagebox.showinfo('Current Time',Current_Time)       

def ShowmagicNote():
    import magicText

title = Label(root,text = 'HYOMIN Operating System')
title.pack(side = TOP)

quit = Button(root,text = 'Quit',command = terminateOS)
quit.pack()
calopen = Button(root, text = 'open Calculator',command = openCalcu)
calopen.pack()
currntTime = Button(root,text = 'show current time',command = showTime)
currntTime.pack()

magicNote = Button(root, text = 'open magic note',command = ShowmagicNote)
magicNote.pack()
root.mainloop()