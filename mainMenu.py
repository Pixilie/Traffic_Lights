# Compatibility with Python 2 and 3
try:
    import tkinter
    from tkinter import *
except ImportError:
    import Tkinter as tkinter
    from Tkinter import *
import pygame
# Import other files from the game
import Menus.selectLevel as selectLevel
import Menus.settings as settings

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


# Levels button function #TODO: Terminer fonction, chercher importer un autre fichier
def Levels():
    selectLevel.levelsWindow()


# Settings button function #TODO: Terminer fonction, chercher importer un autre fichier
def Settings():
    mainWindow.destroy()


# Credits button function #TODO: Terminer fonction, chercher importer un autre fichier
def Credits():
    mainWindow.destroy()


def onEnter(e):
    e.widget['bg'] = '#c59dd1'
    e.widget['fg'] = 'white'


def onLeave(e):
    e.widget['bg'] = '#B78BC4'
    e.widget['fg'] = 'white'


# Title
title_icon = PhotoImage(file="./Menus/Assets/traffic_lights.png")
title = Canvas(mainWindow, width=screenWidth*0.7, height=screenHeight*0.35,
               bg='#B78BC4', bd=0, highlightthickness=0)
title.create_image(screenWidth*0.35, screenHeight*0.2, image=title_icon)
title.pack(side='top')

# Exit button
exitIcon = PhotoImage(file='./Menus/Assets/exit_icon.png',
                      width=round(screenWidth*0.08), height=round(screenHeight*0.09))
exitButton = Button(mainWindow, image=exitIcon,
                    bd=0, bg='#B78BC4', highlightthickness=0, cursor="hand2", activebackground="#c59dd1", command=Close)
exitButton.pack()
exitButton.place(x=screenWidth - 100, y=screenHeight - 71)
exitButton.bind("<Enter>", onEnter)
exitButton.bind("<Leave>", onLeave)

# TODO: son
# Levels Button
levelsButton = Button(mainWindow, text="Niveaux", font=('Arial', round(screenWidth*0.016)),
                      bd=0, relief="flat", activebackground="#c59dd1", cursor="hand2", activeforeground="white", bg='#B78BC4', fg="#ffffff", width=round(screenWidth*0.006), command=Levels)
levelsButton.pack(side='top')
levelsButton.bind("<Enter>", onEnter)
levelsButton.bind("<Leave>", onLeave)

# Setting Button
settingsButton = Button(mainWindow, text="Paramètres", font=('Arial', round(screenWidth*0.016)),
                        bd=0, relief="flat", activebackground="#c59dd1", cursor="hand2", activeforeground="white", bg='#B78BC4', fg="#ffffff", width=round(screenWidth*0.008), state="disabled", command=Settings)
settingsButton.pack(side='top')
settingsButton.bind("<Enter>", onEnter)
settingsButton.bind("<Leave>", onLeave)

# Credits Button
creditsButton = Button(mainWindow, text="Crédits", font=('Arial', round(screenWidth*0.016)),
                       bd=0, relief="flat", activebackground="#c59dd1", cursor="hand2", activeforeground="white", bg='#B78BC4', fg="#ffffff", width=round(screenWidth*0.006), state="disabled", command=Credits)
creditsButton.pack(side='top')
creditsButton.bind("<Enter>", onEnter)
creditsButton.bind("<Leave>", onLeave)

#Music
playlist = list()
playlist.append ('./Menus/Assets/music3.mp3')
playlist.append ('./Menus/Assets/music2.mp3')
playlist.append ('./Menus/Assets/music1.mp3')
pygame.mixer.music.load ( playlist.pop() )  
pygame.mixer.music.queue ( playlist.pop() ) 
pygame.mixer.music.set_endevent ( pygame.USEREVENT )  
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()

# Compiling the main frame
mainWindow.mainloop()
