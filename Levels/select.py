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

    # Title
    title = Label(levelWindow, bg='#B78BC4', text="Sélectionner un niveau",
                  font=('Arial', round(screenWidth*0.026)), fg="white", highlightthickness=0, bd=0, width=round(screenWidth*0.01))
    title.pack()

    # Go back button
    # backIcon = PhotoImage(file='../Assets/Icons/exit_icon2.png', width=100, height=71)  # TODO: enlever bordure quand survoler + voir pourquoi erreur si on veut afficher une image
    backButton = Button(levelWindow, text="<-", font=('Arial', round(screenWidth*0.016)), bd=0,
                        bg='#B78BC4', highlightthickness=0, command=goBack)
    backButton.pack(pady=20)
    backButton.place(x=0, y=0)

    # Creating one button and an information panel for each level

    # Panel creation
    infoPanel = Canvas(levelWindow)

    # Panel function
    def onEnter(e):
        infoPanel = Canvas(levelWindow, width=screenWidth *
                           0.43, height=screenHeight*0.8, bg='#B78BC4', bd=8)
        infoPanel.create_text(screenWidth*0.22, screenHeight*0.05, text=f'Niveau {e}', font=(
            'Arial', round(screenWidth*0.016)), fill="white")
        infoPanel.pack()
        infoPanel.place(x=screenWidth*0.55, y=screenHeight*0.17)

    def onLeave(e):
        infoPanel.destroy()

    directory = os.listdir('./Levels')
    yPos = screenHeight*0.1
    fileIndex = 0
    for files in directory:
        if files.endswith('.py') and files != 'select.py' and files != '__pycache__':
            fileIndex += 1
            yPos += 0.07*screenHeight
            # Button creation
            levelButton = Button(levelWindow, text=f'Niveau {fileIndex}', font=(
                'Arial', round(screenWidth*0.016)), bd=0, bg='#B78BC4', fg="#ffffff", width=round(screenWidth*0.02), command=goBack)
            levelButton.pack(pady=40)
            levelButton.place(x=screenWidth*0.01, y=yPos)
            # Executing the panel function
            levelButton.bind("<Enter>", onEnter)
            levelButton.bind("<Leave>", onLeave)

    # Compiling the main frame
    frame.pack(expand=YES)
    levelWindow.mainloop()
