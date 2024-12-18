montant = int(input("Entrez une somme en euros : "))
billets_100 = montant // 100
montant %= 100
billets_50 = montant // 50
montant %= 50
billets_10 = montant // 10
montant %= 10
pieces_2 = montant // 2
pieces_1 = montant % 2

print(f"{billets_100} billets de 100, {billets_50} de 50, {billets_10} de 10, {pieces_2} pièces de 2, et {pieces_1} pièce de 1.")
