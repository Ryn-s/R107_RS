nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
notes = []

for i in range(nombreEtudiants):
    note = -1
    while note < 0 or note > 20:
        note = float(input(f"Note etudiant {i} : "))
    notes.append(note)

moyenne = sum(notes) / nombreEtudiants
print(f"Moyenne de classe : {moyenne:.2f}")

print("Numéro de l’Etudiant | note | ecart a la moyenne")
for i, note in enumerate(notes):
    ecart = note - moyenne
    print(f"{i} | {note:.1f} | {ecart:.2f}")
