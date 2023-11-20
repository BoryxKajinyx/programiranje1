import collections
import random
import unittest


# Inventar
def zaloga(inv, art):
    return inv[art]


def prodaj(inv, art, kol):
    inv[art] -= kol


def primanjkljaj(inv, nar):
    manjkajoce = {}
    for art, kol in nar.items():
        if kol > inv.get(art, 0):
            manjkajoce[art] = kol - inv.get(art, 0)
    return manjkajoce


# Najpogostejše
def freq(s):
    pogostost = {}
    for element in s:
        if element not in pogostost:
            pogostost[element] = 0
        pogostost[element] += 1
    return pogostost


def freq_max(s):
    max_val = None
    max_key = None
    for key, val in s.items():
        if max_val is None or val > max_val:
            max_val = val
            max_key = key
    return max_key


def najpogostejse(s):
    return freq_max(freq(s.split())), freq_max(freq(s))


def najpogostejse_urejene(s):
    pog_sl_bes = freq(s.split())
    pog_sl_crk = freq(s)
    ur_sez_bes = []
    ur_sez_crk = []
    temp_bes = [[] for _ in range(max(list(pog_sl_bes.values())))]
    temp_crk = [[] for _ in range(max(list(pog_sl_crk.values())))]
    for key, val in pog_sl_bes.items():
        temp_bes[val - 1].append(key)
    for key, val in pog_sl_crk.items():
        temp_crk[val - 1].append(key)
    for sezn in reversed(temp_bes):
        ur_sez_bes.extend(sorted(sezn))
    for sezn in reversed(temp_crk):
        ur_sez_crk.extend(sorted(sezn))
    return ur_sez_bes, ur_sez_crk


# Naključno generirano besedilo
def nasledniki(txt):
    seznam_besed = txt.split()
    slovar_nasl = {}
    for tren, nasl in zip(seznam_besed, seznam_besed[1:]):
        if tren not in slovar_nasl:
            slovar_nasl[tren] = []
        slovar_nasl[tren].append(nasl)
    return slovar_nasl


def tekst(nasl, num_besed):
    besedilo = random.choice(list(nasl))
    while num_besed > 1:
        besedilo += " " + random.choice(nasl[besedilo.split()[-1]])
        num_besed -= 1
    return besedilo


# Družinsko drevo
def family_tree(fam):
    tree = {}
    for sta, otr in fam:
        if sta not in tree:
            tree[sta] = []
        tree[sta].append(otr)
    return tree


def children(tree, name):
    return tree.get(name, [])


def grandchildren(tree, name):
    vnuki = []
    for otr in children(tree, name):
        vnuki.extend(children(tree, otr))
    return vnuki


def successors(tree, name):
    nasl = []
    neobdelani = list(children(tree, name))
    nasl.extend(neobdelani)
    while neobdelani:
        otroki = children(tree, neobdelani.pop())
        neobdelani.extend(otroki)
        nasl.extend(otroki)
    return nasl


