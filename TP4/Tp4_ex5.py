date = input("Entrez une date (jjmmaaaa) : ")

if len(date) != 8 or not date.isdigit():
    print("Format invalide. Veuillez entrer une date sous la forme jjmmaaaa.")
else:
    jour, mois, annee = int(date[:2]), int(date[2:4]), int(date[4:])
    bissextile = (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)
    jours_mois = [31, 29 if bissextile else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if mois < 1 or mois > 12 or jour < 1 or jour > jours_mois[mois - 1]:
        print("Date invalide.")
    else:
        print("Date valide.")
