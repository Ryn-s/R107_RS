tab = [5, 2, 4, 8, 1, 3]
print(tab)

for i in range(len(tab)):
    for j in range(i + 1, len(tab)):
        if tab[j] < tab[i]:
            tab[i], tab[j] = tab[j], tab[i]
    print(tab)
