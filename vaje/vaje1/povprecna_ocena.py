ocena_a = int(input("Ocena [Ana]:"))
ocena_b = int(input("Ocena [Benjamin]:"))
ocena_c = int(input("Ocena [Cene]:"))
povprecna_ocena = (ocena_c + ocena_b + ocena_a) / 3
srednja_ocena = min(max(ocena_c, ocena_b), max(ocena_a, ocena_b))
print("Povprečna ocena:", povprecna_ocena)
print("Srednja ocena", srednja_ocena)
