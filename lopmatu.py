import pygame as pg
import os
from elements import nupp
from elements import tekstikast
from algope import file_to_string

vajutus = ""
tippimiste_arv = 0
viga = False
kirjutatud_tekst = ""


def lopmatu_main(win, winx, winy, hiir, klikk, klahv):
    global vajutus
    global viga
    global tippimiste_arv
    global kirjutatud_tekst
    vajutus = ""
    win.blit(pg.image.load(os.path.join("img", "tahistaevas.jpg")), (0, 0))

    # nupud
    tagasi = nupp(0, 0, 100, 150, "Tagasi", (0, 0, 170), (255, 255, 255))
    if tagasi.hiire_all(hiir):
        tagasi.varv = (0, 0, 255)
    tagasi.draw(win)
    if tagasi.is_clicked(klikk, hiir):
        vajutus = "start"
        tippimiste_arv = 0
        kirjutatud_tekst = ""
        viga = False
        return False

    # tekstikast
    rlaius = (winx - 2 * 100) / 2
    rkorgus = 85
    riba0 = tekstikast(100, winy / 2 - rkorgus / 2 - 100, rlaius, rkorgus)
    riba1 = tekstikast(100 + rlaius, winy / 2 - rkorgus / 2 - 100, rlaius, rkorgus)
    if viga:
        riba0.aarise_varv = (255, 0, 0)
        riba1.aarise_varv = (255, 0, 0)
    riba0.draw(win)
    riba1.draw(win)

    tekst = file_to_string(os.path.join("data", "test.txt"))
    font = pg.font.SysFont("Arial", 50)
    kuvatav_tekst = tekst[tippimiste_arv: tippimiste_arv + 28]
    if klahv != "":
        if klahv != kuvatav_tekst[0]:
            viga = True
        else:
            tippimiste_arv += 1
            kirjutatud_tekst += klahv
            if len(kirjutatud_tekst) > 28:
                kirjutatud_tekst = kirjutatud_tekst[-28:]
            viga = False

    riba1.kuva_tekst(win, kuvatav_tekst, (0, 0, 0), 50, True)
    win.blit(font.render(kirjutatud_tekst, True, (128, 128, 128)),
             (100 + rlaius - font.size(kirjutatud_tekst)[0], winy / 2 - rkorgus / 2 - 100 + 10))

    return True
