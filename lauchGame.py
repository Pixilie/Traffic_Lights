# Compatibility with Python 2 and 3
try:
    import tkinter
    from tkinter import *
except ImportError:
    import Tkinter as tkinter
    from Tkinter import *
# Other imports
import os
# Import other files from the game
import Menus.selectLevel as selectLevel
import Menus.settings as settings
import Menus.credits as credits
import music

# Changing working directory
os.chdir('../Traffic_Lights')

# Main window setup
mainWindow = tkinter.Tk()

# Screen info
screenWidth = mainWindow.winfo_screenwidth()
screenHeight = mainWindow.winfo_screenheight()

# Main window setting
mainWindow.title("Traffic Light")
mainWindow.config(background='#B78BC4')
mainWindow.attributes('-fullscreen', True)


# Exit button function
def Close():
    mainWindow.destroy()


# Levels button function
def Levels():
    selectLevel.levelsWindow()


# Settings button function
def Settings():
    settings.settingsWindow()


# Credits button function
def Credits():
    credits.creditsWindow()

def onEnter(e):
    e.widget['bg'] = '#c59dd1'
    e.widget['fg'] = 'white'
    music.playSound(float(music.getVolume()))

def onLeave(e):
    e.widget['bg'] = '#B78BC4'
    e.widget['fg'] = 'white'


# Title
title_icon = PhotoImage(file="./Menus/Assets/Images/traffic_lights.png")
title = Canvas(mainWindow, width=screenWidth*0.7, height=screenHeight*0.35, bg='#B78BC4', bd=0, highlightthickness=0)
title.create_image(screenWidth*0.35, screenHeight*0.2, image=title_icon)
title.pack(side='top')

# Exit button
exitIcon = PhotoImage(file='./Menus/Assets/Images/exit_icon.png', width=round(screenWidth*0.08), height=round(screenHeight*0.09))
exitButton = Button(mainWindow, image=exitIcon, bd=0, bg='#B78BC4', highlightthickness=0, cursor="hand2", activebackground="#c59dd1", command=Close)
exitButton.pack()
exitButton.place(x=screenWidth - 100, y=screenHeight - 71)
exitButton.bind("<Enter>", onEnter)
exitButton.bind("<Leave>", onLeave)

# Levels Button
levelsButton = Button(mainWindow, text="Niveaux", font=('Arial', round(screenWidth*0.016)), bd=0, relief="flat", activebackground="#c59dd1", cursor="hand2", activeforeground="white", bg='#B78BC4', fg="#ffffff", width=round(screenWidth*0.006), command=Levels)
levelsButton.pack(side='top')
levelsButton.bind("<Enter>", onEnter)
levelsButton.bind("<Leave>", onLeave)

# Setting Button
settingsButton = Button(mainWindow, text="Paramètres", font=('Arial', round(screenWidth*0.016)), bd=0, relief="flat", activebackground="#c59dd1", cursor="hand2", activeforeground="white", bg='#B78BC4', fg="#ffffff", width=round(screenWidth*0.008), command=Settings)
settingsButton.pack(side='top')
settingsButton.bind("<Enter>", onEnter)
settingsButton.bind("<Leave>", onLeave)

# Credits Button
creditsButton = Button(mainWindow, text="Crédits", font=('Arial', round(screenWidth*0.016)), bd=0, relief="flat", activebackground="#c59dd1", cursor="hand2", activeforeground="white", bg='#B78BC4', fg="#ffffff", width=round(screenWidth*0.006), state="disabled", command=Credits)
creditsButton.pack(side='top')
creditsButton.bind("<Enter>", onEnter)
creditsButton.bind("<Leave>", onLeave)

# Play music
music.playMusic(float(music.getVolume()))

# Compiling window
mainWindow.mainloop()
