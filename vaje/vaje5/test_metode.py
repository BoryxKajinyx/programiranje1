import unittest


def unikati(s):
    seznam_unikatov = []
    for element in s:
        if element not in seznam_unikatov:
            seznam_unikatov.append(element)
    return seznam_unikatov


def avtor(tvit):
    return tvit[:tvit.find(":")]


def vsi_avtorji(tviti):
    seznam_avtorjev = []
    for tvit in tviti:
        seznam_avtorjev.append(avtor(tvit))
    seznam_avtorjev = unikati(seznam_avtorjev)
    return seznam_avtorjev


def izloci_besedo(beseda):
    beseda1 = beseda
    for znak in beseda1:
        if not znak.isalnum():
            beseda1 = beseda1[1:]
        else:
            break
    for znak in reversed(beseda1):
        if not znak.isalnum():
            beseda1 = beseda1[:-1]
        else:
            break
    return beseda1


def se_zacne_z(tvit, c):
    seznam_besed = []
    for beseda in tvit.split():
        if beseda.startswith(c):
            seznam_besed.append(izloci_besedo(beseda))
    return seznam_besed


def zberi_se_zacne_z(tviti, c):
    seznam_besed = []
    for tvit in tviti:
        seznam_besed.extend(se_zacne_z(tvit, c))
    seznam_besed = unikati(seznam_besed)
    return seznam_besed


def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")


def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")


def vse_osebe(tviti):
    seznam_oseb = []
    seznam_oseb.extend(vse_afne(tviti))
    seznam_oseb.extend(vsi_avtorji(tviti))
    seznam_oseb = unikati(seznam_oseb)
    seznam_oseb.sort()
    return seznam_oseb


def custva(tviti, hashtagi):
    seznam_avtorjev = []
    for tvit in tviti:
        for tag in hashtagi:
            if tag in tvit:
                seznam_avtorjev.append(avtor(tvit))
    seznam_avtorjev = unikati(seznam_avtorjev)
    seznam_avtorjev.sort()
    return seznam_avtorjev


def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        if avtor(tvit) == oseba1 and oseba2 in se_zacne_z(tvit, "@"):
            return True
        elif avtor(tvit) == oseba2 and oseba1 in se_zacne_z(tvit, "@"):
            return True
    return False


class TestTviti(unittest.TestCase):
    tviti = [
        "sandra: Spet ta dež. #dougcajt",
        "berta: @sandra Delaj domačo za #programiranje1",
        "sandra: @berta Ne maram #programiranje1 #krneki",
        "ana: kdo so te @berta, @cilka, @dani? #krneki",
        "cilka: jst sm pa #luft",
        "benjamin: pogrešam ano #zalosten",
        "ema: @benjamin @ana #split? po dvopičju, za začetek?",
    ]

    def test_01_unikat(self):
        self.assertEqual(unikati([1, 2, 1, 1, 3, 2]), [1, 2, 3])
        self.assertEqual(unikati([1, 3, 2, 1, 1, 3, 2]), [1, 3, 2])
        self.assertEqual(unikati([1, 5, 4, 3, 2]), [1, 5, 4, 3, 2])
        self.assertEqual(unikati([1, 1, 1, 1, 1]), [1])
        self.assertEqual(unikati([1]), [1])
        self.assertEqual(unikati([]), [])
        self.assertEqual(unikati(["Ana", "Berta", "Cilka", "Berta"]), ["Ana", "Berta", "Cilka"])

    def test_02_avtor(self):
        self.assertEqual(avtor("janez: pred dvopičjem avtor, potem besedilo"), "janez")
        self.assertEqual(avtor("ana: malo krajse ime"), "ana")
        self.assertEqual(avtor("benjamin: pomembne so tri stvari: prva, druga in tretja"), "benjamin")

    def test_03_vsi_avtorji(self):
        self.assertEqual(vsi_avtorji(self.tviti), ["sandra", "berta", "ana", "cilka", "benjamin", "ema"])
        self.assertEqual(vsi_avtorji(self.tviti[:3]), ["sandra", "berta"])

    def test_04_izloci_besedo(self):
        self.assertEqual(izloci_besedo("@ana"), "ana")
        self.assertEqual(izloci_besedo("@@ana!!!"), "ana")
        self.assertEqual(izloci_besedo("ana"), "ana")
        self.assertEqual(izloci_besedo("!#$%\"=%/%()/Ben-jamin'"), "Ben-jamin")

    def test_05_vse_na_crko(self):
        self.assertEqual(se_zacne_z("Benjamin $je $skocil! Visoko!", "$"), ["je", "skocil"])
        self.assertEqual(se_zacne_z("Benjamin $je $skocil! #Visoko!", "$"), ["je", "skocil"])
        self.assertEqual(se_zacne_z("ana: kdo so te @berta, @cilka, @dani? #krneki", "@"), ["berta", "cilka", "dani"])

    def test_06_zberi_na_crko(self):
        self.assertEqual(zberi_se_zacne_z(self.tviti, "@"),
                         ['sandra', 'berta', 'cilka', 'dani', 'benjamin', 'ana'])
        self.assertEqual(zberi_se_zacne_z(self.tviti, "#"),
                         ['dougcajt', 'programiranje1', 'krneki', 'luft', 'zalosten', 'split'])

    def test_07_vse_afne(self):
        self.assertEqual(vse_afne(self.tviti), ['sandra', 'berta', 'cilka', 'dani', 'benjamin', 'ana'])

    def test_08_vsi_hashtagi(self):
        self.assertEqual(vsi_hashtagi(self.tviti),
                         ['dougcajt', 'programiranje1', 'krneki', 'luft', 'zalosten', 'split'])

    def test_09_vse_osebe(self):
        self.assertEqual(vse_osebe(self.tviti), ['ana', 'benjamin', 'berta', 'cilka', 'dani', 'ema', 'sandra'])

    def test_10_custva(self):
        self.assertEqual(custva(self.tviti, ["dougcajt", "krneki"]), ["ana", "sandra"])
        self.assertEqual(custva(self.tviti, ["luft"]), ["cilka"])
        self.assertEqual(custva(self.tviti, ["meh"]), [])

    def test_11_se_poznata(self):
        self.assertTrue(se_poznata(self.tviti, "ana", "berta"))
        self.assertTrue(se_poznata(self.tviti, "ema", "ana"))
        self.assertFalse(se_poznata(self.tviti, "sandra", "ana"))
        self.assertFalse(se_poznata(self.tviti, "cilka", "luft"))
        self.assertFalse(se_poznata(self.tviti, "cilka", "balon"))


if __name__ == "__main__":
    unittest.main()
