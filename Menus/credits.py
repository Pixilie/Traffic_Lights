# Compatibility with Python 2 and 3
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

def creditsWindow():
    """credits window."""    
    # Main window setup
    creditsWindow = tkinter.Toplevel()

    # Screen info
    screenWidth = creditsWindow.winfo_screenwidth()
    screenHeight = creditsWindow.winfo_screenheight()

    # Main window setting
    creditsWindow.title("Crédits")
    creditsWindow.config(background='#B78BC4')
    creditsWindow.attributes('-fullscreen', True)

    # Exit button function
    def Close():
        """Close the credits window."""        
        creditsWindow.destroy()

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
    title = Label(creditsWindow, bg='#B78BC4', text="Crédits", font=('Arial', round(screenWidth*0.026)), fg="white", highlightthickness=0, bd=0, width=round(screenWidth*0.02))
    title.pack(side='top')

    # Exit button
    backIcon = PhotoImage(file='./Menus/Assets/Images/back.png', width=round(screenWidth*0.08), height=round(screenHeight*0.13))
    backButton = Button(creditsWindow, image=backIcon, bd=0, bg='#B78BC4', highlightthickness=0, cursor="hand2", activebackground="#c59dd1", command=Close)
    backButton.pack()
    backButton.place(x=screenWidth*0.01, y=0)
    backButton.bind("<Enter>", onEnter)
    backButton.bind("<Leave>", onLeave)
    
    #Text for credits
    text = tkinter.Label(creditsWindow, text = "\n\n\n\n\n\n\n\n**Traffic Lights** est un jeu en 2D qui s'inspire du jeu populaire [Traffix].\n Nous avons développé ce jeu en utilisant la bibliothèque Pygame dans le cadre d'un projet informatique scolaire.\n Le gameplay est simple, défiant les joueurs de gérer le trafic en contrôlant les feux de circulation.\n Si vous aimez les jeux de réflexion qui mettent à l'épreuve vos capacités de décision, essayez 'Traffic Lights'.\nCe projet est celui de 3 lycéens de Saint-Michel de picpus, Paris XII : COUTY Kristen, BRUNO Thomas et Vladimir TURCANU-LAZAROV.\nPour les différentes musiques voici les sources afin de respecter les différentes licenses libre de droits :\nNoms des différentes musiques:\nShine par Onycs\nGaia par Nova Noma\nK For Kool par Kuromaru\nLicenses pour les effets sonores :\nSound Effect from Pixabay",bg= '#B78BC4',fg= "white",font=('Arial', ))
    text.pack(side = TOP)
    


    # Compiling window
    creditsWindow.mainloop()
