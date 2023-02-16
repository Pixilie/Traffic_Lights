import tkinter
from tkinter import *
# Programme principal
#  création de la fenêtre principale
main_window = tkinter.Tk()

#  paramètres de la fenêtre
main_window.title("Traffic Light")
main_window.config(background='#B78BC4')
main_window.attributes('-fullscreen', True)


#exit_Button

def Close():
    main_window.destroy()
  
  
# Button for closing
image_exit= PhotoImage(file='app_icon\exit_icon.png', width=128, height=130)
exit_button = Button(main_window,image=image_exit, bd=0, bg='#B78BC4',command=Close)
exit_button.pack(pady=800)
exit_button.place(x= 1400, y=5)

#Main_Frame
frame = Frame(main_window, bg='#B78BC4')

#Title
width = 1200
height = 400
image = PhotoImage(file="app_icon\TRAFFIC LIGHT.png")
canvas = Canvas(main_window, width=width, height=height, bg='#B78BC4', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.pack(pady=20)

# enpacktage
frame.pack(expand=YES)
main_window.mainloop()
 