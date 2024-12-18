jour = int(input("Saisir le jour du mois : "))
heure = int(input("Saisir l'heure (entre 0 et 23) : "))
minute = int(input("Saisir les minutes (entre 0 et 59) : "))

minutes_total = (jour - 1) * 24 * 60 + heure * 60 + minute

print(f"Nombre de minutes écoulées depuis le début du mois : {minutes_total}")
