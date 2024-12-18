BASE = 4
fromage = 800.0
eau = 2.0
ail = 2
pain = 400

nbConvives = int(input("Entrez le nombre de personne(s) conviées à la fondue : "))

fromage = fromage * nbConvives / BASE
eau = eau * nbConvives / BASE
ail = ail * nbConvives / BASE
pain = pain * nbConvives / BASE

print(f"Pour faire une fondue fribourgeoise pour {nbConvives} personnes, il vous faut :")
print(f"- {fromage} gr de fromage")
print(f"- {eau} dl d'eau")
print(f"- {ail} gousse(s) d'ail")
print(f"- {pain} gr de pain")
