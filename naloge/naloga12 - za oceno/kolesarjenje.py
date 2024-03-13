import random
import pygame


class Ovira:
    def __init__(self):
        self.tip = random.randrange(7)
        self.slika = pygame.image.load("zvok-in-slika\\" + dat[self.tip])
        self.sirina, self.visina = self.slika.get_size()
        self.y = 0
        self.x = random.randrange(zaslon.get_width() - self.sirina)
        self.trceno = False
        self.zvok = pygame.mixer.Sound("zvok-in-slika\\explosion.mp3") if self.tip != 6\
            else pygame.mixer.Sound("zvok-in-slika\\jump.mp3")

    def update(self, zasl, igr):
        if igr.zivljenja > 0:
            self.y += 1 + (igr.tocke // 5 + 1) / 10
        self.trk(igr)
        if not self.trceno:
            zasl.blit(self.slika, (self.x, self.y))

    def trk(self, igr):
        if self.y + self.visina > igr.y and igr.x - self.sirina < self.x < igr.x + igr.sirina and not self.trceno:
            self.trceno = True
            self.zvok.play()
            if self.tip == 6:
                igr.tocke += 1
            else:
                igr.zivljenja -= 1


class Igralec:
    def __init__(self):
        self.slika = pygame.image.load("zvok-in-slika\\" + "kolesar.png")
        self.sirina, self.visina = self.slika.get_size()
        self.y = zaslon.get_height() - self.visina
        self.x = zaslon.get_width() // 2
        self.zivljenja = 3
        self.tocke = 0

    def levo(self):
        if self.x > 0:
            self.x -= 2 + (self.tocke // 5 + 1) / 10

    def desno(self):
        if self.x < zaslon.get_width() - self.sirina:
            self.x += 2 + (self.tocke // 5 + 1) / 10

    def update(self, zasl, keys):
        if self.zivljenja > 0:
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                igralec.levo()
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                igralec.desno()
        zasl.blit(self.slika, (self.x, self.y))


pygame.init()
pygame.font.init()
pygame.mixer.init()
font = pygame.font.Font(pygame.font.get_default_font(), 20)
zaslon = pygame.display.set_mode((800, 600))
ura = pygame.time.Clock()
cas_ovire = 0
ovire = []
dat = ["bottle.png", "flowers.png", "grass.png", "scooter.png", "stones.png", "walker.png", "mol.png"]
igralec = Igralec()
pygame.mixer.set_reserved(0)
konec = False
hrup = pygame.mixer.Sound("zvok-in-slika\\arcade.mp3")
pygame.mixer.Channel(0).play(hrup, -1)
while not konec:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            konec = True
            break

    zaslon.fill("black")
    for ovira in ovire:
        ovira.update(zaslon, igralec)
        if ovira.y > zaslon.get_height():
            ovire = ovire[1:]

    igralec.update(zaslon, pygame.key.get_pressed())
    if igralec.zivljenja == 0:
        pygame.mixer.Channel(0).stop()

    tocke_t = font.render(f"Točke: {igralec.tocke:<3}", False, "white")
    zaslon.blit(tocke_t, (0, 0))
    nivo_t = font.render(f"Nivo: {igralec.tocke // 5 + 1:<3}", False, "white")
    zaslon.blit(nivo_t, (zaslon.get_width() / 2 - nivo_t.get_width(), 0))
    zivljenja_t = font.render(f"Življenja: {igralec.zivljenja:1}", False, "white")
    zaslon.blit(zivljenja_t, (zaslon.get_width() - zivljenja_t.get_width(), 0))

    pygame.display.flip()
    if cas_ovire == 0:
        ovire.append(Ovira())
        cas_ovire = random.randrange(30, 160 - 10 * (igralec.tocke // 5 + 1)) if igralec.tocke < 65 else 30
    elif igralec.zivljenja > 0:
        cas_ovire -= 1
    ura.tick(480)
pygame.quit()
