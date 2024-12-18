debut = int(input("Donnez l’heure de début de la location (un entier) : "))
fin = int(input("Donnez l’heure de fin de la location (un entier) : "))

if debut < 0 or fin < 0 or debut > 24 or fin > 24:
    print("Les heures doivent être comprises entre 0 et 24 !")
elif debut == fin:
    print("Attention ! l’heure de fin est identique à l’heure de début.")
elif debut > fin:
    print("Attention ! le début de la location est après la fin ...")
else:
    tarif_1 = 0
    tarif_2 = 0

    for heure in range(debut, fin):
        if 0 <= heure < 7 or 17 <= heure < 24:
            tarif_1 += 1
        else:
            tarif_2 += 1

    total = tarif_1 * 1 + tarif_2 * 2

    print(f"Vous avez loué votre vélo pendant")
    if tarif_1 > 0:
        print(f"{tarif_1} heure(s) au tarif horaire de 1.0 euro(s)")
    if tarif_2 > 0:
        print(f"{tarif_2} heure(s) au tarif horaire de 2.0 euro(s)")
    print(f"Le montant total à payer est de {total:.1f} euro(s).")
