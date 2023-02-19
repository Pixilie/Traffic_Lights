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
    file='./Assets/Icons/exit_icon2.png', width=170, height=120)  # TODO: bordure + fond quand survoler + image en blanc
exit_button = Button(main_window, image=exit_icon,
                     bd=0, bg='#B78BC4', command=Close)
exit_button.pack(pady=800)
exit_button.place(x=screen_width/1.08, y=screen_height/1.12)

# Main frame
frame = Frame(main_window, bg='#B78BC4')

# Title #TODO: Taille ?
title_icon = PhotoImage(file="./Assets/Icons/TRAFFIC LIGHT.png")
canvas = Canvas(main_window, width=1300, height=500,
                bg='#B78BC4', bd=0, highlightthickness=0)
canvas.create_image(screen_width/3, screen_height/4.5, image=title_icon)
canvas.pack(pady=20)

# Levels Button #TODO: Terminer design bouton (même police que le titre, bordure, fond quand survoler)
levels_button = Button(main_window, text="Levels", font=('Arial', 50),
                       bd=0, bg='#B78BC4', fg="#ffffff", command=Levels)
levels_button.pack(pady=20)
levels_button.place(x=screen_width/2.2, y=screen_height/2.7)

# Compiling the main frame
frame.pack(expand=YES)
main_window.mainloop()
