# Compatibility with Python 2 and 3
try:
    import tkinter
    from tkinter import *
except ImportError:
    import Tkinter as tkinter
    from Tkinter import *
#Import other files from the game
import music
# Other imports
import os
#import Game.level1 as level1

# Changing working directory
os.chdir('../Traffic_Lights')

def levelsWindow():
    """Creates the window to select a level"""    
    # Select window setup
    levelWindow = tkinter.Toplevel()

    # Screen info
    screenWidth = levelWindow.winfo_screenwidth()
    screenHeight = levelWindow.winfo_screenheight()

    # Main window setting
    levelWindow.title("Traffic Light")
    levelWindow.config(background='#B78BC4')
    levelWindow.attributes('-fullscreen', True)

    # Exit button function
    def goBack():
        levelWindow.destroy()

    def onEnter(e):
        e.widget['bg'] = '#c59dd1'
        e.widget['fg'] = 'white'
        music.playSound('hover', music.getVolume())

    def onLeave(e):
        e.widget['bg'] = '#B78BC4'
        e.widget['fg'] = 'white'
        
    def startGame(level): #FIXME: niveau se lance directement sans cliquer sur le bouton du niveau
        print("click")
        #exec(open(f"./Game/{level}").read())

    # Title
    title = Label(levelWindow, bg='#B78BC4', text="Sélectionner un niveau", font=('Arial', round(screenWidth*0.026)), fg="white", highlightthickness=0, bd=0, width=round(screenWidth*0.02))
    title.pack()

    # Go back button
    backIcon = PhotoImage(file='./Menus/Assets/Images/back.png', width=round(screenWidth*0.08), height=round(screenHeight*0.13))
    backButton = Button(levelWindow, image=backIcon, font=('Arial', round(screenWidth*0.016)),  bd=0, relief="flat", activebackground="#c59dd1", activeforeground="white", cursor="hand2", bg='#B78BC4', fg="#ffffff", command=goBack)
    backButton.pack(pady=20)
    backButton.place(x=screenWidth*0.01, y=0)
    backButton.bind("<Enter>", onEnter)
    backButton.bind("<Leave>", onLeave)

    # Creating one button and an information panel for each level
    # Panel creation
    infoPanel = Canvas(levelWindow)
    infoPanel = Canvas(levelWindow, width=screenWidth * 0.43, height=screenHeight*0.8, bg='#B78BC4', bd=8)
    infoPanel.create_text(screenWidth*0.22, screenHeight*0.05, text='Aucun niveau sélectionné', font=('Arial', round(screenWidth*0.016)), fill="white")
    infoPanel.pack()
    infoPanel.place(x=screenWidth*0.55, y=screenHeight*0.15)


    # Panel function
    def onEnterLevelButton(fileIndex):
        """Update the information panel
        Args:
            fileIndex (int): Index of the file
        """
        level = __import__(f'Game.level{fileIndex}', fromlist=[f'Game.level{fileIndex}'])
        # Info panel update
        levelName, levelDescription, completed, lives, score, carsToPass = level.levelName, level.levelDescription, level.completed, level.lives, level.score, level.carsToPass
        infoPanel.delete("all")
        infoPanel.create_text(screenWidth*0.22, screenHeight*0.05, text=levelName, font=('Arial', round(screenWidth*0.025)), fill="white")
        infoPanel.create_text(screenWidth*0.22, screenHeight*0.15, text="Description (bug à fixe)", font=('Arial', round(screenWidth*0.016)), fill="white")
        infoPanel.create_text(screenWidth*0.22, screenHeight*0.20, text=f'Complété: {completed}', font=('Arial', round(screenWidth*0.016)), fill="white")
        infoPanel.create_text(screenWidth*0.22, screenHeight*0.25, text=f'Vies: {lives}', font=('Arial', round(screenWidth*0.016)), fill="white")
        infoPanel.create_text(screenWidth*0.22, screenHeight*0.30, text=f'Score: {score}', font=('Arial', round(screenWidth*0.016)), fill="white")
        infoPanel.create_text(screenWidth*0.22, screenHeight*0.35, text=f'Voitures à faire passer: {carsToPass}', font=('Arial', round(screenWidth*0.016)), fill="white")

    def onLeaveLevelButton(e): #FIXME: panel ne disparaît pas quand on quitte le bouton
        """Update the information panel
        Args:
            e (event): Event (unused because mandatory)
        """
        infoPanel.delete("all")
        infoPanel.create_text(screenWidth*0.22, screenHeight*0.05, text='Aucun niveau sélectionné', font=('Arial', round(screenWidth*0.016)), fill="white")


    # Creating the buttons for each level
    directory = os.listdir('./Game')
    yPos = screenHeight*0.1
    fileIndex = 0
    for file in directory:
        if "level" in file and file != "levelFinished.py":
            fileIndex += 1
            yPos += 0.07*screenHeight
            # Button creation
            levelButton = Button(levelWindow, text=f'Niveau {fileIndex}', font=('Arial', round(screenWidth*0.016)), bd=0, cursor="hand2", bg='#B78BC4' ,activebackground="#c59dd1", activeforeground="white", fg="#ffffff", width=round(screenWidth*0.03), command=startGame(file))
            levelButton.pack(pady=40)
            levelButton.place(x=screenWidth*0.04, y=yPos)
            #FIXME: Bug .bind() n'effectue pas la fonction après le 1er essai
            levelButton.bind("<Enter>", onEnter)
            levelButton.bind("<Enter>", onEnterLevelButton(fileIndex), add='+')
            levelButton.bind("<Leave>", onLeave)
            levelButton.bind("<Leave>", onLeaveLevelButton, add='+')

    # Play music
    music.playSound('music', music.getVolume())
    
    # Compiling window
    levelWindow.mainloop()
