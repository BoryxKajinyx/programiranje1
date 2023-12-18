import unittest


def preberi_vrstice(ime_datoteke):
    with open(ime_datoteke, "r", encoding='utf-8') as datoteka:
        return [vrstica.strip() for vrstica in datoteka]


def preberi_csv(ime_datoteke):
    podatki = []
    for vrstica in preberi_vrstice(ime_datoteke):
        mesto, vreme, temp = vrstica.split(";")
        podatki.append((mesto, vreme, float(temp)))
    return podatki


def oblikuj(podatki):
    oblikovani = []
    for mesto, vreme, temp in podatki:
        oblikovani.append(f"Kraj: {mesto}, Vreme: {vreme}, Temperatura: {temp}°C")
    return oblikovani


def oblikuj_tabelo(podatki):
    tabela = [
        f"{'Kraj':<16}{'Vreme':<16}{'Temperatura (°C)':<16}",
        "-"*16*3
    ]
    for mesto, vreme, temp in podatki:
        tabela.append(f"{mesto:<16}{vreme:<16}{temp:>16.1f}")
    return tabela


def oblikuj_tabelo_f(podatki):
    podatki = [(mesto, vreme, temp * (9 / 5) + 32) for mesto, vreme, temp in podatki]
    tabela = [
        f"{'Kraj':<16}{'Vreme':<16}{'Temperatura (°F)':<16}",
    ] + oblikuj_tabelo(podatki)[1:]
    return tabela


def oblikuj_pike(podatki):
    podatki = [(mesto, vreme, temp * (9 / 5) + 32) for mesto, vreme, temp in podatki]
    tabela = [
        f"{'Kraj':<16}{'Vreme':<16}{'Temperatura (°F)':<16}",
        "-" * 16 * 3
    ]
    for mesto, vreme, temp in podatki:
        tabela.append(f"{mesto:.<16}{vreme:.<16}{temp:.>16.1f}")
    return tabela


def oblikuj_fc(podatki):
    podatki = [(mesto, vreme, temp * (9 / 5) + 32, temp) for mesto, vreme, temp in podatki]
    tabela = [
        f"{'Kraj':<16}{'Vreme':<13}{'Temperatura °F (°C)':<19}",
        "-" * (16 * 3)
    ]
    for mesto, vreme, tempf, tempc in podatki:
        temp = f"{tempf:.>3.1f} ({tempc:3.1f})"
        tabela.append(f"{mesto:.<16}{vreme:.<13}{temp:.>19}")
    return tabela


# najdaljše besede
def najdaljse_besede(s):
    dolzina = max(map(len, s.split()))
    niz = ""
    for beseda in s.split():
        if len(beseda) == dolzina:
            niz += beseda + ", "
    return niz[:-2]


def shrani(xs, ime_datoteke):
    with open(ime_datoteke, "w", encoding="utf-8") as datoteka:
        datoteka.writelines((x + "\n" for x in xs))
    return None


# ## ^^^ Naloge rešujte nad tem komentarjem. ^^^ ###


class Testi(unittest.TestCase):

    def setUp(self):
        f = open("podatki.txt", "w", encoding='utf-8')
        f.write("Ljubljana;oblačno;12.1\n")
        f.write("Maribor;sončno;9\n")
        f.write("Koper;sončno;14.7\n")
        f.close()

        self.podatki = [('Ljubljana', 'oblačno', 12.1), ('Maribor', 'sončno', 9.0), ('Koper', 'sončno', 14.7)]

    def test_preberi_vrstice(self):
        self.assertEqual(preberi_vrstice("podatki.txt"), ["Ljubljana;oblačno;12.1", "Maribor;sončno;9", "Koper;sončno;14.7"])

    def test_preberi_csv(self):
        self.assertEqual(preberi_csv("podatki.txt"), [('Ljubljana', 'oblačno', 12.1), ('Maribor', 'sončno', 9.0), ('Koper', 'sončno', 14.7)])

    def test_oblikuj(self):
        self.assertEqual(oblikuj(self.podatki),
                         ['Kraj: Ljubljana, Vreme: oblačno, Temperatura: 12.1°C',
                          'Kraj: Maribor, Vreme: sončno, Temperatura: 9.0°C',
                          'Kraj: Koper, Vreme: sončno, Temperatura: 14.7°C'])

    def test_oblikuj_tabelo(self):
        self.assertEqual(oblikuj_tabelo(self.podatki),
                         ['Kraj            Vreme           Temperatura (°C)',
                          '------------------------------------------------',
                          'Ljubljana       oblačno                     12.1',
                          'Maribor         sončno                       9.0',
                          'Koper           sončno                      14.7'])

    def test_oblikuj_tabelo_f(self):
        self.assertEqual(oblikuj_tabelo_f(self.podatki),
                         ['Kraj            Vreme           Temperatura (°F)',
                          '------------------------------------------------',
                          'Ljubljana       oblačno                     53.8',
                          'Maribor         sončno                      48.2',
                          'Koper           sončno                      58.5'])

    def test_oblikuj_pike(self):
        self.assertEqual(oblikuj_pike(self.podatki),
                         ['Kraj            Vreme           Temperatura (°F)',
                          '------------------------------------------------',
                          'Ljubljana.......oblačno.....................53.8',
                          'Maribor.........sončno......................48.2',
                          'Koper...........sončno......................58.5'])

    def test_oblikuj_fc(self):
        self.assertEqual(oblikuj_fc(self.podatki),
                         ['Kraj            Vreme        Temperatura °F (°C)',
                          '------------------------------------------------',
                          'Ljubljana.......oblačno..............53.8 (12.1)',
                          'Maribor.........sončno................48.2 (9.0)',
                          'Koper...........sončno...............58.5 (14.7)'])

    def test_shrani(self):
        lines = ['prva vrstica', 'druga vrstica', 'tretja vrstica']
        shrani(lines, 'datoteka.txt')
        f = open("datoteka.txt", "r")
        lines_f = f.read().splitlines()
        f.close()
        self.assertEqual(lines_f, lines)

    def test_najdaljse_besede(self):
        self.assertEqual(najdaljse_besede('ob znaku bo ura deset in pet minut'), 'znaku, deset, minut')

if __name__ == '__main__':
    unittest.main(verbosity=2)
