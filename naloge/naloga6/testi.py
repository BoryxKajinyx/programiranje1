import unittest


A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, R, S, T, U, V = "ABCDEFGHIJKLMNOPRSTUV"

zemljevid = {
    (A, B): "gravel trava",
    (A, V): "pešci lonci",
    (B, C): "bolt lonci",
    (B, V): "",
    (C, R): "stopnice pešci lonci",
    (D, F): "stopnice pešci",
    (D, R): "pešci",
    (E, I): "trava lonci",
    (F, G): "trava črepinje",
    (G, H): "črepinje pešci",
    (G, I): "avtocesta",
    (H, J): "robnik bolt",
    (I, M): "avtocesta",
    (I, P): "gravel",
    (I, R): "stopnice robnik",
    (J, K): "",
    (J, L): "gravel bolt",
    (K, M): "stopnice bolt",
    (L, M): "robnik pešci",
    (M, N): "rodeo",
    (N, P): "gravel",
    (O, P): "gravel",
    (P, S): "",
    (R, U): "trava pešci",
    (R, V): "pešci lonci",
    (S, T): "robnik trava",
    (T, U): "gravel trava",
    (U, V): "robnik lonci trava"
}

mali_zemljevid = {(A, B): "robnik bolt",
                  (A, C): "bolt rodeo pešci",
                  (C, D): ""}


def dvosmerni_zemljevid(z):
    dvosmerni = {}
    for (zac, kon), ovire in z.items():
        dvosmerni[(zac, kon)] = set(ovire.split())
        dvosmerni[(kon, zac)] = set(ovire.split())
    return dvosmerni


def mozna_pot(pot, z):
    dvosmerni = dvosmerni_zemljevid(z)
    for tren, nasl in zip(pot, pot[1:]):
        if (tren, nasl) not in dvosmerni:
            return False
    return True


def potrebne_vescine(pot, z):
    dvosmerni = dvosmerni_zemljevid(z)
    vescine = set()
    for tren, nasl in zip(pot, pot[1:]):
        vescine |= dvosmerni[(tren, nasl)]
    return vescine


def nepotrebne_vescine(pot, z, vescine):
    return vescine - potrebne_vescine(pot, z)


def tocke_vescine(z, vescina):
    tocke = set()
    for rel, ovire in dvosmerni_zemljevid(z).items():
        if vescina in ovire:
            tocke |= set(rel)
    return "".join(sorted(tocke))


def koncna_tocka(pot, z, vescine):
    dvosmerni = dvosmerni_zemljevid(z)
    for rel in zip(pot, pot[1:]):
        ovire = dvosmerni[rel]
        if ovire - vescine:
            return rel[0], ovire - vescine
    return pot[-1], set()


class TestObvezna(unittest.TestCase):
    def test_1_dvosmerni_zemljevid(self):
        kopija = mali_zemljevid.copy()

        self.assertEqual({('A', 'B'): {'robnik', 'bolt'},
                          ('B', 'A'): {'robnik', 'bolt'},
                          ('A', 'C'): {'bolt', 'rodeo', 'pešci'},
                          ('C', 'A'): {'bolt', 'rodeo', 'pešci'},
                          ('C', 'D'): set(),
                          ('D', 'C'): set()},
                         dvosmerni_zemljevid(mali_zemljevid))
        self.assertEqual(mali_zemljevid, kopija, "Ne spreminjaj zemljevida, temveč sestavi novega!")

    def test_2_mozna_pot(self):
        self.assertTrue(mozna_pot("ACD", mali_zemljevid))
        self.assertTrue(mozna_pot("ABACD", mali_zemljevid))
        self.assertTrue(mozna_pot("AB", mali_zemljevid))
        self.assertFalse(mozna_pot("ABD", mali_zemljevid))

        self.assertTrue(mozna_pot("ABCRVRIEIPNM", zemljevid))
        self.assertTrue(mozna_pot("HJKMLJH", zemljevid))
        self.assertFalse(mozna_pot("AC", zemljevid))
        self.assertFalse(mozna_pot("ABCRVRIEPNM", zemljevid))
        self.assertTrue(mozna_pot("A", zemljevid))

    def test_3_potrebne_vescine(self):
        self.assertEqual({'pešci', 'bolt', 'rodeo'},
                         potrebne_vescine("AC", mali_zemljevid))

        self.assertEqual({'pešci', 'bolt', 'rodeo'},
                         potrebne_vescine("ACD", mali_zemljevid))

        self.assertEqual({'pešci', 'robnik', 'bolt', 'rodeo'},
                         potrebne_vescine("ABACD", mali_zemljevid))

        self.assertEqual({'robnik', 'stopnice', 'gravel', 'trava'},
                         potrebne_vescine("RIPSTUT", zemljevid))

        self.assertEqual({'pešci', 'trava', 'lonci', 'bolt', 'stopnice', 'gravel'},
                         potrebne_vescine("ABCRVR", zemljevid))

        self.assertEqual({'pešci', 'trava', 'robnik', 'lonci', 'bolt', 'stopnice', 'rodeo', 'gravel'},
                         potrebne_vescine("ABCRVRIEIPNM", zemljevid))

        self.assertEqual({'pešci', 'robnik', 'bolt', 'stopnice', 'gravel'},
                         potrebne_vescine("HJKMLJH", zemljevid))

        self.assertEqual(set(), potrebne_vescine("BVBVBVB", zemljevid))

    def test_4_nepotrebne_vescine(self):
        vescine = {'pešci', 'robnik', 'stopnice', 'gravel', 'bolt', 'rodeo'}
        kopija = vescine.copy()
        self.assertEqual({'stopnice', 'gravel'},
                         nepotrebne_vescine("ABACD", mali_zemljevid, vescine))
        self.assertEqual(vescine, kopija, "Se mi prav zdi, da je funkcija nepotrebne_vescine spremenila "
                                          "vrednost svojega argumenta `vescine`? Fail, fail!")

        vescine = {'stopnice', 'gravel', 'bolt', 'rodeo'}
        self.assertEqual({'stopnice', 'bolt'},
                         nepotrebne_vescine("IPNMNPO", zemljevid, vescine))

        vescine = {'gravel', 'rodeo'}
        self.assertEqual(set(), nepotrebne_vescine("IPNMNPO", zemljevid, vescine))

    def test_5_tocke_vescine(self):
        self.assertEqual("GIM", tocke_vescine(zemljevid, "avtocesta"))
        self.assertEqual("HIJLMRSTUV", tocke_vescine(zemljevid, "robnik"))
        self.assertEqual("MN", tocke_vescine(zemljevid, "rodeo"))
        self.assertEqual("ABIJLNOPTU", tocke_vescine(zemljevid, "gravel"))


class TestDodatna(unittest.TestCase):
    def test_1_koncna_tocka(self):
        vescine = {'pešci', 'robnik', 'bolt', 'stopnice', 'gravel'}
        self.assertEqual(("H", {'črepinje'}), koncna_tocka("HJKMLJHGFD", zemljevid, vescine))
        self.assertEqual(("M", {'rodeo'}), koncna_tocka("HJKMNPIG", zemljevid, vescine))
        self.assertEqual(("B", {'lonci', 'bolt'}), koncna_tocka("ABCRVB", zemljevid, {"gravel", "trava"}))


if "__main__" == __name__:
    unittest.main()
