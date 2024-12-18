nom1 = input("Entrez le nom de la première personne : ").upper()
prenom1 = input("Entrez le prénom de la première personne : ").capitalize()
nom2 = input("Entrez le nom de la deuxième personne : ").upper()
prenom2 = input("Entrez le prénom de la deuxième personne : ").capitalize()

personnes = [(nom1, prenom1), (nom2, prenom2)]
personnes.sort()

for nom, prenom in personnes:
    print(f"{prenom} {nom}")
