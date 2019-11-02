import pygame as pg


class nupp():
    def __init__(self, x, y, pikkus, laius, tekst, varv=(255, 255, 255), t_varv=(0, 0, 0)):
        self.x = x
        self.y = y
        self.pikkus = pikkus
        self.laius = laius
        self.tekst = tekst
        self.varv = varv
        self.teksti_varv = t_varv

    def get_koord(self):  # tagastab enniku kujul klikkimise jaoks vajalikud nupu koordnaadid
        return ((self.x, self.x + self.laius), (self.y, self.y + self.pikkus))

    def draw(self, aken):  # joonistab nupu koos sellel oleva tekstiga
        pg.draw.rect(aken, self.varv, (self.x, self.y, self.laius, self.pikkus))
        font = pg.font.SysFont("Arial", 24)
        tekst = font.render(self.tekst, True, self.teksti_varv)
        tekst_koordx = self.x + self.laius / 2 - font.size(self.tekst)[0] / 2
        tekst_koordy = self.y + self.pikkus / 2 - font.size(self.tekst)[1] / 2
        aken.blit(tekst, (tekst_koordx, tekst_koordy))

    def hiire_all(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.laius:
            if pos[1] > self.y and pos[1] < self.y + self.pikkus:
                return True
        return False

    def is_clicked(self, klikk, pos):  # true kui nuppu on hiirega klikitud
        if self.hiire_all(pos) and klikk:
            return True
        return False


class menu():
    def __init__(self, ridade_arv):
        self.r_arv = ridade_arv
        self.laius = 150