# Šifra
def sifriraj(niz, kljuc):
    return ''.join(chr(ord(c) ^ (kljuc // 256**(i % 2) % 256)) for i, c in enumerate(niz))


def sifra(niz):
    file = open("Usr.dict.words")
    temp = [w for w in file]
    file.close()
    besede = []
    while temp:
        besede.append(temp.pop().split("\n")[0])

    for kljuc in range(65537):
        besedilo = sifriraj(niz, kljuc)
        for beseda in besedilo.split():
            if beseda not in besede:
                break
        else:
            return besedilo
    return "Ni ključa"


# ^^^ Naloge rešujte nad tem komentarjem. ^^^ ###


class TestSlovarji(unittest.TestCase):
    def setUp(self):
        self.tree = {
            'alice': ['mary', 'tom', 'judy'],
            'bob': ['mary', 'tom', 'judy'],
            'ken': ['suzan'],
            'renee': ['rob', 'bob'],
            'rob': ['jim'],
            'sid': ['rob', 'bob'],
            'tom': ['ken']}

    def assertDictCounterEqual(self, first, second, msg=None):
        def dict_counter(d):
            d_copy = dict(d)
            for k, v in d_copy.items():
                d_copy[k] = collections.Counter(v)
            return d_copy

        self.assertDictEqual(dict_counter(first), dict_counter(second), msg)

    def test_zaloga(self):
        inv = {"kruh": 5, "kajzerica": 4, "makovka": 3}
        self.assertEqual(zaloga(inv, "kruh"), 5)
        self.assertEqual(zaloga(inv, "kajzerica"), 4)
        self.assertEqual(zaloga(inv, "makovka"), 3)

    def test_prodaj(self):
        inv = {"kruh": 5, "kajzerica": 4, "makovka": 3}
        self.assertIsNone(prodaj(inv, "kajzerica", 2), "Funkcija naj ne vrača ničesar!")
        self.assertEqual(zaloga(inv, "kruh"), 5)
        self.assertEqual(zaloga(inv, "kajzerica"), 2)
        self.assertEqual(zaloga(inv, "makovka"), 3)

        prodaj(inv, "kruh", 5)
        self.assertTrue("kruh" not in inv or (zaloga(inv, "kruh"), 0))
        self.assertEqual(zaloga(inv, "kajzerica"), 2)
        self.assertEqual(zaloga(inv, "makovka"), 3)

    def test_primanjkljaj(self):
        inventar = {
            'sir': 8, 'kruh': 15, 'makovka': 10, 'pasja radost': 2,
            'pašteta': 10, 'mortadela': 4, 'klobasa': 7
        }
        self.assertDictEqual(
            primanjkljaj(inventar, {"kruh": 2, "makovka": 10}),
            {})
        self.assertDictEqual(
            primanjkljaj(inventar, {"kruh": 2, "makovka": 12}),
            {"makovka": 2})
        self.assertDictEqual(
            primanjkljaj(inventar, {"kruh": 2, "makovka": 12, "pivo": 3}),
            {"makovka": 2, "pivo": 3})
        self.assertDictEqual(primanjkljaj(inventar, {}), {})
        self.assertDictEqual(primanjkljaj(inventar, inventar), {})

    def test_family_tree(self):
        family = [
            ('bob', 'mary'),
            ('bob', 'tom'),
            ('bob', 'judy'),
            ('alice', 'mary'),
            ('alice', 'tom'),
            ('alice', 'judy'),
            ('renee', 'rob'),
            ('renee', 'bob'),
            ('sid', 'rob'),
            ('sid', 'bob'),
            ('tom', 'ken'),
            ('ken', 'suzan'),
            ('rob', 'jim')]
        self.assertDictCounterEqual(family_tree(family), self.tree)

    def test_children(self):
        self.assertCountEqual(children(self.tree, 'alice'), ['mary', 'tom', 'judy'])
        self.assertCountEqual(children(self.tree, 'mary'), [])
        self.assertCountEqual(children(self.tree, 'renee'), ['bob', 'rob'])
        self.assertCountEqual(children(self.tree, 'rob'), ['jim'])
        self.assertCountEqual(children(self.tree, 'suzan'), [])

    def test_grandchildren(self):
        self.assertCountEqual(grandchildren(self.tree, 'alice'), ['ken'])
        self.assertCountEqual(grandchildren(self.tree, 'bob'), ['ken'])
        self.assertCountEqual(grandchildren(self.tree, 'ken'), [])
        self.assertCountEqual(grandchildren(self.tree, 'mary'), [])
        self.assertCountEqual(grandchildren(self.tree, 'renee'), ['jim', 'mary', 'tom', 'judy'])
        self.assertCountEqual(grandchildren(self.tree, 'sid'), ['jim', 'mary', 'tom', 'judy'])
        self.assertCountEqual(grandchildren(self.tree, 'tom'), ['suzan'])

    def test_successors(self):
        self.assertCountEqual(successors(self.tree, 'tom'), ['ken', 'suzan'])
        self.assertCountEqual(successors(self.tree, 'sid'),
                              ['rob', 'bob', 'jim', 'mary', 'tom', 'judy', 'ken', 'suzan'])
        self.assertCountEqual(successors(self.tree, 'suzan'), [])
        self.assertCountEqual(successors(self.tree, 'ken'), ['suzan'])
        self.assertCountEqual(successors(self.tree, 'rob'), ['jim'])

    def test_najpogostejse(self):
        self.assertEqual(najpogostejse('a'), ('a', 'a'))
        self.assertEqual(najpogostejse('aa bb aa'), ('aa', 'a'))
        self.assertEqual(najpogostejse('in to in ono in to smo mi'), ('in', ' '))
        self.assertEqual(najpogostejse('abc abc abc abacbca'), ('abc', 'a'))
        self.assertEqual(najpogostejse('abc abc abc abacbcb'), ('abc', 'b'))
        self.assertEqual(najpogostejse('abc abc abc abacbcc'), ('abc', 'c'))

    def test_najpogostejse_urejene(self):
        self.assertEqual(najpogostejse_urejene('a'), (['a'], ['a']))
        self.assertEqual(najpogostejse_urejene('aa bb aa'), (['aa', 'bb'], ['a', ' ', 'b']))
        self.assertEqual(najpogostejse_urejene('in to in ono in to smo mi'),
                         (['in', 'to', 'mi', 'ono', 'smo'], [' ', 'o', 'i', 'n', 'm', 't', 's']))
        self.assertEqual(najpogostejse_urejene('abc abc abc abacbca'),
                         (['abc', 'abacbca'], ['a', 'b', 'c', ' ']))
        self.assertEqual(najpogostejse_urejene('abc abc abc abacbcb'),
                         (['abc', 'abacbcb'], ['b', 'a', 'c', ' ']))
        self.assertEqual(najpogostejse_urejene('abc abc abc abacbcc'),
                         (['abc', 'abacbcc'], ['c', 'a', 'b', ' ']))

    def test_sifra(self):
        self.assertEqual(sifra('\x19\x14\x1c]\x19\x0f\x14\t\x13\x18\t]\x12\x0e[\n\x1a\t\x18\x15\x12\x13\x1c'),
                         'big brother is watching')
        self.assertEqual(sifra('\xe1d\xe0q\xe5r\xf7b\xe0i'), 'strawberry')

    def test_nasledniki(self):
        self.assertDictCounterEqual(nasledniki('in in in in'), {'in': ['in', 'in', 'in']})
        self.assertDictCounterEqual(nasledniki('in to in ono in to smo mi'),
                                    {'smo': ['mi'], 'to': ['in', 'smo'], 'ono': ['in'], 'in': ['to', 'ono', 'to']})
        self.assertDictCounterEqual(nasledniki('danes je lep dan danes sije sonce'),
                                    {'lep': ['dan'], 'je': ['lep'], 'dan': ['danes'], 'danes': ['je', 'sije'],
                                     'sije': ['sonce']})

    def test_tekst(self):
        self.assertEqual(tekst({'in': ['in', 'in']}, 3), 'in in in')


if __name__ == '__main__':
    unittest.main(verbosity=2)
