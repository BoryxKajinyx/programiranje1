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

stevila = [44, 48, 12, 7, 8, 10, 78, 88]
sodo = False
for x in stevila:
    if x % 2 == 1:
        print("Imamo liho število:", x)
        break
else:
    print("Sama soda")





