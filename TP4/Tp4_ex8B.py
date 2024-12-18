binome = {
    "etudiant1": {"firstname": "Toto", "name": "Titi", "promo": 2024, "group": 101},
    "etudiant2": {"firstname": "Tata", "name": "Tutu", "promo": 2024, "group": 102},
}

print("Les étudiants formant le binôme sont :")
for key, value in binome.items():
    print(f"- L'étudiant {value['firstname']} {value['name']} du groupe {value['group']}")
