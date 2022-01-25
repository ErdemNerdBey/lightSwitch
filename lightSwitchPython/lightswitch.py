from tkinter import *

def handle_click(event):
    if gui["bg"] == "black":
        gui.configure(bg = "yellow")
        print('light is aan')
    else:
        gui.configure(bg = "black")
        print('light is uit')

gui = Tk(className='lamp')

gui.geometry("200x200")

gui.configure(bg = "black")

button = Button(
    gui,
    text="click hier!!!",
    bg = "white",
    fg="black"
)

button.bind("<Button-1>", handle_click)
button.pack(pady = 50, padx = 40,)

gui.mainloop()