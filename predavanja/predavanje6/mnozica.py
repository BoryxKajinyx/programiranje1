# prazna množica
set()

# neprazna množica
imena = {"Ana", "Berta", "Cilka", "Dani"}
stevilke = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Množice ne poznajo vrstnega reda.
# Do elementov se ne more dostopat z indeksi. Uporabi se npr. for zanko.

# dodajanje v množico
imena.add("Benjamin")

# odstranjevanje iz množic:
stevilke.remove(9)

# množice lahko vsebujejo samo stvari, ki se ne spremenijo:
terke = {(1, 2, 3), (2, 3, 4), (1, 2, 3)}  # to deluje
# množice ne morajo vsebovati seznamov, množic, slovarjev, ker za te tipe ne more izračunati hash.

mn1 = {1, 2, 3}
mn2 = {3, 4, 5}
mn3 = {2, 3}
# operacije:
print(mn1 & mn2)  # presek

print(mn1 | mn2)  # unija

print(mn1 > mn3)  # mn1 nadmnožica mn3

print(mn3 < mn1)  #
