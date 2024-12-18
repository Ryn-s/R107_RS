nombre = int(input("Entrez un nombre entier: "))

if nombre > 0:
    if nombre % 2 == 0:
        print("Le nombre est positif et pair")
    else:
        print("Le nombre est positif et impair")
elif nombre < 0:
    if nombre % 2 == 0:
        print("Le nombre est négatif et pair")
    else:
        print("Le nombre est négatif et impair")
else:
    print("Le nombre est zéro (et il est pair)")
