from modules.biudzetas import Biudzetas

biudzetas = Biudzetas()

while True:
    pasirinkimas = int(input("Pasirinkite: \n1 - Įvesti pajamas \n2 - Įvesti išlaidas \n3 - Peržiūrėti balansą \n4 - Rodyti ataskaitą \n5 - Išeiti\n"))

    if pasirinkimas == 1:
        suma = float(input("Įveskite pajamų sumą: "))
        siuntejas = input("Siuntėjas: ")
        papildoma_info = input("Papildoma informacija: ")
        biudzetas.prideti_pajamu_irasa(suma, siuntejas, papildoma_info)

    elif pasirinkimas == 2:
        suma = float(input("Įveskite išlaidų sumą: "))
        atsiskaitymo_budas = input("Atsiskaitymo būdas: ")
        isigyta_preke = input("Įsigyta prekė/paslauga: ")
        biudzetas.prideti_islaidu_irasa(suma, atsiskaitymo_budas, isigyta_preke)

    elif pasirinkimas == 3:
        print(f"Balansas: {biudzetas.gauti_balansa()} EUR")

    elif pasirinkimas == 4:
        biudzetas.parodyti_ataskaita()

    elif pasirinkimas == 5:
        break
    else:
        print("Neteisingas pasirinkimas, bandykite dar kartą.")
