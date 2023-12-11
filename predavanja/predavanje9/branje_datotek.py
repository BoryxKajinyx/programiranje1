import random

f = open("besedilo")
d = open("../../drugo/drugo.dic")
for vrstica in d:
    print(vrstica[:-1])
# datoteka je prebrana in jo je treba za ponovno branje spet odpret
# readline se uporabi, ko ima kakšna vrstica različen pomen (header, ...)
# readlines razdeli preostanek datoteke v seznam po vrsticah
# read prebere cel preostanek datoteke v en niz
