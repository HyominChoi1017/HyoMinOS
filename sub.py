from tkinter import *
import tkinter.messagebox
import sys
import math as mth

root = Tk()
root.config(background = 'green')
root.title('Calculator')
firstNum = Entry(root)
secNum = Entry(root)
firstNum.grid(column = 1,row = 1)
secNum.grid(column = 1,row = 5)
def add():
    a = int(firstNum.get())
    b = int(secNum.get())
    tkinter.messagebox.showinfo('result',a+b)
    if tkinter.messagebox.showinfo == 'yes':
        sys.exit()
def sub():
    a = int(firstNum.get())
    b = int(secNum.get())
    tkinter.messagebox.showinfo('result',a-b)

def mul():
    a = int(firstNum.get())
    b = int(secNum.get())
    tkinter.messagebox.showinfo('result',a*b)


def demul():
    a = int(firstNum.get())
    b = int(secNum.get())
    tkinter.messagebox.showinfo('result',a/b)


def square():
    a = int(firstNum.get())
    b = int(secNum.get())
    tkinter.messagebox.showinfo('result',a**b)


addBt = Button(root, text = '+', command = add)
subBt = Button(root,text = '-', command = sub)
mulBt = Button(root,text = '*', command = mul)
demulBt = Button(root,text = '/', command = demul)
squareBt = Button(root, text = '^', command = square)


addBt.grid(column = 0,row = 6)
subBt.grid(column = 1,row = 6)
mulBt.grid(column = 2,row = 6)
demulBt.grid(column = 3,row = 6)
squareBt.grid(column = 4,row = 6)

root.mainloop()