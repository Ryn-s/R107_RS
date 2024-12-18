n = int(input("Entrez un entier positif : "))
choix = input("Utiliser une boucle (for/while) ? ")

if choix == "for":
    factorielle = 1
    for i in range(1, n + 1):
        factorielle *= i
        print(f"Factorielle intermédiaire à l'étape {i} : {factorielle}")
elif choix == "while":
    factorielle = 1
    i = 1
    while i <= n:
        factorielle *= i
        print(f"Factorielle intermédiaire à l'étape {i} : {factorielle}")
        i += 1

print(f"La factorielle de {n} est {factorielle}")
