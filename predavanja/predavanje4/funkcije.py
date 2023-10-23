import math


def najdi_deljitelje(stevilo):
    deljitelji = []
    for i in range(1, stevilo + 1):
        if stevilo % i == 0:
            deljitelji.append(i)
    return deljitelji


for x in range(0, 1000):
    if x == sum(najdi_deljitelje(x)[:-1]):
        print(x)


def hipotenuza(k1, k2):
    return math.sqrt(k1 ** 2 + k2 ** 2)


def prastevilo(stevilo):
    for i in range(2, stevilo // 2):
        if stevilo % i == 0:
            return False
    else:
        return True


print(prastevilo(37))
# funkcije morajo vrnit vrednost in ne izpisat(brezveze)
