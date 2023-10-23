ovire = [(1, 3, 6), (2, 4, 3), (4, 6, 7),
         (3, 4, 9), (6, 9, 5), (9, 10, 2), (9, 10, 8),]
izbrani_stolpec = 6


sirina = 0
prva_ovira = None
for x1, x2, y in ovire:
    sirina = max(sirina, x2)
    if (x1 <= izbrani_stolpec <= x2) and prva_ovira is None:
        prva_ovira = y
    elif (x1 <= izbrani_stolpec <= x2) and prva_ovira is not None:
        prva_ovira = min(prva_ovira, y)

najdlje = None
najdaljsi_stolpec = 0

for stolpec in range(1, sirina + 1):
    najdlje_zacasno = None
    for x1, x2, y in ovire:
        if (x1 <= stolpec <= x2) and najdlje_zacasno is None:
            najdlje_zacasno = y
        elif (x1 <= stolpec <= x2) and najdlje_zacasno is not None:
            najdlje_zacasno = min(najdlje_zacasno, y)
    if najdlje_zacasno is None:
        najdlje = najdlje_zacasno
        najdaljsi_stolpec = stolpec
        break
    elif najdlje is None or najdlje_zacasno > najdlje:
        najdlje = najdlje_zacasno
        najdaljsi_stolpec = stolpec


print(prva_ovira)
if najdlje is None:
    najdlje = "Zmaga"
print(str(najdaljsi_stolpec)+",", najdlje)
