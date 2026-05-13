"""
##### Task 1
Create entry widets to allow user to enter their:
* name
* student number
* grade

Create a button so that when they click on the button, it states all of the information in a 4th entry widget
"""
import tkinter as tk

def run(e):
    data1 = e1.get()
    data2 = e2.get()
    e3Data.set(data1)

win = tk.Tk()


e3Data = tk.StringVar()

l1 = tk.Label(win, text="Enter your name :")
e1 = tk.Entry(win, width=15)
l2 = tk.Label(win, text="Enter your student number :")
e2 = tk.Entry(win, width=15)
b1 = tk.Button(win, text="Confirm", width=15)
b1.bind("<Button>",run)
e3 = tk.Entry(win, textvariable=e3Data)

l1.grid(row=0, column=0, sticky="e")
e1.grid(row=0, column=1)
l2.grid(row=1, column=0)
e2.grid(row=1, column=1)
b1.grid(row=2, column=1)
e3.grid(row=3, column=0)

win.mainloop()

#dekinaii
#entry3 ni, name sika arawarenai