binome = ("login1", "login2")
print(f"L’étudiant {binome[0]} est en binome avec l’étudiant {binome[1]}")


binome = (binome[0], "nouveau_login")
print(binome)


trinome = binome + ("login3",)
print(trinome)
