import random

nombre_mystere = random.randint(0, 100)
tentatives = 0
trouve = False

while not trouve:
    tentative = int(input("Devinez le nombre mystère (entre 0 et 100) : "))
    tentatives += 1
    if tentative < nombre_mystere:
        print("Plus grand !")
    elif tentative > nombre_mystere:
        print("Plus petit !")
    else:
        print(f"Bravo ! Vous avez trouvé en {tentatives} tentative(s).")
        trouve = True
