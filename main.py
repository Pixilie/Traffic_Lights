# Compatibility with Python 2 and 3
try:
    import tkinter
    from tkinter import *
except ImportError:
    import Tkinter as tkinter
    from Tkinter import *
# Import other files from the game
import Levels.select as lvl

# Main window setup
main_window = tkinter.Tk()

# Screen info
screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()

# Main window setting
main_window.title("Traffic Light")
main_window.config(background='#B78BC4')
main_window.attributes('-fullscreen', True)


# Exit button
def Close():
    main_window.destroy()


# Levels button #TODO: Terminer fonction, chercher importer un autre fichier
def Levels():
    main_window.destroy()


# Settings button #TODO: Terminer fonction, chercher importer un autre fichier
def Settings():
    main_window.destroy()


# Credits button #TODO: Terminer fonction, chercher importer un autre fichier
def Credits():
    main_window.destroy()


# Main frame
frame = Frame(main_window, bg='#B78BC4')


# Title
title_icon = PhotoImage(file="./Assets/Icons/TRAFFIC LIGHT.png")
title = Canvas(main_window, width=1400, height=600,
               bg='#B78BC4', bd=0, highlightthickness=0)
title.create_image(screen_width/2.8, screen_height/4.7, image=title_icon)
title.pack(pady=20)

# Button for closing
exit_icon = PhotoImage(
    file='./Assets/Icons/exit_icon2.png', width=100, height=71)  # TODO: enlever bordure quand survoler
exit_button = Button(main_window, image=exit_icon,
                     bd=0, bg='#B78BC4', highlightthickness=0, command=Close)
exit_button.pack(pady=800)
exit_button.place(x=screen_width/1.05, y=screen_height/1.075)

# Levels Button #TODO:son quand survoler ou cliquer
levels_button = Button(main_window, text="Niveaux", font=('Arial', 30),
                       bd=0, bg='#B78BC4', fg="#ffffff", width=10, command=Levels)
levels_button.pack(pady=20)
levels_button.place(x=screen_width/2.3, y=screen_height/2.9)

# Setting Button #TODO:son quand survoler ou cliquer
setting_button = Button(main_window, text="Paramètres", font=('Arial', 30),
                        bd=0, bg='#B78BC4', fg="#ffffff", width=10, command=Settings)
setting_button.pack(pady=20)
setting_button.place(x=screen_width/2.3, y=screen_height/2.3)

# Credits Button #TODO:son quand survoler ou cliquer
credits_button = Button(main_window, text="Crédits", font=('Arial', 30),
                        bd=0, bg='#B78BC4', fg="#ffffff", width=10, command=Credits)
credits_button.pack(pady=20)
credits_button.place(x=screen_width/2.3, y=screen_height/1.9)

# Compiling the main frame
frame.pack(expand=YES)
main_window.mainloop()
