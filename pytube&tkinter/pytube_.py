from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=fCO7f0SmrDc')
print('影片名稱:', yt.title)
print("影片格式共有", str(len(yt.streams)), '種')
print('影片型態為 mp4 且影像及聲音都有的影片:')
print(yt.streams.filter(subtype='mp4', progressive=True))
print('開始下載 mp4, 360p 的影片:')
yt.streams.get_highest_resolution().download()
print('下載完成!')