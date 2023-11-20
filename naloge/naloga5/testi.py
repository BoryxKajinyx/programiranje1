import unittest


def koordinate(s):
    stolpec = int(s.split("-")[0])
    return stolpec, stolpec + s.count("-") - 1


def vrstica(s):
    vrsta = int(s.strip().split()[0][1:-1])
    seznam_ovir = []
    for zapis in s.strip().split()[1:]:
        seznam_ovir.append(koordinate(zapis) + (vrsta,))
    return seznam_ovir


def preberi(s):
    seznam_ovir = []
    for vrsta in s.splitlines():
        seznam_ovir += vrstica(vrsta)
    return seznam_ovir


def intervali(xs):
    zapis = []
    for zacetek, konec in xs:
        zapis.append(str(zacetek) + "-" * (konec - zacetek + 1))
    return zapis


def zapisi_vrstico(y, xs):
    zapis = "(" + str(y) + ")" + " " + " ".join(intervali(xs))
    return zapis


def kljuc_vrstica(zapis):
    return zapis[-1]


def kljuc_stolpec(zapis):
    return zapis[0]


def zapisi(ovire):
    urejene_ovire = sorted(ovire, key=kljuc_vrstica)
    vrstice = []
    vrsta = []
    y_prej = None
    for x1, x2, y in urejene_ovire:
        if y_prej is None:
            y_prej = y
        if y == y_prej:
            vrsta.append((x1, x2))
        else:
            vrstice.append((y_prej, sorted(vrsta, key=kljuc_stolpec)))
            vrsta = [(x1, x2)]
            y_prej = y
    vrstice.append((y_prej, sorted(vrsta, key=kljuc_stolpec)))
    vrste = []
    for y, xs in vrstice:
        vrste.append(zapisi_vrstico(y, xs))
    return "\n".join(vrste)


class Obvezna(unittest.TestCase):
    def test_koordinate(self):
        self.assertEqual((3, 4), koordinate("3--"))
        self.assertEqual((5, 10), koordinate("5------"))
        self.assertEqual((123, 123), koordinate("123-"))
        self.assertEqual((123, 125), koordinate("123---"))

    def test_vrstica(self):
        self.assertEqual([(1, 3, 4), (5, 11, 4), (15, 15, 4)], vrstica("  (4) 1---  5------- 15-"))
        self.assertEqual([(989, 991, 1234)], vrstica("(1234) 989---"))

    def test_preberi(self):
        self.assertEqual([(5, 6, 4),
                          (90, 100, 13), (5, 8, 13), (19, 21, 13),
                          (9, 11, 5), (19, 20, 5), (30, 34, 5),
                          (9, 11, 4),
                          (22, 25, 13), (17, 19, 13)], preberi(
            """ (4) 5--
(13) 90-----------   5---- 19---
 (5) 9---           19--   30-----
(4)           9---
(13)         22---- 17---
"""))

    def test_intervali(self):
        self.assertEqual(["6-----", "12-", "20---", "98-----"], intervali([(6, 10), (12, 12), (20, 22), (98, 102)]))

    def test_zapisi_vrstico(self):
        self.assertEqual("(5) 6----- 12-",
                         zapisi_vrstico(5, [(6, 10), (12, 12)]).rstrip("\n"))
        self.assertEqual("(8) 6----- 12- 20--- 98-----",
                         zapisi_vrstico(8, [(6, 10), (12, 12), (20, 22), (98, 102)]).rstrip("\n"))
        self.assertEqual("(8) 6----- 12- 20--- 98-----",
                         zapisi_vrstico(8, [(6, 10), (12, 12), (20, 22), (98, 102)]).rstrip("\n"))


class Dodatna(unittest.TestCase):
    def test_zapisi(self):
        ovire = [(5, 6, 4),
                 (90, 100, 13), (5, 8, 13), (9, 11, 13),
                 (9, 11, 5), (19, 20, 5), (30, 34, 5),
                 (9, 11, 4),
                 (22, 25, 13), (17, 19, 13)]
        kopija_ovir = ovire.copy()
        self.assertEqual("""(4) 5-- 9---
(5) 9--- 19-- 30-----
(13) 5---- 9--- 17--- 22---- 90-----------""", zapisi(ovire).rstrip("\n"))
        self.assertEqual(ovire, kopija_ovir, "Pusti seznam `ovire` pri miru")


if __name__ == "__main__":
    unittest.main()
