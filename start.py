import os
import pygame as pg
from elements import nupp

vajutus = ""


def screen(win, wx, hiir, klikk):
    wel_img = pg.image.load(os.path.join("img", "Microsoft_Keyboard.jpg"))
    win.blit(wel_img, (0, 0))

    font = pg.font.SysFont("Arial", 90)
    tekst = font.render("Vali õpperežiim: ", True, (255, 255, 255))
    tekst_koordx = wx / 2 - font.size("Vali õpperežiim: ")[0] / 2
    win.blit(tekst, (tekst_koordx, 75))

    # Nupud
    laius = 400
    korgus = 100
    pos1 = 75 + 200
    alg = nupp(wx / 2 - laius / 2, pos1, korgus, laius, "Algõpe")
    if alg.hiire_all(hiir):
        alg.varv = (0, 0, 255)
    alg.draw(win)
    if alg.is_clicked(klikk, hiir):
        vajutus = "alg"
        win.fill((0, 0, 0))
        return False

    edasi = nupp(wx / 2 - laius / 2, pos1 + korgus + 10, korgus, laius, "Edasijõudnud")
    if edasi.hiire_all(hiir):
        edasi.varv = (0, 0, 255)
    edasi.draw(win)
    if edasi.is_clicked(klikk, hiir):
        vajutus = "edasi"
        win.fill((0, 0, 0))
        return False

    lopmatu = nupp(wx / 2 - laius / 2, pos1 + 2 * korgus + 20, korgus, laius, "Lõpmatu")
    if lopmatu.hiire_all(hiir):
        lopmatu.varv = (0, 0, 255)
    lopmatu.draw(win)
    if lopmatu.is_clicked(klikk, hiir):
        vajutus = "lopmatu"
        win.fill((0, 0, 0))
        return False

    return True
