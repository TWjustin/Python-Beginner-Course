import tkinter as tk

def clickme():
    global count
    count += 1
    labeltext.set('you clicked me '+str(count)+' times!')
    if(btntext.get()=='click me!'):
        btntext.set('reverted!')
    else:
        btntext.set('click me!')

win = tk.Tk
labeltext = tk.StringVar()
btntext = tk.StringVar()
count = 0
label1 = tk.Label(win, fg='red', textvariable=labeltext)
labeltext.set('welcome!')
label1.pack()
btn1 = tk.Button(win, textvariable=btntext, command=clickme)
btntext.set('click me!')
btn1.pack()
win.mainloop()