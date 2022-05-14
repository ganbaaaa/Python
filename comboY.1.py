from tkinter import *
from tkinter import ttk
win  = Tk()
win.geometry("400x200")
win.configure(bg = 'blue')
import tkinter.messagebox as msg
def quit():
    msg.showinfo("quit", "leaving now")
    exit()
l1=Label(win, text="Date")
l1.place(x=10, y=10)
comboY=ttk.Combobox(win, values=["2020","2021", "2022", "2003" , "2010"], width=10)
comboY.place(x=60, y=10)
comboY.current(0)
comboM=ttk.Combobox(win, values=["January","February","March","April",
"May","June","July","August", "September","October","November",
"December"], width=10)
comboM.place(x=150, y=10)
comboM.current(0)
comboD=ttk.Combobox(win, values=["1","2","3","4","5","6","7","8", "9","10","11","12","13","14","15","16","17","18","19","20","21",
"22","23","24","25","26","27","28","29","30","31"], width=10)
comboD.place(x=240, y=10)
comboD.current(0)
def save():
    msg.showinfo("save", "Gan-Erdene")
    exit()
btn=Button( text='SAVE', command=save)
btn.place(x=225, y=70)      
def quit():
    msg.showinfo("quit", "BEY LLRA")
    exit()
btn=Button( text='LEAVING', command=quit)
btn.place(x=60, y=70)
l1=Label( text="text")
l1.pack(side=LEFT)
l1.place(x=10, y=50)
e1=Entry()
win.mainloop()