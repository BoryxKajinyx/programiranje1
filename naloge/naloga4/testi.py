import unittest


def dolzina_ovir(vrstica):
    return vrstica.count("#")


def stevilo_ovir(vrstica):
    return len(pretvori_vrstico(vrstica))


def najsirsa_ovira(vrstica):
    sirina = 0
    sirina_max = 0
    for x in vrstica:
        if x == "#":
            sirina += 1
            if sirina > sirina_max:
                sirina_max = sirina
        if x == ".":
            sirina = 0
    return sirina_max


def pretvori_vrstico(vrstica):
    pretvorba = []
    prvi = 0
    vrstica = "." + vrstica + "."
    for prej, po, num in zip(vrstica, vrstica[1:], range(len(vrstica)+1)):
        if prej + po == ".#":
            prvi = num + 1
        if prej + po == "#.":
            pretvorba.append((prvi, num))
    return pretvorba


def pretvori_zemljevid(zemljevid):
    pretvorba = []
    for num, vrstica in enumerate(zemljevid, start=1):
        for ovira, y in zip(pretvori_vrstico(vrstica), [num] * len(zemljevid)):
            pretvorba.append(ovira + (y,))
    return pretvorba


def izboljsave(prej, potem):
    dodane_ovire = []
    for ovira in pretvori_zemljevid(potem):
        if ovira not in pretvori_zemljevid(prej):
            dodane_ovire.append(ovira)
    return dodane_ovire


def huligani(prej, potem):
    dodane = []
    odstranjene = []
    for ovira in pretvori_zemljevid(prej):
        if ovira not in pretvori_zemljevid(potem):
            odstranjene.append(ovira)
    for ovira in pretvori_zemljevid(potem):
        if ovira not in pretvori_zemljevid(prej):
            dodane.append(ovira)
    return dodane, odstranjene


class Test(unittest.TestCase):
    def test_dolzina_ovir(self):
        self.assertEqual(3, dolzina_ovir("...###..."))
        self.assertEqual(1, dolzina_ovir("...#..."))
        self.assertEqual(2, dolzina_ovir("...#..#."))
        self.assertEqual(7, dolzina_ovir("#...#####..#."))
        self.assertEqual(8, dolzina_ovir("...#####.##...#"))
        self.assertEqual(9, dolzina_ovir("#...#####.##...#"))
        self.assertEqual(6, dolzina_ovir("##...#.#...##"))
        self.assertEqual(0, dolzina_ovir("..."))
        self.assertEqual(0, dolzina_ovir("."))

    def test_stevilo_ovir(self):
        self.assertEqual(1, stevilo_ovir("...###..."))
        self.assertEqual(1, stevilo_ovir("...#..."))
        self.assertEqual(2, stevilo_ovir("...#..#."))
        self.assertEqual(3, stevilo_ovir("#...#####..#."))
        self.assertEqual(3, stevilo_ovir("...#####.##...#"))
        self.assertEqual(4, stevilo_ovir("#...#####.##...#"))
        self.assertEqual(4, stevilo_ovir("##...#.#...##"))
        self.assertEqual(0, stevilo_ovir("..."))
        self.assertEqual(0, stevilo_ovir("."))

    def test_najsirsa_ovira(self):
        self.assertEqual(3, najsirsa_ovira("...###..."))
        self.assertEqual(1, najsirsa_ovira("...#..."))
        self.assertEqual(1, najsirsa_ovira("...#..#."))
        self.assertEqual(5, najsirsa_ovira("#...#####..#."))
        self.assertEqual(5, najsirsa_ovira("...#####.##...#"))
        self.assertEqual(5, najsirsa_ovira("#...#####.##...#"))
        self.assertEqual(6, najsirsa_ovira("######...#####.##...#"))
        self.assertEqual(6, najsirsa_ovira("...#####.##...######"))

    def test_pretvori_vrstico(self):
        self.assertEqual([(3, 5)], pretvori_vrstico("..###."))
        self.assertEqual([(3, 5), (7, 7)], pretvori_vrstico("..###.#."))
        self.assertEqual([(1, 2), (5, 7), (9, 9)], pretvori_vrstico("##..###.#."))
        self.assertEqual([(1, 1), (4, 6), (8, 8)], pretvori_vrstico("#..###.#."))
        self.assertEqual([(1, 1), (4, 6), (8, 8)], pretvori_vrstico("#..###.#"))
        self.assertEqual([], pretvori_vrstico("..."))
        self.assertEqual([], pretvori_vrstico(".."))
        self.assertEqual([], pretvori_vrstico("."))

    def test_pretvori_zemljevid(self):
        zemljevid = [
            "......",
            "..##..",
            ".##.#.",
            "...###",
            "###.##",
        ]
        self.assertEqual([(3, 4, 2), (2, 3, 3), (5, 5, 3), (4, 6, 4), (1, 3, 5), (5, 6, 5)],
                         pretvori_zemljevid(zemljevid))

        zemljevid = [
            "..............##...",
            "..###.....###....##",
            "...###...###...#...",
            "...........#.....##",
            "...................",
            "###.....#####...###"
        ]
        self.assertEqual([(15, 16, 1),
                          (3, 5, 2), (11, 13, 2), (18, 19, 2),
                          (4, 6, 3), (10, 12, 3), (16, 16, 3),
                          (12, 12, 4), (18, 19, 4),
                          (1, 3, 6), (9, 13, 6), (17, 19, 6)], pretvori_zemljevid(zemljevid))

    def test_izboljsave(self):
        prej = [
            "..............##...",
            "..###.....###....##",
            "...###...###...#...",
            "...........#.....##",
            "...................",
            "###.....#####...###"
        ]

        potem = [
            "...##.........##...",
            "..###.....###....##",
            "#..###...###...#...",
            "...###.....#.....##",
            "................###",
            "###.....#####...###"
        ]

        self.assertEqual([(4, 5, 1), (1, 1, 3), (4, 6, 4), (17, 19, 5)], izboljsave(prej, potem))

        self.assertEqual([], izboljsave(prej, prej))

    def test_huligani(self):
        prej = [
            "..............##...",
            "..###.....###....##",
            "...###...###...#...",
            "...........#.....##",
            "...................",
            "###.....#####...###"
        ]

        potem = [
            "...##..............",
            "..........###....##",
            "#..###...###...#...",
            "...###.....#.....##",
            "................###",
            "###.....##.##...###"
        ]

        dodane, odstranjene = huligani(prej, potem)
        self.assertEqual([(4, 5, 1), (1, 1, 3), (4, 6, 4), (17, 19, 5), (9, 10, 6), (12, 13, 6)], dodane,
                         "Napaka v seznamu dodanih")
        self.assertEqual([(15, 16, 1), (3, 5, 2), (9, 13, 6)], odstranjene,
                         "Napaka v seznamu odstranjenih")

        dodane, odstranjene = huligani(potem, prej)  # Pazi, obrnjeno!
        self.assertEqual([(15, 16, 1), (3, 5, 2), (9, 13, 6)], dodane,
                         "Napaka v seznamu dodanih")
        self.assertEqual([(4, 5, 1), (1, 1, 3), (4, 6, 4), (17, 19, 5), (9, 10, 6), (12, 13, 6)], odstranjene,
                         "Napaka v seznamu odstranjenih")

        self.assertEqual(([], []), huligani(prej, prej))


if __name__ == "__main__":
    unittest.main()
