inferieur_10 = 0
entre_10_15 = 0
superieur_15 = 0

for i in range(10):
    valeur = -1
    while valeur < 0 or valeur > 20:
        valeur = float(input(f"Entrez la valeur {i + 1}/10 (entre 0 et 20) : "))
    if valeur < 10:
        inferieur_10 += 1
    elif valeur < 15:
        entre_10_15 += 1
    else:
        superieur_15 += 1

print(f"Nombre de valeurs < 10 : {inferieur_10}")
print(f"Nombre de valeurs entre 10 et 15 : {entre_10_15}")
print(f"Nombre de valeurs >= 15 : {superieur_15}")
