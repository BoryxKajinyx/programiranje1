stevilo = int(input("Vnesi število:"))
x = 1
deljitelji = []
while x <= stevilo / 2:
    if stevilo % x == 0:
        deljitelji.append(x)
    x += 1

if len(deljitelji) <= 2:
    print("Praštevilo")
else:
    print("Ni praštevilo")
