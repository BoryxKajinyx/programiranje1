teze = [74, 83, 58, 66, 61, 84]
imena = ["Anže", "Benjamin", "Cilka", "Dani", "Eva", "Franc"]
studentka = [False, False, True, False, True, False]

stevila = (1, 2, 3, 4, 5)
cifre = (1, 2, 3, 4, 5)
terka = (6,)
# Terke se ne da spremenit
t = (1, "besedilo", False)
t = (2, "različno besedilo", True)
# Terka se ne spremeni, spremenljivka kaže na drugo terko

# razpakiranje

ena, dva, tri, stiri, pet = stevila
a, b, c, d, e, *_ = "abcdefghij"
_, _, _, i, *ostali = "fghijklmnop"
malo = 1
dosti = 10
ena, dva = dva, ena

# indeksiranje
Franc = imena[5]
F = Franc[0]
# tudi v rikverc
c = Franc[-1]
# rezine
ra = Franc[1:3]  # ne vključi zgornje meje
