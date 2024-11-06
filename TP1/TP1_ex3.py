jour=int(input("Entrez le jour du mois (1 à 31):"))
heure = int(input("Entrez l'heure(0 à 23)"))
minute = int(input("Entrez les minutes(0 à 59)"))
minutes_ecoulees= (jour-1)*24*60 + heure * 60 + minute
print("Nombres de minutes écoulées depuis le début du mois:", minutes_ecoulees)
