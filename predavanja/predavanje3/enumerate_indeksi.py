# enumerate(seznam) doda številke elementom v seznamu

seznam = ["ena", "dva", "tri", "štiri", "pet", "šest"]
for mesto, besedilo in enumerate(seznam):
    ...

# indeksiranje vrne element na določenem mestu

print(seznam[3])  # izpiše element na mestu 3 (4. mesto - šteje od 0)

# ne more vrnit elementa izven seznama

# indeksiranje ponazaj

print(seznam[-1])  # začne od -1 ker -0 ni različen od 0

# indeksiranje več elementov hkrati
print(seznam[1:])  # vsi elementi od 2. dalje

print(seznam[:2])  # vsi elementi do 3.

print(seznam[1:5])  # vsi elementi med 2. in 6. brez 6.

print(seznam[2:-3])  # vsi elementi med 3. in -3., brez -3.

print(seznam[::2])  # vsak drugi element

print(seznam[::-1])  # obrnjen seznam
