# Sukurkite programą, kuri,
# gavusi nuorodą į katalogą:
# praiteruos visus jame esančius failus,
# išrinks nuotraukas,
# pakeis dydį pagal jūsų nurodytą aukštį išlaikant proporcijas,
# kiekvienos nuotraukos apatiniame dešiniajame kampe įdės logotipą,
# tą kurį išsisaugojote pirmoje užduotyje.
# Naudokite .resize, kadangi nuotrauką galbūt reikės padidinti, nebūtinai tik sumažinti.

import os


# path_input = input("Copy paste your folder path: ")
def image_finder(path):
    os.chdir(path)
    folder_list = os.listdir()
    index = 0
    while True:
        try:
            a = folder_list[index]
            yield a
            index += 1
        except IndexError:
            break


folder_path = 'D:/2025/Study/CodeAcademy/Files'
file = image_finder(folder_path)
image_formats = [".jpg", ".png", ".jpeg"]
while True:
    try:
        print(next(file))
    except StopIteration:
        break

# i=0
# while True:
#     try:
#         print(folder_list[i])
#         i+=1
#     except IndexError:
#         break


# folder_path = r"D:/2025/Study/CodeAcademy/Files"
# print(os)
