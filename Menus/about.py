# Compatibility Python 2 and 3
try:
    import tkinter
    from tkinter import *
except ImportError:
    import Tkinter as tkinter
    from Tkinter import *
# Other imports
import os


# Changing working directory
os.chdir('../Traffic_Lights')

def aboutWindow():
    """credits window."""    
    # Main window setup
    aboutWindow = tkinter.Toplevel()

    # Screen info
    screenWidth = aboutWindow.winfo_screenwidth()
    screenHeight = aboutWindow.winfo_screenheight()

    # Main window setting
    aboutWindow.title("A propos")
    aboutWindow.config(background='#B78BC4')
    aboutWindow.attributes('-fullscreen', True)

    # Exit button function
    def Close():
        """Close the credits window."""        
        aboutWindow.destroy()

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
    title = Label(aboutWindow, bg='#B78BC4', text="A propos", font=('Arial', round(screenWidth*0.026)), fg="white", highlightthickness=0, bd=0, width=round(screenWidth*0.02))
    title.pack(side='top')

    # Exit button
    backIcon = PhotoImage(file='./Menus/Assets/Images/back.png', width=round(screenWidth*0.08), height=round(screenHeight*0.12))
    backButton = Button(aboutWindow, image=backIcon, bd=0, bg='#B78BC4', highlightthickness=0, cursor="hand2", activebackground="#c59dd1", command=Close)
    backButton.pack()
    backButton.place(x=screenWidth*0.01, y=0)
    backButton.bind("<Enter>", onEnter)
    backButton.bind("<Leave>", onLeave)
    
    #Text for credits
    text = tkinter.Label(aboutWindow, text = "Traffic Lights est un jeu en 2D qui s'inspire du jeu populaire Traffix disponible sur Steam, Apple store et Google store.\n Nous avons développé ce jeu en utilisant la bibliothèque Pygame dans le cadre d'un projet informatique scolaire.\n Le gameplay est simple, défiant les joueurs de gérer le trafic en contrôlant les feux de circulation.\n Si vous aimez les jeux de réflexion qui mettent à l'épreuve vos capacités de décision, essayez Traffic Lights.\nCe projet est celui de 3 lycéens de Saint-Michel de Picpus, Paris XII : COUTY Kristen, BRUNO Thomas et Vladimir TURCANU-LAZAROV.\n\nPour les différents sons utilisés dans le jeu voici les sources afin de respecter les différentes licenses libre de droits. \n\nNoms des différentes musiques:\nShine par Onycs\nGaia par Nova Noma\nK For Kool par Kuromaru\n\nLicenses pour les effets sonores:\nSound Effect from Pixabay", bg= '#B78BC4', fg= "white", font=('Arial', round(screenWidth*0.012)))
    text.place(x=screenWidth*0.01, y=screenHeight*0.3)
    
    # Compiling window
    aboutWindow.mainloop()
