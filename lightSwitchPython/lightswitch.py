from tkinter import *

def handle_click(event):
    if gui["bg"] == "black":
        gui.configure(bg = "yellow")
        print('licht is aan')
        button["text"] = "licht is aan"
        button["bg"] = "black"
        button["fg"] = "yellow"
    else:
        gui.configure(bg = "black")
        print('light is uit')
        button["text"] = "licht is uit"
        button["bg"] = "yellow"
        button["fg"] = "black"


gui = Tk(className='lamp')
gui.geometry("200x200")

gui.configure(bg = "black")

button = Button(
    gui,
    text="click hier!!!",
    bg = "yellow",
    fg="black"
)

button.bind("<Button-1>", handle_click)
button.pack(pady = 50, padx = 40,)

gui.mainloop()