vsota = 0
stevilo_izdelkov = 0
cena = -1

while vsota < 100 and stevilo_izdelkov < 10 and cena != 0:
    cena = float(input("Cena izdelka:"))
    vsota += cena
    if cena != 0:
        stevilo_izdelkov += 1
print("Porabili boste", vsota, "evrov za", stevilo_izdelkov, "stvari")
