import pygame as pg
import os
from elements import nupp
from elements import tekstikast
import statistika
import time
from algope import file_to_string

vajutus = ""
kirjutatud_tekst = ""
kirjutamise_jarg = -1
viga = False
tippimiste_arv = 0
WPM = 0
ainult_korra = True
kell0 = 0
kirjutatud_sonad = 0
aeg = 0.1
vigade_arv = 0
tekst = ""
tase = statistika.get_tase("edasi")


def edasijoudnud_main(win, wx, wy, hiir, klikk, klahv):
    global vajutus, kirjutatud_tekst, kirjutamise_jarg, viga, tippimiste_arv, kirjutatud_sonad, vigade_arv, WPM, ainult_korra, kell0, aeg, tekst, tase

    if ainult_korra:
        kell0 = time.time()
        win.fill((255, 255, 255))
        vajutus = ""
        if tase <= 10:
            tekst = file_to_string(os.path.join("data", "edasi" + str(tase) + ".txt"))
        ainult_korra = False

    if tase >= 11:
        win.fill((255, 255, 255))
        font = pg.font.SysFont("Arial", 50)
        win.blit(font.render("Mooduli lõpp!", True, (0, 0, 0)),
                 (wx / 2 - font.size("Mooduli lõpp!")[0] / 2, wy / 2 - font.size("Mooduli lõpp!")[1] / 2))

    tagasi = nupp(0, 0, 100, 150, "Tagasi", (0, 0, 170), (255, 255, 255))
    if tagasi.hiire_all(hiir):
        tagasi.varv = (255, 0, 140)
    tagasi.draw(win)
    if tagasi.is_clicked(klikk, hiir):
        statistika.salvesta_sessioon("edasi")
        win.fill((0, 0, 0))
        vajutus = "start"
        kirjutatud_tekst = ""
        kirjutamise_jarg = -1
        kirjutatud_sonad = 0
        aeg = 0.1
        ainult_korra = True
        viga = False
        WPM = 0
        vigade_arv = 0
        return False

    if tase >= 11:
        return True

    if kirjutamise_jarg + 1 >= len(tekst):
        tase += 1
        statistika.tase_ules("edasi")
        if tase <= 10:
            tekst = file_to_string(os.path.join("data", "edasi" + str(tase) + ".txt"))
        kirjutamise_jarg = -1
        kirjutatud_tekst = ""

    kastilaius = 900
    kastipikkus = 525
    kast1 = tekstikast(wx / 2 - kastilaius / 2, 50, kastilaius, kastipikkus)
    if viga:
        kast1.aarise_varv = (255, 0, 0)

    kast1.draw(win)
    kast1.kuva_tekst(win, tekst)


    nihe_nurgast = 40
    pildilaius = 250
    pildikorgus = 250
    taimer = pg.transform.scale(pg.image.load(os.path.join("img", "timer.png")), (pildilaius, pildikorgus))

    win.blit(taimer, (wx - pildilaius - nihe_nurgast, wy - pildikorgus - nihe_nurgast))

    if klahv != "":
        kirjutatud_tekst += klahv
        kirjutamise_jarg += 1
        if tekst[kirjutamise_jarg] != kirjutatud_tekst[kirjutamise_jarg]:
            kirjutamise_jarg -= 1
            kirjutatud_tekst = kirjutatud_tekst[:-1]
            viga = True
            vigade_arv += 1
        else:
            viga = False

            aeg = time.time() - kell0
            if klahv == " ":
                kirjutatud_sonad += 1
    kast1.kuva_tekst(win, kirjutatud_tekst, (0, 200, 0))

    kiiruse_kast = tekstikast(kastilaius - 340, 605, 500, 220, (255, 255, 255))
    kiiruse_kast.aarise_varv = (0, 0, 0)
    kiiruse_kast.draw(win)
    teksti_varv = (0, 0, 0)

    WPM = round(kirjutatud_sonad / (aeg / 60), 4)
    font = pg.font.SysFont("Arial", 25)
    win.blit(font.render("Kirjutatud sõnad: " + str(kirjutatud_sonad), True, teksti_varv), (kastilaius - 330, 620))
    win.blit(font.render("WPM: " + str(WPM), True, teksti_varv), (kastilaius - 330, 660))

    win.blit(font.render("Vigade arv: " + str(vigade_arv), True, teksti_varv), (kastilaius - 330, 700))
    win.blit(font.render("Aeg: " + str(round(aeg, 2)) + " sekundit", True, teksti_varv), (kastilaius - 330, 740))

    if vigade_arv >= 10:
        win.blit(font.render("Proovi täpsem olla!", True, teksti_varv), (kastilaius - 330, 780))

    return True
