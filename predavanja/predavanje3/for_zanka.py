imena = ["Anže", "Benjamin", "Cilka", "Dani", "Eva", "Franc"]
teze = [74, 83, 58, 66, 61, 84]

for ime in imena:
    print(ime)

najmanjsa = None
for teza in teze:
    if najmanjsa is None or najmanjsa > teza:
        najmanjsa = teza
print(najmanjsa)

for c in "Franc":
    print(c)

stevila = [44, 48, 42, 12, 7, 8, 10, 78, 88]
sodo = False
for x in stevila:
    if x % 2 == 1:
        print("Imamo liho število:", x)
        break
else:
    print("Sama soda")

# for zanka, zapisana z while:
g = iter(stevila)
# naslednji = next(g)
naslednji = None
while naslednji is not None:
    print(naslednji)
    next(g)
# ta je boljša, zahteva samo iterator

# for po številih --- šteje
for x in range(0, 10):
    print(x)
# ta je slabša, ker zahteva,da so elementi seznama dostopni z indeksom in ima dolžino
# tudi se lahko zgubiš v indeksih


# continue:
for x in stevila:
    if x == 0:
        break  # skoči iz zanke
    if x > 42:
        continue  # skoči na začetek zanke
    print(x)

# prejšnji element v for zanki z iteratorjem
vsota = 0
for x, prej in zip(stevila, stevila[1:]):
    if x > prej:
        vsota += x - prej
print(vsota)

# enumerate
for i, crka in enumerate("Benjamin"):
    print(i, crka)

