t = 0


# def lihosodi(sezn):
#     if not sezn:
#         return True
#     elif sezn[0] % 2 == 0:
#         return False
#     return sodolihi(sezn[1:])


def lihosodi(s):
    return not s or s[0] % 2 == 1 and sodolihi(s[:1])


def sodolihi(s):
    return not s or s[0] % 2 == 0 and lihosodi(s[:1])


# def sodolihi(sezn):
#     if not sezn:
#         return True
#     elif sezn[0] % 2 == 1:
#         return False
#     return lihosodi(sezn[1:])


def sodo(sezn):
    if not sezn:
        return True
    elif sezn[0] % 2 == 1:
        return False
    return sodo(sezn[1:])


def liho(sezn):
    if not sezn:
        return True
    elif sezn[0] % 2 == 0:
        return False
    return liho(sezn[1:])


sls = [1, 2, 3, 4]
ssl = [2, 3, 4, 5]
s_s = [2, 4, 6, 8]
s_l = [1, 3, 5, 7]

sodolihi(ssl)
lihosodi(sls)
sodo(s_s)
liho(s_l)


rodbina = {
    "Adam": ["Matjaž", "Cilka", "Daniel"],
    "Aleksander": [],
    "Alenka": [],
    "Barbara": [],
    "Cilka": [],
    "Daniel": ["Elizabeta", "Hans"],
    "Erik": [],
    "Elizabeta": ["Ludvik", "Jurij", "Barbara"],
    "Franc": [],
    "Herman": ["Margareta"],
    "Hans": ["Herman", "Erik"],
    "Jožef": ["Alenka", "Aleksander", "Petra"],
    "Jurij": ["Franc", "Jožef"],
    "Ludvik": [],
    "Margareta": [],
    "Matjaž": ["Viljem"],
    "Petra": [],
    "Tadeja": [],
    "Viljem": ["Tadeja"],
}


def obstaja(oseba, ime):
    if oseba == ime:
        return True
    for otrok in rodbina[oseba]:
        if obstaja(otrok, ime):
            return True
    return False


def velikost_rodbine(oseba):
    velikost = 0
    for otrok in rodbina[oseba]:
        velikost += velikost_rodbine(otrok)
    return velikost + 1


print(velikost_rodbine("Adam"))


def globina_rodbine(oseba):
    if not rodbina[oseba]:
        return 1
    naj_glob = 0
    for otrok in rodbina[oseba]:
        glob = globina_rodbine(otrok)
        naj_glob = max(glob, naj_glob)
    return naj_glob + 1

print(globina_rodbine("Adam"))