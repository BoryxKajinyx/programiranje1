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
        self.ocene = {}
        self.znanje = {}

    def oceni(self, predmet, ocena):
        self.ocene[predmet] = ocena
        self.znanje[predmet] = ocena

    def kaj_sem(self):
        return "student" if self.spol == "M" else "studentka"


class Profesor(Oseba):
    def __init__(self, ime, naziv):
        if naziv[-1] == "a":
            spol = "Ž"
        else:
            spol = "M"
        super().__init__(ime, spol)
        self.naziv = naziv

    def kaj_sem(self):
        return self.naziv


class Bruc(Student):
    def plonkaj(self, predmet):
        self.oceni(predmet, 10)
        self.znanje[predmet] = 0

