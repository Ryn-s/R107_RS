minutes_ecoulees = int(input("Entrez le nombre de minutes écoulées depuis le début du mois:"))
jour = minutes_ecoulees// (24*60) + 1
reste_minutes = minutes_ecoulees % (24*60)
heure = reste_minutes// 60
minute = reste_minutes % 60
print(f"La date associée est : jour {jour}, heure {heure}, minute {minute}")