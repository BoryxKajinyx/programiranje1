stevilo = int(input("Vnesi število:"))
x=0
#Collatz
while stevilo != 1:
    print(stevilo)
    if stevilo % 2 == 0:
        stevilo //= 2
    else:
        stevilo = stevilo * 3 + 1
    x += 1
print(stevilo)
print(x)
