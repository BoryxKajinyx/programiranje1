class Oseba:
    def __init__(self, ime, spol):
        self.ime = ime
        self.spol = spol

    def pozdrav(self):
        print(f"Pozdravljeni, jaz sem {self.kaj_sem()} {self.ime}.")

    def kaj_sem(self):
        return "gospod" if self.spol == "M" else "gospa"


class Student(Oseba):
    def __init__(self, ime, spol):
        super().__init__(ime, spol)
        self.lokacija = None
        self.stol = None
        self.ocene = {}

    def premakni(self, predavalnica):
        pass

    def oceni(self, predmet, ocena):
        self.ocene[predmet] = ocena

    def pozdrav(self):
        super().pozdrav()
        if not self.lokacija:
            print("Nimam pojma, kje sem")
        else:
            print(f"Sem v predavalnici {self.lokacija.ime()} na stolu {self.stol}")

    def vstopi(self, predavalnica):
        self.lokacija = predavalnica

    def kje_sem(self):
        return self.lokacija

    def sedi(self, stol):
        if self.kje_sem().zasedeni(stol):
            self.stol = stol

    def vstani(self):
        self.kje_sem().sprosti(self.stol)
        self.stol = None

    def kaj_sem(self):
        return "student" if self.spol == "M" else "studentka"


class Profesor(Oseba):
    def __init__(self, ime, naziv):
        spol = "MŽ"[naziv[-1] == "a"]
        super().__init__(ime, spol)
        self.naziv = naziv

    def kaj_sem(self):
        return self.naziv


class Bruc(Student):
    def plonkaj(self, predmet):
        self.oceni(predmet, 10)


class Snazilka(Oseba):
    def kaj_sem(self):
        return "snažilka"


class Predavalnica(set):
    def __init__(self, ime, stevilo_stolov):
        super().__init__()
        self.ime = ime
        self.stevilo_stolov = stevilo_stolov

    def zasedeni(self, stol):
        if stol > self.stevilo_stolov or stol in self:
            return False
        else:
            self.add(stol)
            return True

    def sprosti(self, stol):
        assert stol in self
        self.remove(stol)


p1 = Predavalnica("P1", 100)
ana = Student("Ana", "Ž")

