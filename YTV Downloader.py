import tkinter as tk
import pytube

frame = tk.Tk()
frame.title("Save YT ilazzy")
frame.geometry('400x200')
frame.configure(bg='gold')
lable1 = tk.Label(frame, text="\n YOUTUBE VIDEO DOWNLOADER WITH ONE CLICK",background="gold")
lable1.pack()
link = tk.Text(frame,height = 2,width = 25, foreground="black")
link.pack()

def engine():
   result=link.get("1.0","end")
   yt = pytube.YouTube(result)
   stream = yt.streams.first()
   save = "d:/Save/"
   stream.download(save)
   lable2.config(text = "RESULT:SAVED")
   link.delete("1.0","end")

Button1 = tk.Button(frame,text = "SAVE",command = engine)
Button1.pack()
lable2 = tk.Label(frame, text = "",background="gold")
lable2.pack()

frame.mainloop()
