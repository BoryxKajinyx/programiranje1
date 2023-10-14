from math import *

a = int(input("Vnesi a:"))
b = int(input("Vnesi b:"))
c = int(input("Vnesi c:"))

D = b ** 2 - 4 * a * c

if D < 0:
    print("Enačba nima realnih rešitev.")
elif D == 0:
    x = (-1 * b) / (2 * a)
    print("Enačba ima eno realno rešitev:", x)
else:
    x1 = (-1 * b + sqrt(D)) / (2 * a)
    x2 = (-1 * b - sqrt(D)) / (2 * a)
    print("Enačba ima dve realni rešitve:", x1, "in", x2)
