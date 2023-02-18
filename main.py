import tkinter
from tkinter import *
# import level_selector as lvl

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
    # lvl.start()


# Levels button #TODO: Terminer fonction, chercher importer un autre fichier
def Levels():
    main_window.destroy()


# Button for closing
exit_icon = PhotoImage(
    file='./Assets/Icons/exit_icon2.png', width=128, height=130)  # TODO: Redimensionner l'image de base plus changer les dimensions dans le code
exit_button = Button(main_window, image=exit_icon,
                     bd=0, bg='#B78BC4', command=Close)
exit_button.pack(pady=800)
exit_button.place(x=1400, y=5)

# Main frame
frame = Frame(main_window, bg='#B78BC4')

# Title
width = 1200
height = 400
title_icon = PhotoImage(file="./Assets/Icons/TRAFFIC LIGHT.png")
canvas = Canvas(main_window, width=width, height=height,
                bg='#B78BC4', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=title_icon)
canvas.pack(pady=20)

# Levels Button #TODO: Terminer design bouton
levels_button = Button(main_window, text="Levels", font=('Arial', 40),
                       bd=0, bg='#B78BC4', command=Levels)
levels_button.pack(pady=20)
levels_button.place(x=screen_width/2.1, y=screen_height/3)

# Compiling the main frame
frame.pack(expand=YES)
main_window.mainloop()
