tovor = int(input("Vnesi količino tovora:"))
vsota = 0
korak = 0
while tovor > 0:
    tovor = tovor // 3 - 2
    korak += 1
    vsota += max(0, tovor)
print(korak)
print(vsota)
