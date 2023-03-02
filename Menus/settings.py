# Compatibility with Python 2 and 3
try:
    import tkinter
    from tkinter import *
except ImportError:
    import Tkinter as tkinter
    from Tkinter import *
import time
import pygame 

# Main window setup
SettingsWindow = tkinter.Tk()

# Screen info
screenWidth = SettingsWindow.winfo_screenwidth()
screenHeight = SettingsWindow.winfo_screenheight()

# Main window setting
SettingsWindow.title("Settings")
SettingsWindow.config(background='#B78BC4')
SettingsWindow.attributes('-fullscreen', True)


# Exit button function
def Close():
    SettingsWindow.destroy()

def onEnter(e):
    e.widget['bg'] = '#c59dd1'
    e.widget['fg'] = 'white'

def onLeave(e):
    e.widget['bg'] = '#B78BC4'
    e.widget['fg'] = 'white'


# Title
title = Label(SettingsWindow, bg='#B78BC4', text="Paramètre",
                  font=('Arial', round(screenWidth*0.026)), fg="white", highlightthickness=0, bd=0, width=round(screenWidth*0.02))
title.pack(side='top')

# Exit button
exitIcon = PhotoImage(file='./Menus/Assets/exit_icon.png',
                      width=round(screenWidth*0.08), height=round(screenHeight*0.09))
exitButton = Button(SettingsWindow, image=exitIcon,
                    bd=0, bg='#B78BC4', highlightthickness=0, cursor="hand2", activebackground="#c59dd1", command=Close)
exitButton.pack()
exitButton.place(x=screenWidth - 100, y=screenHeight - 71)
exitButton.bind("<Enter>", onEnter)
exitButton.bind("<Leave>", onLeave)

#Music Settings
pygame.mixer.init()

playlist = list()
playlist.append ('./Menus/Assets/music3.mp3')
playlist.append ('./Menus/Assets/music2.mp3')
playlist.append ('./Menus/Assets/music1.mp3')
pygame.mixer.music.load ( playlist.pop() )  
pygame.mixer.music.queue ( playlist.pop() ) 
pygame.mixer.music.set_endevent ( pygame.USEREVENT )  
pygame.mixer.music.set_volume(0.1)

pygame.mixer.music.play()        
Scale = Scale(SettingsWindow, orient='horizontal', from_=0, to=100,
      resolution=1, tickinterval=10, length=200,
      label='Volume (%)', bg = '#B78BC4', activebackground="#B78BC4",relief="flat",fg = 'white', cursor="hand2",highlightthickness=0)
Scale.pack(side = 'top')
# Compiling the main frame
SettingsWindow.mainloop()
