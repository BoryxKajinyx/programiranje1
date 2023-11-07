ime = "Benjamin"
ime2 = "     Benjamin     "
ime3 = """Benjamin
Benjamin
Benjamin
Janez
"""

# count prešteje, kolikokrat se podniz pojavlja v določenem nizu
print(ime.count("e"))

# find vrne mesto prve ponovitve podniza v nizu
# če podniz ne obstaja, vrne -1
print(ime.find("ja"))

# index navede mesto prve ponovitve podniza v nizu
# če podniz ne obstaja, vrže napako
print(ime.find("mi"))

# prvi in drugi   preveri, če je prvi niz vsebovan v drugem - če je, vrne True, drugače vrne False
print("B" in ime)

# replace zamenja podniz v nizu z drugim podnizom
print(ime.replace("min", "max"))

# strip odstrani presledke na začetku in koncu niza
print(ime2.strip())

# split razdeli niz v podnize, ločene z podanim nizem, če niz ni podan, razdeli po presledkih, a ne vrne praznih nizov
print(ime2.split())
print(ime2.split("n"))

# splitlines razdeli niz, ki vsebuje več vrstic, po vrsticah
print(ime3.splitlines())

# join združi nize v podanem seznamu, loči jih z nizom, čigar metoda je
print(", ".join([ime, ime2, ime3.splitlines()]))

