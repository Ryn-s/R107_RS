X = int(input("Entrez une valeur pour X (> 1) : "))
somme = 0
N = -1
while somme <= X:
    N += 1
    somme += N
print(f"Le plus grand N tel que la somme <= {X} est {N - 1}")
