chaine = input("Entrez une chaîne de caractères : ")


taille = 0
for c in chaine:
    taille += 1
print(f"Taille de la chaîne : {taille}")


voyelles = "aeiouyAEIOUY"
compteur_voyelles = sum(1 for c in chaine if c in voyelles)
pourcentage_voyelles = (compteur_voyelles / taille) * 100
print(f"Pourcentage de voyelles : {pourcentage_voyelles:.2f}%")


mot = "wagon"
occurences = 0
positions = []

for i in range(taille - len(mot) + 1):
    if chaine[i:i+len(mot)] == mot:
        occurences += 1
        positions.append(i)

if occurences > 0:
    print(f"'{mot}' est une sous-chaîne, première occurrence à la position {positions[0]}")
else:
    print(f"'{mot}' n'est pas une sous-chaîne.")

print(f"Nombre d'occurrences de '{mot}' : {occurences}")
