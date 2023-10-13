tovor = int(input("Vnesi količino tovora:"))
vsota=0
korak = 0
while tovor > 0:
    tovor = tovor // 3 - 2
    vsota += tovor
    korak += 1
print(korak)
print(vsota)