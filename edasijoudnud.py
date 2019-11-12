import pygame as pg
import os
from elements import nupp
from elements import tekstikast

vajutus = ""
kirjutatud_tekst = ""
kirjutamise_järg = -1
counter = 0
viga = False


def file_to_string(failinimi):
    sõne = ""
    with open(failinimi, "r", encoding ="utf-8") as fsisse:
        for x in fsisse.readlines():
            tmp = x.strip().split(" ")
            sõne += " ".join(tmp)
    return sõne

def edasijõudnud_main(win, wx, wy, hiir, klikk, klahv):
    global vajutus
    global kirjutatud_tekst
    global kirjutamise_järg
    global counter
    global viga
    vajutus = ""

    tekst = file_to_string(os.path.join("jutt", "transkriptsioon.txt"))
    järgmine_täht = tekst[kirjutamise_järg + 1]  

    win.fill((255, 255, 255))
    kastilaius = 1000
    kastipikkus = 500
    kast1 = tekstikast(wx / 2 - kastilaius / 2, 50, kastilaius, kastipikkus)
    if viga:
        kast1.aarise_varv = (255, 0, 0)
    kast1.draw(win)
    kast1.kuva_tekst(win, tekst)

    #nupud
    tagasi = nupp(0, 0, 100, 150, "Tagasi", (0, 0, 170), (255, 255, 255))
    if tagasi.hiire_all(hiir):
        tagasi.värv = (0, 0, 255)
        tagasi.draw(win)
    if tagasi.is_clicked(klikk, hiir):
        win.fill((0, 0, 0))
        vajutus = "start"
        kirjutatud_tekst = ""
        kirjutamise_järg = -1
        counter = 0
        return False

    if klahv != "":
        kirjutatud_tekst += klahv
        kirjutamise_järg += 1
        if tekst[kirjutamise_järg] != kirjutatud_tekst[kirjutamise_järg]:
            kirjutamise_järg -= 1
            kirjutatud_tekst = kirjutatud_tekst[:-1]
            viga = True
            counter = 0
            #kirjutamisveale saab reageerida siit
    kast1.kuva_tekst(win, kirjutatud_tekst, (0, 200, 0))

    return True

