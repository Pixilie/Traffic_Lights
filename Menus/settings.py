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
import music

# Changing working directory
os.chdir('../Traffic_Lights')

#TODO: Terminer le design + param son appliquer uniquement après restart + langues
def settingsWindow():
    """Settings window."""    
    # Main window setup
    settingsWindow = tkinter.Toplevel()

    # Screen info
    screenWidth = settingsWindow.winfo_screenwidth()
    screenHeight = settingsWindow.winfo_screenheight()

    # Main window setting
    settingsWindow.title("Settings")
    settingsWindow.config(background='#B78BC4')
    settingsWindow.attributes('-fullscreen', True)

    # Exit button function
    def Close():
        """Close the settings window."""        
        settingsWindow.destroy()

    def onEnter(e):
        """On enter event.
        Args:
            e (event): Event.
        """        
        e.widget['bg'] = '#c59dd1'
        e.widget['fg'] = 'white'

    def onLeave(e):
        """On leave event.
        Args:
            e (event): Event.
        """        
        e.widget['bg'] = '#B78BC4'
        e.widget['fg'] = 'white'

    # Title
    title = Label(settingsWindow, bg='#B78BC4', text="Paramètres", font=('Arial', round(screenWidth*0.026)), fg="white", highlightthickness=0, bd=0, width=round(screenWidth*0.02))
    title.pack(side='top')

    # Exit button
    backIcon = PhotoImage(file='./Menus/Assets/Images/back.png', width=round(screenWidth*0.06), height=round(screenHeight*0.09))
    backButton = Button(settingsWindow, image=backIcon, bd=0, bg='#B78BC4', highlightthickness=0, cursor="hand2", activebackground="#c59dd1", command=Close)
    backButton.pack()
    backButton.place(x=screenWidth*0.01, y=0)
    backButton.bind("<Enter>", onEnter)
    backButton.bind("<Leave>", onLeave)

    # Volume control
    volumeControl = Scale(settingsWindow, orient='horizontal', from_=0, to=100, resolution=1, tickinterval=10, length=300, label='Volume (%)', bg='#B78BC4', activebackground="#B78BC4", relief="flat", fg='white', cursor="hand2", highlightthickness=0, command=music.setVolume)
    volumeControl.set(float(music.getVolume()*100))
    volumeControl.pack(side='top')

    # Compiling window
    settingsWindow.mainloop()
