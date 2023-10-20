filmi = [
    ('Poletje v skoljki 2', 6.1),
    ('Ne cakaj na maj', 7.3),
    ('Pod njenim oknom', 7.1),
    ('Kekec', 8.1),
    ('Poletje v skoljki', 7.2),
    ('To so gadi', 7.7),
]
ocena_7 = []
ocena_najvisje = ""
najvisja_ocena = 0
ocena_7_prvi = ""
ocena_povprecje = 0
film_sequel = []
for naslov, ocena in filmi:
    if ocena > 7:
        ocena_7.append(naslov)
        if ocena_7_prvi == "":
            ocena_7_prvi = ocena
    if ocena > najvisja_ocena:
        ocena_najvisje = naslov
        najvisja_ocena = ocena
    ocena_povprecje += ocena
    for naslov1, _ in filmi:
        if naslov in naslov1 and naslov1 != naslov:
            film_sequel.append(naslov)
ocena_povprecje /= len(filmi)
print("Filmi z oceno, višjo od 7:")
for film in ocena_7:
    print("    ", film)
print("Film z najvišjo oceno:", ocena_najvisje)
print("Prvi film z oceno, višjo od 7:", ocena_7_prvi)
print("Povprečna ocena:", ocena_povprecje)
print("Filmi z drugim delom:")
for film in film_sequel:
    print("    ", film)
