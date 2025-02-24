# Patobulinti 3 užduoties programą, kad ji turėtų statuso juostą apačioje, kurioje:
# Būtų rodoma "Sukurta", kai atspausdinamas pasisveikinimo tekstas
# Būtų rodoma "Išvalyta", kai ištrinamas pasisveikinimo tekstas
# Būtų rodoma "Atkurta", kai atkuriamas paskutinis pasisveikinimo tekstas
# Nuspaudus klaviatūros mygtuką "Escape", uždarytų programos langą
from tkinter import *

window = Tk()
frame = Frame(window)
frame.pack()

bottom_frame = Frame(window)
bottom_frame.pack(side=BOTTOM)


# funkcijos
def confirm(event):
    input_data = input_field.get()
    label["text"] = f'Labas, {input_data}!'
    status["text"] = "Created"


def clear_input():
    label["text"] = ""
    status["text"] = "Cleared"


def restore_input():
    label["text"] = f'Labas, {input_field.get()}!'
    status["text"] = "Restored"


def close_window(event):
    window.destroy()


# menu
menu1 = Menu(window)
window.config(menu=menu1)
submenu = Menu(menu1, tearoff=0)

# window content
text_1 = Label(frame, text="Name")
input_field = Entry(frame)
button = Button(frame, text="Confirm")
button.bind("<Button-1>", confirm)
label = Label(bottom_frame, text="")

# window actions
window.bind("<Return>", confirm)
window.bind("<Escape>", lambda event: close_window(event))

# submenu content
menu1.add_cascade(label="Menu", menu=submenu)
submenu.add_command(label="Clear", command=clear_input)
submenu.add_command(label="Restore", command=restore_input)
submenu.add_separator()
submenu.add_command(label="Leve", command=window.destroy)

# window element positions
text_1.pack(side=LEFT)
input_field.pack(side=LEFT)
button.pack(side=LEFT)
label.pack()

# status
status = Label(bottom_frame, text="Waiting...")
status.pack(fill=X)

window.mainloop()
