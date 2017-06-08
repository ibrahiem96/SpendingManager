import time as date
import json as utility
from Tkinter import *

def show_entry_fields():
    print ("Month: %s" % (e1.get()))


def updatePortfolio():
    return

master = Tk()

Label(master, text="Month").grid(row=0,column=0)
Label(master, text="Placeholder").grid(row=0,column=1)
Label(master, text="Rent").grid(row=1)
Label(master, text="Food").grid(row=2)
Label(master, text="Gifts").grid(row=3)
Label(master, text="Events").grid(row=4)
Label(master, text="Large Expense").grid(row=5)
Label(master, text="Misc").grid(row=6)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e6 = Entry(master)
e7 = Entry(master)


e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)
e7.grid(row=6, column=1)

Button(master, text='Quit', command=master.quit).grid(row=8,column=0,sticky=W+E,pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=8,column=2,sticky=E,pady=4)
Button(master, text='Update', command=updatePortfolio).grid(row=7,column=1,sticky=W+E,pady=4)

mainloop()



