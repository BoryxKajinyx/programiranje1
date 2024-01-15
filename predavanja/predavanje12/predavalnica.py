class Predavalnica:
    def __init__(self, ime, stevilo_stolov):
        super().__init__()
        self.ime = ime
        self.zasedeni = [None] * stevilo_stolov

    def zasedi(self, stol, ime):
        if stol > len(self.zasedeni) or self[stol]:
            return False
        self[stol] = ime
        return True

    def sprosti(self, stol):
        assert stol in self
        assert stol < len(self.zasedeni)
        self[stol] = None

    def __str__(self):  # Posebna metoda za print
        return self.ime

    def __len__(self):
        return len(self.zasedeni) - self.zasedeni.count(None)

    def __getitem__(self, item):
        return self.zasedeni[item]

    def __setitem__(self, key, value):
        self.zasedeni[key] = value

    def __bool__(self):
        return len(self) > 0

    def __iter__(self):
        return self.zasedeni

