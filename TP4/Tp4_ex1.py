nombre = float(input("Vous cherchez la table de multiplication de quel nombre ? "))
table = [round(nombre * i, 1) for i in range(10)]
for i, val in enumerate(table):
    print(f"{nombre} * {i} = {val}")
