import pygame as pg
import os
from elements import nupp
from elements import tekstikast
from algope import file_to_string
import time
import statistika

vajutus = ""
tippimiste_arv = 0
viga = False
kirjutatud_tekst = ""
WPM = 0
ainult_korra = True
kell0 = 0
kirjutatud_sonade_arv = 0
aeg = 0.1
vigade_arv = 0
tekst = ""
tase = statistika.get_tase("lopmatu")

def lopmatu_main(win, winx, winy, hiir, klikk, klahv):
    global vajutus
    global viga
    global tippimiste_arv
    global kirjutatud_tekst
    global kirjutatud_sonade_arv
    global vigade_arv
    global WPM
    global ainult_korra
    global kell0
    global aeg
    global tekst
    global tase
    if ainult_korra:  # hiljem saab seda struktuuri kasutada koodi optimeerimiseks
        kell0 = time.time()
        tekst = file_to_string(os.path.join("data", "test.txt"))
        vajutus = ""
        win.blit(pg.image.load(os.path.join("img", "tahistaevas.jpg")), (0, 0))
        ainult_korra = False

    # nupud
    tagasi = nupp(0, 0, 100, 150, "Tagasi", (0, 0, 170), (255, 255, 255))
    if tagasi.hiire_all(hiir):
        tagasi.varv = (0, 0, 255)
    tagasi.draw(win)
    if tagasi.is_clicked(klikk, hiir):  # + reset
        statistika.salvesta_sessioon("lopmatu")
        vajutus = "start"
        tippimiste_arv = 0
        kirjutatud_tekst = ""
        viga = False
        ainult_korra = True
        WPM = 0
        kell0 = 0
        kirjutatud_sonade_arv = 0
        aeg = 0.1
        vigade_arv = 0
        tekst = ""
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

    font = pg.font.SysFont("Arial", 50)
    kuvatav_tekst = tekst[tippimiste_arv: tippimiste_arv + 28]
    if klahv != "":
        if klahv != kuvatav_tekst[0]:
            viga = True
            vigade_arv += 1
        else:
            tippimiste_arv += 1
            kirjutatud_tekst += klahv
            if len(kirjutatud_tekst) > 28:
                kirjutatud_tekst = kirjutatud_tekst[-28:]
            viga = False

            # kirjutamise kiiruse mõõtmiseks
            aeg = time.time() - kell0
            if klahv == " ":
                kirjutatud_sonade_arv += 1

    win.blit(font.render(kirjutatud_tekst, False, (128, 128, 128)),
             (100 + rlaius - font.size(kirjutatud_tekst)[0], winy / 2 - rkorgus / 2 - 100 + 10))
    win.blit(font.render(kuvatav_tekst, False, (0, 0, 0)), (100 + rlaius, (winy / 2 - rkorgus / 2 - 100) + 10))

    # statistika
    stat_kast = tekstikast(rlaius - 10, 160, 220, 115, (0, 0, 0))
    stat_kast.aarise_varv = (255, 255, 255)
    stat_kast.draw(win)
    # Sõnu minutis
    WPM = round(kirjutatud_sonade_arv / (aeg / 60), 4)
    font = pg.font.SysFont("Arial", 25)
    win.blit(font.render("WPM: " + str(WPM), True, (255, 255, 255)), (rlaius, 170))

    # vigade arv
    win.blit(font.render("Vigade arv: " + str(vigade_arv), True, (255, 255, 255)), (rlaius, 200))

    # Korrektsus
    if tippimiste_arv != 0:
        korrektsus = 100 - ((vigade_arv / tippimiste_arv) * 100)
        if korrektsus < 0:
            korrektsus = 0
    else:
        korrektsus = 0
    win.blit(font.render("Korrektsus: " + str(int(round(korrektsus, 0))) + "%", True, (255, 255, 255)), (rlaius, 230))

    return True
