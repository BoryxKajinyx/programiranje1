import unittest
import ast
import itertools


A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, R, S, T, U, V = "ABCDEFGHIJKLMNOPRSTUV"

zemljevid = {
    (A, B): {'trava', 'gravel'},
    (B, A): {'trava', 'gravel'},
    (A, V): {'lonci', 'pešci'},
    (V, A): {'lonci', 'pešci'},
    (B, C): {'lonci', 'bolt'},
    (C, B): {'lonci', 'bolt'},
    (B, V): set(),
    (V, B): set(),
    (C, R): {'lonci', 'pešci', 'stopnice'},
    (R, C): {'lonci', 'pešci', 'stopnice'},
    (D, F): {'pešci', 'stopnice'},
    (F, D): {'pešci', 'stopnice'},
    (D, R): {'pešci'},
    (R, D): {'pešci'},
    (E, I): {'lonci', 'trava'},
    (I, E): {'lonci', 'trava'},
    (F, G): {'črepinje', 'trava'},
    (G, F): {'črepinje', 'trava'},
    (G, H): {'pešci', 'črepinje'},
    (H, G): {'pešci', 'črepinje'},
    (G, I): {'avtocesta'},
    (I, G): {'avtocesta'},
    (H, J): {'bolt', 'robnik'},
    (J, H): {'bolt', 'robnik'},
    (I, M): {'avtocesta'},
    (M, I): {'avtocesta'},
    (I, P): {'gravel'},
    (P, I): {'gravel'},
    (I, R): {'stopnice', 'robnik'},
    (R, I): {'stopnice', 'robnik'},
    (J, K): set(),
    (K, J): set(),
    (J, L): {'bolt', 'gravel'},
    (L, J): {'bolt', 'gravel'},
    (K, M): {'bolt', 'stopnice'},
    (M, K): {'bolt', 'stopnice'},
    (L, M): {'pešci', 'robnik'},
    (M, L): {'pešci', 'robnik'},
    (M, N): {'rodeo'},
    (N, M): {'rodeo'},
    (N, P): {'gravel'},
    (P, N): {'gravel'},
    (O, P): {'gravel'},
    (P, O): {'gravel'},
    (P, S): set(),
    (S, P): set(),
    (R, U): {'pešci', 'trava'},
    (U, R): {'pešci', 'trava'},
    (R, V): {'lonci', 'pešci'},
    (V, R): {'lonci', 'pešci'},
    (S, T): {'robnik', 'trava'},
    (T, S): {'robnik', 'trava'},
    (T, U): {'trava', 'gravel'},
    (U, T): {'trava', 'gravel'},
    (U, V): {'lonci', 'robnik', 'trava'},
    (V, U): {'lonci', 'robnik', 'trava'}
}

mali_zemljevid = {
    (A, B): {"robnik", "bolt"},
    (B, A): {"robnik", "bolt"},
    (A, C): {"bolt", "rodeo", "pešci"},
    (C, D): set(),
    (D, C): set(),
    (V, B): {"avtocesta"}
}


def nove_povezave(pot, z):
    return {rel for rel in itertools.pairwise(pot) if rel not in z}


def obiskane_tocke(pot):
    return {tocka for tocka in pot}


def popravljena_pot(pot):
    return "".join([x for x, y in itertools.pairwise(pot + " ") if x != y])


def povezave_z_vescino(pot, z, vescina):
    return [rel for rel in itertools.pairwise(pot) if vescina in z[rel]]


def dolgocasna_pot(pot, z):
    return any([not bool(z[rel]) for rel in itertools.pairwise(pot)])


def dobra_pot(pot, z):
    return all([len(z[rel]) >= 2 for rel in itertools.pairwise(pot)])


def zahtevnost_poti(pot, z):
    return max([len(z[rel]) for rel in itertools.pairwise(pot)])


def izvedljiva(pot, z, zivljenj):
    return sum([rel not in z for rel in itertools.pairwise(pot)]) < zivljenj


def enosmerne(z):
    return {(x, y) for x, y in z if (y, x) not in z}


def dvosmerne(z):
    return {(x, y): z[(x, y)] for x, y in z if (y, x) in z}


def najzahtevnejsi_odsek(pot, z):
    return (lambda x: x[max(x)])({len(z[rel]): rel for rel in itertools.pairwise(pot)})


