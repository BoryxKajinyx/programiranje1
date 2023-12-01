# Enačaj ne spremeni spremenljivke. Enačaj priredi, kam kaže ime.
# Python nikoli ne kopira stvari, če tega ne zahtevaš. Dve imeni namesto tega kažeta na isti objekt
# Operator za enakost preveri, če dve imeni kažeta na objekt z enako vsebino.
# Operator za istost preveri, če dve imeni kažeta na isti objekt.
s = [1, 2, 3]
t = [1, 2, 3]
u = s
print(s == t == u)
print(s is u)

# Funkcija kot argument dobi objekte. Funkcija ne sme spreminjati vrednosti svojih argumentov, razen če je to zahtevano.
