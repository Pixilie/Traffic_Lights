# Compatibility with Python 2 and 3
try:
    import tkinter
    from tkinter import *
except ImportError:
    import Tkinter as tkinter
    from Tkinter import *
# Import other files from the game
import Levels.select as level
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
    level.levelsWindow()


# Settings button function #TODO: Terminer fonction, chercher importer un autre fichier
def Settings():
    mainWindow.destroy()


# Credits button function #TODO: Terminer fonction, chercher importer un autre fichier
def Credits():
    mainWindow.destroy()


# Main frame
frame = Frame(mainWindow, bg='#B78BC4')


# Title
title_icon = PhotoImage(file="./Assets/Icons/TRAFFIC LIGHT.png")
title = Canvas(mainWindow, width=screenWidth*0.7, height=screenHeight*0.5,
               bg='#B78BC4', bd=0, highlightthickness=0)
title.create_image(screenWidth*0.35, screenHeight*0.2, image=title_icon)
title.pack(pady=20)

# Exit button
exitIcon = PhotoImage(
    file='./Assets/Icons/exit_icon2.png', width=100, height=71)  # TODO: enlever bordure quand survoler + solution pour reponsive taille car n'accepte pas les float
exitButton = Button(mainWindow, image=exitIcon,
                    bd=0, bg='#B78BC4', highlightthickness=0, command=Close)
exitButton.pack(pady=800)
exitButton.place(x=screenWidth*0.95, y=screenHeight*0.93)

# Levels Button #TODO:son quand survoler ou cliquer
levelsButton = Button(mainWindow, text="Niveaux", font=('Arial', 30),
                      bd=0, bg='#B78BC4', fg="#ffffff", width=10, command=Levels)
levelsButton.pack(pady=20)
levelsButton.place(x=screenWidth*0.44, y=screenHeight*0.35)

# Setting Button #TODO:son quand survoler ou cliquer
settingsButton = Button(mainWindow, text="Paramètres", font=('Arial', 30),
                        bd=0, bg='#B78BC4', fg="#ffffff", width=10, command=Settings)
settingsButton.pack(pady=20)
settingsButton.place(x=screenWidth*0.44, y=screenHeight*0.45)

# Credits Button #TODO:son quand survoler ou cliquer
creditsButton = Button(mainWindow, text="Crédits", font=('Arial', 30),
                       bd=0, bg='#B78BC4', fg="#ffffff", width=10, command=Credits)
creditsButton.pack(pady=20)
creditsButton.place(x=screenWidth*0.44, y=screenHeight*0.55)

# Compiling the main frame
frame.pack(expand=YES)
mainWindow.mainloop()
