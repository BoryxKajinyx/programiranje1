# pari ključev in vrednosti, med ključem in vrednostjo je dvopičje

stevilke = {'Ana': '041 310239',
            'Berta': '040 318319',
            'Cilka': '041 103194',
            'Dani': '040 193831',
            'Ema': '051 123123',
            'Fanči': '040 135367',
            'Helga': '+49 175 4728 475',
            'Iva': '040 222333'}

# prazen slovar
prazen = {}

# možno je indeksiranje:
print(stevilke["Ema"])

# vrstni red elementov v slovarju je isti, kot vrstni red, v katerem so vili dodani

# slovar navadno vrne samo ključe.
print("Ema" in stevilke)

for x in stevilke:
    print(x)
# izpiše vse ključe

# vrednosti dobiš tako:
for x in stevilke.values():
    print(x)
# izpiše vse vrednosti

for k, v in stevilke.items():
    print(k, ":", v)
# izpiše oboje

# Če želiš privzeto vrednost, če ključa ni, uporabi get()
print(stevilke.get("Fanči"))  # , če Fanči ni v slovarju, vrne None
print(stevilke.get("Fanči", 0))  # , če Fanči ni v slovarju, vrne 0 oziroma karkoli daš tja
# Ne uporabljaj get(), če mora bit ključ v slovarju.
