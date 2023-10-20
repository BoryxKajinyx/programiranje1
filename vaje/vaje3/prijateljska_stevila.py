def deljitelji(num):
    seznam = []
    x = 1
    while x < num:
        if num % x == 0:
            seznam.append(x)
        x += 1
    return seznam


stevilo = int(input("Vnesi število:"))
if stevilo == sum(deljitelji(sum(deljitelji(stevilo)))):
    print("Prijateljsko število:", sum(deljitelji(stevilo)))
else:
    print("Ni prijateljskih števil")
