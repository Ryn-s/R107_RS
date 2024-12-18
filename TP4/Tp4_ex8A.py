dico = {"firstname": "Toto", "name": "Titi", "promo": 2024, "group": 101}
print(f"Votre nom est '{dico['name']}', prénom est '{dico['firstname']}', vous faites partie de la promo '{dico['promo']}' et votre groupe est '{dico['group']}'.")

print("Les clés du dictionnaire sont :")
for key in dico.keys():
    print(f"- {key}")

print("Les valeurs du dictionnaire sont :")
for value in dico.values():
    print(f"- {value}")

print("Les tuplets du dictionnaire sont :")
for item in dico.items():
    print(f"- {item}")
