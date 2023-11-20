import math


def izracun(fi, v):
    g = 9.807
    fi = math.radians(fi)
    razdalja = (v ** 2 * math.sin(2 * fi)) / g
    return razdalja


print("Program za izračun dolžine strela s topom")
kot = float(input("Vnesite kot strela:"))
hitrost = float(input("Vnesite hitrost izstrelka:"))
print("Izstrelek leti ", izracun(kot, hitrost), " metrov.")

