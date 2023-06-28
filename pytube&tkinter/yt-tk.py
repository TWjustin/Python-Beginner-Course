import tkinter as tk
from pytube import YouTube

def rbVideo():  # 點選按鈕
    global getvideo
    labelMsg.config(text='')
    getvideo = videorb.get()

def clickDown():    # 按下載影片
    global getvideo, strftype, listradio
    labelMsg.config(text='')
    if(url.get()==''):
        labelMsg.config(text='請輸入網址!')
        return

    if(path.get()==''):
        pathdir = 'download'
    else:
        pathdir = path.get()
        pathdir = pathdir.replace('\\', '\\\\')

    try:
        yt = YouTube(url.get())
        yt.streams.filter(subtype='mp4', res=getvideo, progressive=True).first().download(pathdir)
        labelMsg.config(text='下載完成!')
    except:
        labelMsg.config(text='影片無法下載!')

win = tk.Tk
win.geometry('560x280')
win.title('下載Youtube影片')
getvideo = '360p'
videorb = tk.striingVar()    # 選項按鈕值
url = tk.striingVar()
path = tk.striingVar()   #存檔資料夾

label1 = tk.Label(win, text='Youtube網址:')
label1.place(x=123, y=30)
entryUrl = tk.Entry(win, textvariable=url)
entryUrl.config(width=45)
entryUrl.place(x=220, y=30)

label2 = tk.Label(win, text='存檔路徑:')
label2.place(x=10, y=70)
entryPath = tk.Entry(win, textvariable=path)
entryPath.config(width=45)
entryPath.place(x=220, y=70)

btnDown = tk.Button(win, text='下載影片', command=clickDown)
btnDown.place(x=200, y=110)

rb1 = tk.Radiobutton(win, text='360p, mp4', variable=videorb, value='360p', command=rbVideo)
rb1.place(x=200, y=150)
rb1.select()
rb2 = tk.Radiobutton(win, text='720p, mp4', variable=videorb, value='720p', command=rbVideo)
rb1.place(x=200, y=180)

labelMsg = tk.Label(win, text='', fg='red')
labelMsg.place(x=200, y=220)    # 訊息標籤

win.mainloop()