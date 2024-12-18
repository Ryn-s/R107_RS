nMax = 3
n = 0
while n < 1 or n > nMax:
    n = int(input(f"Quelle est la taille de vos vecteurs [entre 1 et {nMax}] ? "))

v1 = []
v2 = []

print("Saisie du premier vecteur :")
for i in range(n):
    v1.append(int(input(f"v1[{i}] = ")))

print("Saisie du second vecteur :")
for i in range(n):
    v2.append(int(input(f"v2[{i}] = ")))

produit_scalaire = sum(v1[i] * v2[i] for i in range(n))
print(f"Le produit scalaire de v1 par v2 vaut {produit_scalaire}")
