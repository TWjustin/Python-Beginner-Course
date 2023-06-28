import tkinter as tk
def click1():
    textvar.set('clicked')

win = tk.Tk()
textvar = tk.StringVar()
button1 = tk.Button(win, textvariable=textvar, command=click1)
textvar.set('button')
button1.pack()
win.mainloop()
# print(type(textvar))