#!python3

"""
Create a window with 3 entry widgets and 1 button.
The first 2 entry widgets allow the user to enter in the 2 short sides of a right triangle.
When the button is clicked, calculate the length of the hypotenuse and display it in the 3rd entry widget.
Any labels you need for instruction are optional.
"""
import tkinter as tk
import math

def run(e):
    data1 = float(e1.get())
    data2 = float(e2.get())
    answer = math.sqrt(data1**2+data2**2)
    e3.delete(0,tk.END)
    e3.insert(0, answer)

win = tk.Tk()

l = tk.Label(win, text="Enter 2 short sides of a right triangle\nto determin a length of hypotenuse")
e1 = tk.Entry(win)
e2 = tk.Entry(win)
b = tk.Button(win, text="Click here")
b.bind("<Button>",run)
e3 = tk.Entry(win)


l.pack()
e1.pack()
e2.pack()
b.pack()
e3.pack()

win.mainloop()

#dekita