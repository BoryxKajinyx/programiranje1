stevilo_izdelkov = int(input("Vnesi število izdelkov:"))
vsota = 0
for x in range(0, stevilo_izdelkov):
    vsota += float(input("Cena izdelka:"))
print("Vsota:", vsota)