class Test01Obvezna(unittest.TestCase):
    def test_0_ena_vrstica(self):
        pricakovane = "nove_povezave obiskane_tocke popravljena_pot povezave_z_vescino dolgocasna_pot" \
                      " dobra_pot dolgocasne_povezave zahtevnost_poti izvedljiva najzahtevnejsi_odsek" \
                      " enosmerne dvosmerne".split()

        with open(__file__, "r", encoding="utf-8") as f:
            for elm in ast.parse(f.read()).body:
                if not isinstance(elm, ast.FunctionDef):
                    continue

                self.assertIn(elm.name, pricakovane,
                              f"\nTokrat ne dodajaj drugih funkcij: odstrani funkcijo '{elm.name}'.")
                body = elm.body
                self.assertEqual(len(body), 1, "\nFunkcija ni dolga le eno vrstico")
                self.assertIsInstance(body[0], ast.Return, "\nFunkcija naj bi vsebovala le return")

    def test_1_nove_povezave(self):
        self.assertEqual({(V, C), (C, D), (F, E)}, nove_povezave("ABVCDFE", zemljevid))
        self.assertEqual({(A, U)}, nove_povezave("AU", zemljevid))
        self.assertEqual(set(), nove_povezave("ABVRC", zemljevid))
        self.assertEqual(set(), nove_povezave("ABVRCBA", zemljevid))
        self.assertEqual({(C, D), (D, P), (P, M)}, nove_povezave("CDPM", zemljevid))

    def test_2_obiskane_tocke(self):
        self.assertEqual({A, B, C, R, U, V}, obiskane_tocke("ABVURURC"))
        self.assertEqual({P, N}, obiskane_tocke("PN"))

    def test_3_popravljena_pot(self):
        self.assertEqual("ABCRIE", popravljena_pot("ABBCCRRIIE"))
        self.assertEqual("MN", popravljena_pot("MN"))
        self.assertEqual("NMI", popravljena_pot("NMMI"))
        self.assertEqual("ABCRDFGIMNPSTUVA", popravljena_pot("ABBCCRRDDFFGGIIMMNNPPSSTTUUVVA"))

    def test_4_povezave_z_vescino(self):
        self.assertEqual([('R', 'U'), ('V', 'R'), ('R', 'U')], povezave_z_vescino("RUVRUTS", zemljevid, "pešci"))
        self.assertEqual([], povezave_z_vescino("RUVRUTS", zemljevid, "avtocesta"))
        self.assertEqual([(V, R), (R, C), (C, R), (R, D), (D, F)], povezave_z_vescino("VRCRDF", zemljevid, "pešci"))
        self.assertEqual([(G, I)], povezave_z_vescino("FGIE", zemljevid, "avtocesta"))

    def test_5_dolgocasna_pot(self):
        self.assertTrue(dolgocasna_pot("ABVUR", zemljevid))
        self.assertFalse(dolgocasna_pot("AVUR", zemljevid))
        self.assertTrue(dolgocasna_pot("GIPS", zemljevid))
        self.assertFalse(dolgocasna_pot("GIP", zemljevid))
        self.assertFalse(dolgocasna_pot("GI", zemljevid))
        self.assertTrue(dolgocasna_pot("PS", zemljevid))
        self.assertTrue(dolgocasna_pot("SP", zemljevid))

    def test_6_dobra_pot(self):
        self.assertTrue(dobra_pot("ABCR", zemljevid))
        self.assertFalse(dobra_pot("ABCRDF", zemljevid))
        self.assertFalse(dobra_pot("BV", zemljevid))
        self.assertFalse(dobra_pot("ABV", zemljevid))
        self.assertFalse(dobra_pot("BVU", zemljevid))

    def test_7_zahtevnost_poti(self):
        self.assertEqual(3, zahtevnost_poti("ABCRU", zemljevid))
        self.assertEqual(1, zahtevnost_poti("IPS", zemljevid))
        self.assertEqual(0, zahtevnost_poti("PS", zemljevid))
        self.assertEqual(3, zahtevnost_poti("ABVUT", zemljevid))
        self.assertEqual(2, zahtevnost_poti("ABVR", zemljevid))

    def test_8_izvedljiva(self):
        self.assertTrue(izvedljiva("AVUSPRDEI", zemljevid, 4))
        self.assertFalse(izvedljiva("AVUSPRDEI", zemljevid, 3))
        self.assertFalse(izvedljiva("AVUSPRE", zemljevid, 3))
        self.assertFalse(izvedljiva("AVUSPRE", zemljevid, 2))
        self.assertTrue(izvedljiva("AB", zemljevid, 2))
        self.assertTrue(izvedljiva("AB", zemljevid, 1))
        self.assertFalse(izvedljiva("AB", zemljevid, 0))

    def test_9_enosmerne(self):
        self.assertEqual({(A, C), (V, B)}, enosmerne(mali_zemljevid))
        self.assertEqual(set(), enosmerne(zemljevid))

    def test_10_dvosmerne(self):
        self.assertEqual(zemljevid, dvosmerne(zemljevid))
        self.assertEqual({(A, B): {"robnik", "bolt"}, (B, A): {"robnik", "bolt"},
                          (C, D): set(), (D, C): set()}, dvosmerne(mali_zemljevid))


class Test02Dodatna(unittest.TestCase):
    def test_najzahtevnejsi_odsek(self):
        self.assertEqual((C, R), najzahtevnejsi_odsek("ABCRU", zemljevid))
        self.assertEqual((C, R), najzahtevnejsi_odsek("CR", zemljevid))
        self.assertEqual((V, U), najzahtevnejsi_odsek("ABVUT", zemljevid))


if "__main__" == __name__:
    unittest.main()