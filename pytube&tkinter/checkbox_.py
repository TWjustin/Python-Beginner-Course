import tkinter as tk

def choose():
    str = '你喜歡的球類運動:'
    for i in range(len(choice)):
        if(choice[i].get()==1):
            str = str + ball[i] +','
    msg.set(str)

win = tk.Tk
choice = []
ball = ['足球','籃球','棒球']
msg = tk.StringVar()
label = tk.Label(win, text='選擇喜歡的球類運動:')
label.pack()
for i in range(len(ball)):
    item = tk.Checkbutton(win, text=ball[i], variable=choice[i], command=choose)
    item.pack()
lblmsg = tk.Label(win, fg='red', textvariable=msg)
lblmsg.pack()
win.mainloop()