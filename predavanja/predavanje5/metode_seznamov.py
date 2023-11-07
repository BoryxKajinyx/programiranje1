
seznam = ["Benjamin", "Cilka", 2, 3, True]

# count vrne, kolikokrat se podan element pojavi v njem
print(seznam.count("Benjamin"))

# index vrne mesto prve ponovitve elementa v seznamu
# ne ga uporabit
print(seznam.index(True))

# append na konec seznama doda podan element
seznam.append("Janez")

# insert vrine element v seznam na določeno mesto
seznam.insert(3, 4)

# extend doda elemente podanega seznama v seznam
# isto dela += in +
seznam.extend(["Jože", False])

# del odstrani elemente v seznamu na podanih mestih
del seznam[-1]

# pop vrne in zbriše zadnji element seznama oziroma podano število elementov na koncu
seznam.pop()
seznam.pop(2)

# remove odstrani prvo pojavitev podanega elementa iz seznama
# izogibaj se uporabi
seznam.remove("Cilka")

# sort uredi elemente seznama, če jih je možno primerjat, glede na podan ključ
seznam.sort()
seznam.sort(reverse=True)

# sorted uredi podan seznam in ga vrne
print(sorted(seznam))

# reversed vrne iterator z obrnjenim seznamom
print(list(reversed(seznam)))
