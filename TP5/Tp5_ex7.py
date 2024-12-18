import os
from datetime import datetime

fichier1 = input("Entrez le chemin du premier fichier : ")
fichier2 = input("Entrez le chemin du deuxième fichier : ")

if os.path.isfile(fichier1) and os.path.isfile(fichier2):
    taille1 = os.path.getsize(fichier1)
    taille2 = os.path.getsize(fichier2)
    date1 = os.path.getmtime(fichier1)
    date2 = os.path.getmtime(fichier2)

    print(f"Taille de {fichier1} : {taille1} octets")
    print(f"Taille de {fichier2} : {taille2} octets")

    if date1 > date2:
        print(f"{fichier1} est le plus récent, modifié le {datetime.fromtimestamp(date1)}")
    else:
        print(f"{fichier2} est le plus récent, modifié le {datetime.fromtimestamp(date2)}")
else:
    print("Un ou les deux fichiers n'existent pas.")
