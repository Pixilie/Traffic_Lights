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
        music.playSound(float(os.getenv("SOUND_VOLUME")))

    def onLeave(e):
        e.widget['bg'] = '#B78BC4'
        e.widget['fg'] = 'white'
        
    def startGame(level): #FIXME: Faire fonctionner, module du niveau non trouvé
        exec(open(f"./Game/{level}").read())

    # Title
    title = Label(levelWindow, bg='#B78BC4', text="Sélectionner un niveau", font=('Arial', round(screenWidth*0.026)), fg="white", highlightthickness=0, bd=0, width=round(screenWidth*0.02))
    title.pack()

    # Go back button
    backIcon = PhotoImage(file='./Menus/Assets/Images/back.png', width=round(screenWidth*0.06), height=round(screenHeight*0.09))
    backButton = Button(levelWindow, image=backIcon, font=('Arial', round(screenWidth*0.016)),  bd=0, relief="flat", activebackground="#c59dd1", activeforeground="white", cursor="hand2", bg='#B78BC4', fg="#ffffff", command=goBack)
    backButton.pack(pady=20)
    backButton.place(x=screenWidth*0.01, y=0)
    backButton.bind("<Enter>", onEnter)
    backButton.bind("<Leave>", onLeave)

    # Creating one button and an information panel for each level
    # Panel creation
    infoPanel = Canvas(levelWindow)

    # Panel function
    def onEnterLevelButton(e):
        """Creates a panel with information about the level and changes the background color of the button
        Args:
            e (Event): Event triggered by the button
        """
        e.widget['bg'] = '#c59dd1'
        e.widget['fg'] = 'white'
        music.playSound(float(os.getenv("SOUND_VOLUME")))
        # TODO: Terminer panel + panel ne disparaît pas quand on quitte le bouton
        infoPanel = Canvas(levelWindow, width=screenWidth * 0.43, height=screenHeight*0.8, bg='#B78BC4', bd=8)
        infoPanel.create_text(screenWidth*0.22, screenHeight*0.05, text=f'Niveau {e}', font=('Arial', round(screenWidth*0.016)), fill="white")
        infoPanel.pack()
        infoPanel.place(x=screenWidth*0.55, y=screenHeight*0.17)

    def onLeaveLevelButton(e):
        """Destroys the panel and changes the background color of the button
        Args:
            e (Event): Event triggered by the button
        """
        infoPanel.destroy()
        e.widget['bg'] = '#B78BC4'
        e.widget['fg'] = 'white'

    # Creating the buttons for each level
    directory = os.listdir('./Game')
    yPos = screenHeight*0.1
    folderIndex = 0
    for file in directory:
        if "level" in file and file != "levelFinished.py":
            print(file)
            folderIndex += 1
            yPos += 0.07*screenHeight
            # Button creation
            levelButton = Button(levelWindow, text=f'Niveau {folderIndex}', font=('Arial', round(screenWidth*0.016)), bd=0, cursor="hand2", bg='#B78BC4' ,activebackground="#c59dd1", activeforeground="white", fg="#ffffff", width=round(screenWidth*0.02), command=startGame(file))
            levelButton.pack(pady=40)
            levelButton.place(x=screenWidth*0.01, y=yPos)
            levelButton.bind("<Enter>", onEnterLevelButton)
            levelButton.bind("<Leave>", onLeaveLevelButton)

    # Play music
    music.playMusic(float(os.getenv("SOUND_VOLUME")))
    
    # Compiling window
    levelWindow.mainloop()
