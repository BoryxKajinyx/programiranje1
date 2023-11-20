from itertools import *


sezn1 = [1, 2, 3, 4, 5]

# pairwise naredi terke z naslednjim elementom
for x1, x2 in pairwise(sezn1):
    print(x1, x2)

# cycle ponavlja seznam
for n, x in enumerate(cycle(sezn1)):
    print(x)
    if n > 100:
        break

# repeat ponavlja vrednost
repeat(1)


# chain naredi verigo iz elementov podanih stvari z elementi
for x in chain("12", (3, 4), [5, 6], {7, 8}, {9: 1, 10: 1}, range(11, 20)):
    print(x)

# count šteje od začetne vrednosti dalje
stevec = count()
next(stevec)

# zip_longest dela isto kot zip, ampak dela do konca daljšega iteratorja / generatorja
for x in zip_longest(sezn1, sezn1 + sezn1):
    print(x)

# takewhile generira elemente danega iteratorja, dokler ne naleti na pogoj
for x in takewhile(lambda y: y < 4, sezn1):
    print(x)


# dropwhile generira elemente danega iteratorja po prvem elementu, ki izpolni pogoj
for x in dropwhile(lambda y: y < 4, sezn1):
    print(x)
