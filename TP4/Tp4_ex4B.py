L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

max_freq = 0
max_nombre = None
for nombre in L1:
    freq = L1.count(nombre)
    if freq > max_freq:
        max_freq = freq
        max_nombre = nombre

print(f"Le nombre le plus frequent dans la liste est le : {max_nombre} ({max_freq} x)")
