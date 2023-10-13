vsota = 0
cena = -1
stevilo_izdelkov = -1
while cena != 0:
    cena = float(input("Cena izdelka:"))
    vsota += cena
    stevilo_izdelkov += 1
print("Vsota:", vsota)
print("Povprečna cena:", vsota / stevilo_izdelkov)
