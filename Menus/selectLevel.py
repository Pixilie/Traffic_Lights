# Compatibility with Python 2 and 3
try:
    import tkinter
    from tkinter import *
except ImportError:
    import Tkinter as tkinter
    from Tkinter import *

#Other imports
import music
import os

# Changing working directory
os.chdir('../Traffic_Lights')

def levelsWindow():
    """Creates the window to select a level"""

    # levelWindow initialization
    levelWindow = tkinter.Toplevel()

    # Screen informations
    screenWidth = levelWindow.winfo_screenwidth()
    screenHeight = levelWindow.winfo_screenheight()

    # Functions definition ----------------------------------------------------------------------------------------------------
    def goBack():
        """Close the window."""        
        levelWindow.destroy()

    def onEnter(event):
        """On enter event.
        Args:
            event (Event): Event.
        Returns:
            int: Index of the hover button.
        """        
        event.widget['bg'] = '#c59dd1'
        event.widget['fg'] = 'white'
        music.playSound('hover', music.getVolume())
        index = 0
        for c in str(event.widget):
            if c.isdigit():
                index += int(c)
        return index-1

    def onLeave(event):
        """On leave event.
        Args:
            event (Event): Event.
        """        
        event.widget['bg'] = '#B78BC4'
        event.widget['fg'] = 'white'

    def onEnterLevelButton(index):
        """Update the information panel
        Args:
            fileIndex (int): Index of the file
        """
        selectedLevel = __import__(f'Game.level{index}', fromlist=[f'Game.level{index}'])

        # Info panel update
        level, levelName, completed, lives, score, carsToPass, carsPassed = selectedLevel.levelInfos
        infoPanel.delete("all")
        infoPanel.create_text(screenWidth*0.22, screenHeight*0.05, text=levelName, font=('Arial', round(screenWidth*0.025)), fill="white")
        infoPanel.create_text(screenWidth*0.22, screenHeight*0.15, text="Description (bug affichage à fixe)", font=('Arial', round(screenWidth*0.016)), fill="white")
        infoPanel.create_text(screenWidth*0.22, screenHeight*0.20, text=f'Complété: {completed}', font=('Arial', round(screenWidth*0.016)), fill="white")
        infoPanel.create_text(screenWidth*0.22, screenHeight*0.25, text=f'Vies: {lives}', font=('Arial', round(screenWidth*0.016)), fill="white")
        infoPanel.create_text(screenWidth*0.22, screenHeight*0.30, text=f'Meilleur score: {score}', font=('Arial', round(screenWidth*0.016)), fill="white")
        infoPanel.create_text(screenWidth*0.22, screenHeight*0.35, text=f'Voitures à faire passer: {carsToPass}', font=('Arial', round(screenWidth*0.016)), fill="white")

    def onLeaveLevelButton(event):
        """Update the information panel
        Args:
            event (event): Event (unused but mandatory)
        """
        infoPanel.delete("all")
        infoPanel.create_text(screenWidth*0.22, screenHeight*0.05, text='Aucun niveau sélectionné', font=('Arial', round(screenWidth*0.016)), fill="white")

    def onLeaveCombined(event):
        """Combined function for onLeave and onLeaveLevelButton functions
        Args:
            event (Event): Event.
        """        
        onLeave(event)
        onLeaveLevelButton(event)
    
    def onEnterCombined(event):
        """Combined function for onEnter and onEnterLevelButton functions
        Args:
            event (Event): Event.
        """        
        index = onEnter(event)
        onEnterLevelButton(index)
        
    def startGame(index):
        """Start the game
        Args:
            fileIndex (int): Index of the file
        """
        level = __import__(f'Game.level{index}', fromlist=[f'Game.level{index}'])
        level.level()

# -----------------------------------------------------------------------------------------------------------------------------
    # Main window setting
    levelWindow.title("Traffic Light")
    levelWindow.config(background='#B78BC4')
    levelWindow.attributes('-fullscreen', True)
    
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

    # Panels creation
    infoPanel = Canvas(levelWindow)
    infoPanel = Canvas(levelWindow, width=screenWidth * 0.43, height=screenHeight*0.8, bg='#B78BC4', bd=8)
    infoPanel.create_text(screenWidth*0.22, screenHeight*0.05, text='Aucun niveau sélectionné', font=('Arial', round(screenWidth*0.016)), fill="white")
    infoPanel.pack()
    infoPanel.place(x=screenWidth*0.55, y=screenHeight*0.15)

    # Creating the buttons for each level
    directory = os.listdir('./Game')
    yPos = screenHeight*0.1
    fileIndex = 0
    for file in directory:
        if file.lower().startswith('level') and file.lower().endswith('.py') and file != 'levelFinished.py':
            fileIndex += 1
            yPos += 0.07*screenHeight
            # Button creation
            levelButton = Button(levelWindow, text=f'Niveau {fileIndex}', font=('Arial', round(screenWidth*0.016)), bd=0, cursor="hand2", bg='#B78BC4' ,activebackground="#c59dd1", activeforeground="white", fg="#ffffff", width=round(screenWidth*0.03))
            levelButton.pack(pady=40)
            levelButton.place(x=screenWidth*0.04, y=yPos)

            # Binds
            levelButton.bind("<Enter>", onEnterCombined)
            levelButton.bind("<Leave>", onLeaveCombined)
            levelButton.bind("<ButtonPress>", lambda event: startGame(index = onEnter(event)))

    # Play music
    music.playSound('music', music.getVolume())
    
    # Compiling window
    levelWindow.mainloop()
