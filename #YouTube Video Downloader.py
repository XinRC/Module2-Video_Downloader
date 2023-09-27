
#Importing needed assets
import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import filedialog, messagebox


#Creation of the GUI looks - specically the labels
def createwidget():
    link_txt = Label(root, text="Youtube Link", background='#FFFFFF', foreground='#FF0000')
    link_txt.grid(pady=5, padx=5, column=1, row=1)
    aud_only = Label(root, text="Audio Only [A]/ Full Video [N]", bg='#FFFFFF', foreground="#FF0000")
    aud_only.grid(pady=5, padx=5, column=1, row=2)
    root.video_link = Entry(root, textvariable=vdo_link, width=50)
    root.video_link.grid(pady= 5, padx=5, column=2, row=1)
    root.audio_only = Entry(root, textvariable=audio_only, width=15)
    root.audio_only.grid(pady=5, padx=5, column=2, row=2)
#Creation of the GUI looks - specifically the buttons
    Download_Button = Button(root, text="Download", command=download, width=30, bg="#008000")
    Download_Button.grid(pady=5, padx=5, column=2, row=3)




def download():

    link = vdo_link.get()
    vdo = YouTube(link)
    audio_choice = audio_only.get()

    if audio_choice == "N":
        my_video = vdo.streams.get_highest_resolution()
        my_video.download()
        messagebox.showinfo("Successfully downloaded the video")


    elif audio_choice == "A":
        my_video = vdo.streams.get_audio_only()
        my_video.download()
        messagebox.showinfo("Successfully downloaded the audio format")


#Creating the "GUI" Box w Tkinter
root = tk.Tk()
vdo_link = StringVar()
audio_only = StringVar()
createwidget()
root.geometry('600x120')
root.resizable(False, False)
root.title("YouTube Video Downloader")
root.config(background='#FFFFFF')


root.mainloop()