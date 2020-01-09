from tkinter import *
import sys
import tkinter.messagebox

root = Tk()
root.title('Magic Note')
root.config(width = 1920, height = 1080)

main = Entry(root)
main.place(width = 1200, height = 700)

def saveEntryData():
    f_name = str(fileName.get())+'.txt'
    file = open(f_name,'w')
    file.write(main.get())
    tkinter.messagebox.showinfo(' ','Save Complete!!')

fileName = Entry(root, text = 'file name')
getData = Button(root, text = 'save', command = saveEntryData)

getData.pack(side = RIGHT)
fileName.pack(side = RIGHT)


root.mainloop()