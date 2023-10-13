from math import *

stranica1=float(input("Stranica a?"))
stranica2=float(input("Stranica b?"))
stranica3=float(input("Stranica c?"))
obseg = stranica3 + stranica2 + stranica1
povrsina_trikotnik = sqrt(obseg / 2 * (obseg / 2 - stranica1) * (obseg / 2 - stranica2) * (obseg / 2 - stranica3))
polmer_vcrtan = (povrsina_trikotnik * 2) / obseg
povrsina_vcrtan = polmer_vcrtan ** 2 * pi
polmer_ocrtan = (stranica3 * stranica2 * stranica1) / (4 * povrsina_trikotnik)
povrsina_ocrtan = polmer_ocrtan ** 2 * pi
print("Površina trikotnika:", povrsina_trikotnik)
print("Površina včrtanega kroga:", povrsina_vcrtan)
print("Površina očrtanega kroga:", povrsina_ocrtan)
