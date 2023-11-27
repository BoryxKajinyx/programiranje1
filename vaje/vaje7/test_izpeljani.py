import unittest
import itertools
import math

morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
         'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
         'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
         '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
         '9': '----.', '0': '-----', " ": ''}


# Vsota kvadratov
def vsota_kvadratov(n):
    return sum([x ** 2 for x in range(n + 1)])


def vsota_kvadratov_pal(n):
    return sum([x ** 2 for x in range(n + 1) if list(str(x)) == list(reversed(str(x)))])


# Zamenjava črk
def subs(niz, polozaj):
    return "".join([niz[int(x)] for x in polozaj])


# Povprečje in standardni odklon
def mean(xs):
    return sum(xs) / len(xs)


def std(xs):
    return math.sqrt(sum([(xi - mean(xs)) ** 2 for xi in xs]) / len(xs))


# Morsejeva abeceda
def txt2morse(s):
    return " ".join([morse[znak] for znak in s])


def morse2txt(s):
    return "".join([list(morse.keys())[list(morse.values()).index(znak)] for znak in s.split(" ")])


# Obrni
def obrni(t):
    return [[x[i] for x in t] for i in range(len(t[0]))]


# ISBN
def valid(s):
    return sum([int(x) * (10-i) for i, x in enumerate(s[:-1])] + [10 if x == "X" else int(x) for x in s[-1:]]) % 11 == 0


# EAN
def valid_ean(s):
    return sum([int(x) * utez for x, utez in zip(s, itertools.cycle([1, 3]))]) % 10 == 0


# ## ^^^ Naloge rešujte nad tem komentarjem. ^^^ ###


class TestVaje(unittest.TestCase):
    def test_vsota_kvadratov(self):
        self.assertEqual(vsota_kvadratov(1), 1)
        self.assertEqual(vsota_kvadratov(10), 385)
        self.assertEqual(vsota_kvadratov(100), 338350)

    def test_vsota_kvadratov_pal(self):
        self.assertEqual(vsota_kvadratov_pal(1), 1)
        self.assertEqual(vsota_kvadratov_pal(100), 34770)
        self.assertEqual(vsota_kvadratov_pal(1000), 33454620)

    def test_subs(self):
        self.assertEqual(subs("abc", "0002"), "aaac")
        self.assertEqual(subs("komar", "23401"), "marko")
        self.assertEqual(subs("xyz", "001122"), "xxyyzz")

    def test_mean_std(self):
        xs = [183, 168, 175, 176, 192, 180]
        self.assertAlmostEqual(mean(xs), 179.0)
        self.assertAlmostEqual(std(xs), 7.43863786814)
        xs = [1]
        self.assertAlmostEqual(mean(xs), 1.0)
        self.assertAlmostEqual(std(xs), 0.0)

    def test_morse(self):
        self.assertEqual(txt2morse('TE A'), '- .  .-')
        self.assertEqual(txt2morse('HELLO WORLD'), '.... . .-.. .-.. ---  .-- --- .-. .-.. -..')
        self.assertEqual(morse2txt('.... . .-.. .-.. ---  .-- --- .-. .-.. -..'), 'HELLO WORLD')

    def test_obrni(self):
        self.assertEqual(obrni([[1]]), [[1]])
        self.assertEqual(obrni([[1, 2, 3]]), [[1], [2], [3]])
        self.assertEqual(obrni([[1], [2], [3]]), [[1, 2, 3]])
        self.assertEqual(obrni([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]),
                         [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]])

    def test_isbn(self):
        self.assertEqual(valid('0306406152'), True)
        self.assertEqual(valid('0553382578'), True)
        self.assertEqual(valid('0553293370'), True)
        self.assertEqual(valid('912115628X'), True)
        self.assertEqual(valid('03064061522'), False)
        self.assertEqual(valid('1553382578'), False)
        self.assertEqual(valid('91211562811'), False)

    def test_ean(self):
        self.assertEqual(valid_ean('9789612410223'), True)
        self.assertEqual(valid_ean('9789616465823'), True)
        self.assertEqual(valid_ean('9789616465723'), False)
        self.assertEqual(valid_ean('9789616466823'), False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
