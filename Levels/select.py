# Compatibility with Python 2 and 3
try:
    import tkinter
    from tkinter import *
except ImportError:
    import Tkinter as tkinter
    from Tkinter import *
# Other imports
import os


def levelsWindow():
    # Main window setup
    levelWindow = tkinter.Tk()

    # Screen info
    screenWidth = levelWindow.winfo_screenwidth()
    screenHeight = levelWindow.winfo_screenheight()

    # Main window setting
    levelWindow.title("Traffic Light")
    levelWindow.config(background='#B78BC4')
    levelWindow.attributes('-fullscreen', True)

    def goBack():
        levelWindow.destroy()

    # Main frame
    frame = Frame(levelWindow, bg='#B78BC4')

    # Title # TODO: Trouver pourquoi l'affichage du titre provoque une erreur <file> not found
    """
    titleIcon = PhotoImage(file="../Assets/Icons/TRAFFIC LIGHT.png")
    title = Canvas(levelWindow, width=screenWidth*0.7, height=screenHeight*0.5,
                   bg='#B78BC4', bd=0, highlightthickness=0)
    title.create_image(screenWidth*0.35, screenHeight*0.2, image=titleIcon)
    title.pack(pady=20)
    """

    # Go back button
    # backIcon = PhotoImage(file='../Assets/Icons/exit_icon2.png', width=100, height=71)  # TODO: enlever bordure quand survoler + voir pourquoi erreur si on veut afficher une image
    backButton = Button(levelWindow, text="<-", font=('Arial', 30), bd=0,
                        bg='#B78BC4', highlightthickness=0, command=goBack)
    backButton.pack(pady=20)
    backButton.place(x=0, y=0)

    # Creating one button for each level
    directory = os.listdir('./Levels')
    yPos = screenHeight*0.3
    fileIndex = 0
    for files in directory:
        if files.endswith('.py') and files != 'select.py' and files != '__pycache__':
            fileIndex += 1
            yPos += 75
            levelButton = Button(levelWindow, text=f'Niveau {fileIndex}', font=(
                'Arial', 30), bd=0, bg='#B78BC4', fg="#ffffff", width=10, command=goBack)
            levelButton.pack(pady=20)
            levelButton.place(x=screenWidth*0.44, y=yPos)

    # Compiling the main frame
    frame.pack(expand=YES)
    levelWindow.mainloop()
