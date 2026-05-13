#!python3

"""
Create the interface shown.  The program should be able to perform the math operation specified
by the buttons and display the entry in the 3rd entry widget;
"""

import tkinter as tk

w = tk.Tk()
w.attributes("-topmost",True)

def multiply():
    number1 = float(e[0].get())
    number2 = float(e[1].get())
    answer = number1*number2
    e[2].insert(0, answer)

def add():
    number1 = float(e[0].get())
    number2 = float(e[1].get())
    answer = number1+number2
    e[2].insert(0, answer)

def subtract():
    number1 = float(e[0].get())
    number2 = float(e[1].get())
    answer = number1-number2
    e[2].insert(0, answer)

def division():
    number1 = float(e[0].get())
    number2 = float(e[1].get())
    answer = number1/number2
    e[2].insert(0, answer)

l = []
l.append( tk.Label(w,text="Number 1"))
l.append( tk.Label(w,text="Number 2"))
l.append( tk.Label(w,text="Number Calculator"))

e = []
e.append( tk.Entry(w,text=""))
e.append( tk.Entry(w,text=""))
e.append( tk.Entry(w,text="answer",state='disabled'))
b=[]
b.append(tk.Button(w,text="x"))
b.append(tk.Button(w,text="+"))
b.append(tk.Button(w,text="-"))
b.append(tk.Button(w,text="÷"))

b[0].bind("<Button>",multiply)
b[1].bind("<Button>",add)
b[2].bind("<Button>",subtract)
b[3].bind("<Button>",division)


l[2].grid(row=1,column=1,columnspan=4)
l[0].grid(row=2,column=1,columnspan=2)
l[1].grid(row=2,column=3,columnspan=2)
e[0].grid(row=3,column=1, columnspan=2)
e[1].grid(row=3,column=3, columnspan=2)
b[0].grid(row=4,column=1)
b[1].grid(row=4,column=2)
b[2].grid(row=4,column=3)
b[3].grid(row=4,column=4)
e[2].grid(row=5,column=1,columnspan=4)

w.mainloop()


# run sareta tokini,  number1 and number2 no numbers wo tukau
#each calculation ni, each def() ga hituyou
#each calculation wo, entry3 ni ireru
#dekinaiiiii