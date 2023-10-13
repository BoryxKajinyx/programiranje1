import math
def izracun(kot,hitrost):
    g=9.807
    kot=math.radians(kot)
    razdalja=(hitrost**2*math.sin(2*kot))/g
    return razdalja

print("Program za izračun dolžine strela s topom")
kot=float(input("Vnesite kot strela:"))
hitrost=float(input("Vnesite hitrost izstrelka:"))
print("Izstrelek leti ",izracun(kot,hitrost)," metrov.")

