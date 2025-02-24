# Turėtų laukelį su užrašu "Įveskite vardą", kuriame vartotojas galėtų įvesti vardą
# Turėtų mygtuką su užrašu "Patvirtinti", kurį nuspaudus, programa po lauku atspausdintų "Labas, {vardas}!"

from tkinter import *

window = Tk()


def confirm():
    input_data = input_field.get()
    result["text"] = f'Labas, {input_data}!'


text_1 = Label(window, text="Name")
input_field = Entry(window)
button = Button(window, text="Confirm", command=confirm)
result = Label(window, text="")

text_1.grid(row=0, column=0, sticky=E)
input_field.grid(row=0, column=1)
button.grid(row=0, column=3)
result.grid(row=2, column=1)
window.mainloop()
