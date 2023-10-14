from math import *

stevilo = int(input("Vnesi število:"))
koren = sqrt(stevilo)

if koren % 1 == 0:
    print("Število je kvadrat")
else:
    print("Število ni kvadrat")