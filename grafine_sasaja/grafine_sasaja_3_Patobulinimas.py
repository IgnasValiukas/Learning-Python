# Patobulinti 2 užduoties programą, kad ji turėtų meniu pavadinimu "Meniu", kuriame:
# Būtų punktas "Išvalyti", kurį paspaudus išsitrintų tekstas eilutėje, kurioje spausdinamas pasisveikinimo tekstas
# Būtų punktas "Atkurti", kurį paspaudus pasisveikinimo teksto eilutėje butų atspausdintas paskutinis atspausdintas tekstas
# Būtų punktas "Išeiti", kurį paspaudus užsidarytų programos langas
# Tarp menių punktų "Atkurti" ir "Išeiti" būtų atskyrimo brūkšnys
from tkinter import *

window = Tk()
frame = Frame(window)
frame.pack()

bottomframe = Frame(window)
bottomframe.pack(side = BOTTOM)

# funkcijos
def confirm(event):
    input_data = input_field.get()
    label["text"] = f'Labas, {input_data}!'

def clear_input():
    label["text"] = ""

def restore_input():
    label["text"] = f'Labas, {input_field.get()}!'


# menu
menu1 = Menu(window)
window.config(menu=menu1)
submenu = Menu(menu1, tearoff=0)

# input
text_1 = Label(frame, text="Name")
input_field = Entry(frame)
button = Button(frame, text="Confirm")
button.bind("<Button-1>", confirm)
window.bind("<Return>", confirm)
label = Label(bottomframe, text="")

# submenu content
menu1.add_cascade(label="Menu", menu=submenu)
submenu.add_command(label="Clear", command=clear_input)
submenu.add_command(label="Restore", command=restore_input)
submenu.add_separator()
submenu.add_command(label="Leve", command=window.destroy)

# input grid
text_1.pack(side = LEFT)
input_field.pack(side = LEFT)
button.pack(side = LEFT)
label.pack(side = BOTTOM)

window.mainloop()

