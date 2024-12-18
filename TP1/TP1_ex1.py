nom = "Dupont"
prenom = "Jean"
math = 15.5
anglais = 14.0
info = 16.0
promotion = 2023
moy = (math + anglais + info) / 3

print("Type de nom :", type(nom))
print("Type de prenom :", type(prenom))
print("Type de math :", type(math))
print("Type de anglais :", type(anglais))
print("Type de info :", type(info))
print("Type de promotion :", type(promotion))
print("Type de moy :", type(moy))

print(f"L’étudiant {nom} {prenom} de la promotion {promotion} a une moyenne de {moy:.2f}")
