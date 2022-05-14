from tkinter import *
app = Tk()
app.geometry('400x300')
L1 = Label(app, text="1. 50 x 2 = ?")
L1.place(x=20, y=20)
radioValue1 = IntVar() 
r1=Radiobutton(app, text="50", variable=radioValue1, value=1)
r1.place(x=30, y=40)
r2=Radiobutton(app, text="100", variable=radioValue1, value=2)
r2.place(x=30, y=60)
r3=Radiobutton(app, text="200", variable=radioValue1, value=3)
r3.place(x=30, y=80)
L2 = Label(app, text="2. What is the capital of Italy?")
L2.place(x=20, y=120)
radioValue2 = IntVar()
r21=Radiobutton(app, text="Paris", variable=radioValue2, value=1)
r21.place(x=30, y=140)
r22=Radiobutton(app, text="Ulaanbaatar", variable=radioValue2,
value=2)
r22.place(x=30, y=160)
r23=Radiobutton(app, text="Rome", variable=radioValue2, value=3)
r23.place(x=30, y=180)
def show():
    score=0
    if (radioValue1.get() == 2):
        score+=1
    if (radioValue2.get() == 3):
        score+=1
    label=Label(app, text=f"Score {score}", padx=10, anchor='e', font=('helvetica',13))
    label.place(x=220,y=310)
def answer():
    radioValue1.set(2)
    radioValue2.set(3)
button = Button(app, text="Show the score", bg="blue", fg="white", command=show, font="Arial 16")
button.place(x=40, y=300)
button1 = Button(app, text="Show the answer", bg="red", fg="white", command=answer, font="Arial 16")
button1.place(x=40, y=360)

app.mainloop()