from tkinter import *
root = Tk()
root.title("Python GUI")

l1=Label(root, text="Date")
l1.grid(row=0, column=0)
e1=Entry(root)
e1.grid(row=0, column=1)

l2=Label(root, text="Content")
l2.grid(row=1, column=0  )
e2=Entry(root)
e2.grid(row=1, column=1)


l3=Label(root, text="bicheed vz")
l3.grid(row=2, column=0  )
e3=Entry(root)
e3.grid(row=2, column=1)

root.mainloop()