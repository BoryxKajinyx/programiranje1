from math import *

kocke = int(input("Vnesi število kock:"))
koren = sqrt(kocke)
skatla = 0
if koren % 1 == 0:
    skatla = int(koren)
else:
    skatla = int(koren) + 1
print("Potrebuješ škatlo širine", skatla)