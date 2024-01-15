import risar
from math import *
import random

class Turtle:
    def __init__(self):
        self.x = risar.maxX / 2
        self.y = risar.maxY / 2
        self.kot = 0
        self.pen_active = True
        self.pause = 0
        self.body = risar.krog(0, 0, 5, risar.zelena, 3)
        self.head = risar.krog(0, 0, 2, risar.zelena, 3)
        self.update()

    def update(self):
        self.body.setPos(self.x, self.y)
        kot = radians(90 - self.kot)
        self.head.setPos(self.x + 5 * cos(kot), self.y - 5 * sin(kot))
        risar.obnovi()
        if self.pause:
            self.wait(self.pause)

    def fly(self, x, y, kot):
        self.x = x
        self.y = y
        self.kot = kot
        self.update()

    def turn(self, obrat):
        self.kot += obrat
        self.update()

    def left(self):
        self.turn(-90)

    def right(self):
        self.turn(90)

    def forward(self, a):
        kot = radians(90 - self.kot)
        nx = self.x + a * cos(kot)
        ny = self.y + a * sin(kot)
        if self.pen_active:
            risar.crta(self.x, self.y, nx, ny)
        self.x, self.y = nx, ny
        self.update()

    def backward(self, a):
        self.forward(-1)

    def pen_up(self):
        self.pen_active = False
        self.update()

    def pen_down(self):
        self.pen_active = True
        self.update()

    def wait(self, pause):
        risar.cakaj(pause)

    def nakljucni_korak(self):
        razdalja = random.randrange(min(self.x, self.y, risar.maxX - self.x, risar.maxY - self.y))
        kot = radians(random.randrange(360))
        self.turn(kot)
        self.forward(razdalja)
