L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

frequence = {}
for nombre in L1:
    if nombre in frequence:
        frequence[nombre] += 1
    else:
        frequence[nombre] = 1

max_val = max(frequence.values())
for nombre, freq in frequence.items():
    if freq == max_val:
        print(f"Le nombre le plus frequent dans la liste est le : {nombre} ({freq} x)")
        break
