teza = int(input("Teža:"))
visina = float(input("Višina:"))
if visina > 10:
    visina = visina / 100
bmi = round(teza / visina ** 2)
print("Vas itm je ", bmi)
if 18 < bmi < 25 and True:
    print("Pridni ste")
if bmi > 25:
    print("Treba bo shujšat!")
    print("Resno mislim!")
elif bmi == 25:
    print(" na meji ste")
elif bmi > 18:
    print("Še naprej se prehranjujte tako kot prej")
else:
    print("Jejte več!")
print("Pregled je končan.")
