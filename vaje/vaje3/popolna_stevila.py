stevilo = 6
deljitelji = []
x = 1
while x < stevilo:
    if stevilo % x == 0:
        deljitelji.append(x)
    x += 1

if stevilo == sum(deljitelji):
    print("Popolno število")
else:
    print("Število ni popolno")
