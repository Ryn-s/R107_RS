notes = []
coefficients = []

for i in range(1, 6):
    saisie = input(f"Veuillez entrer la note du module {i} et le coefficient correspondant (ex : 10.5 2) : ")
    note, coeff = map(float, saisie.split())
    notes.append(note)
    coefficients.append(coeff)

moyenne = sum(note * coeff for note, coeff in zip(notes, coefficients)) / sum(coefficients)

if moyenne > 10 and all(note >= 8 for note in notes):
    print(f"L'étudiant est admis avec une moyenne de {moyenne:.2f}")
else:
    print(f"L'étudiant n'est pas admis. Moyenne : {moyenne:.2f}")
