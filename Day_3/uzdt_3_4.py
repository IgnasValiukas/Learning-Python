#Pakeisti 1 užduoti taip, kad neteisingai įvedus duomenis ar įvykus klaidoms,
# programos mestų norimas klaidas lietuvių kalba (panaudoti try/except)

main_loop = True
while main_loop:
    try:
        integer = int(input("Add integer number: "))
        if integer > 0:
            ar_skaicius_teigiamas = True
            print(ar_skaicius_teigiamas)
        elif integer <= 0:
            ar_skaicius_teigiamas = False
            print(ar_skaicius_teigiamas)
    except ValueError:
        print("\nInput must be Integer!")
    while True:
        options = input("Do you want to continue? y/n\n")
        if options == "y" or options == "Y":
            break
        elif options == "n" or options == "N":
            main_loop = False
            break
        else:
            print("\n!Invalid option: must be Y/y or N/n\n")





