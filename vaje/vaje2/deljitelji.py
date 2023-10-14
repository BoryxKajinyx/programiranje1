stevilo = int(input("Vnesi število:"))
x = 1
while x < stevilo:
    if stevilo % x == 0:
        print(x)
    x += 1
print(stevilo)
