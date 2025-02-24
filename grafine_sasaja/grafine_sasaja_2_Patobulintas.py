# Patobulinti 1 užduoties programą, kad ji:
# Atspausdintų pasisveikinimą ne tik nuspaudus mygtuką, bet ir paspaudus mygtuką "Enter"

from tkinter import *

window = Tk()


def confirm(event):
    input_data = input_field.get()
    result["text"] = f'Labas, {input_data}!'


text_1 = Label(window, text="Name")
input_field = Entry(window)
button = Button(window, text="Confirm")
button.bind("<Button-1>", confirm)
window.bind("<Return>", confirm)
result = Label(window, text="")

text_1.grid(row=0, column=0, sticky=E)
input_field.grid(row=0, column=1)
button.grid(row=0, column=2)
result.grid(row=2, column=1)
window.mainloop()
