import pygame as pg
import os
from elements import nupp
from elements import tekstikast
import statistika
import time

vajutus = ""
kirjutatud_tekst = ""
kirjutamise_järg = -1
viga = False
tippimiste_arv = 0
WPM = 0
ainult_korra = True
kell0 = 0
kirjutatud_sõnad = 0
aeg = 0.1
vigade_arv = 0
tekst = ""
tase = statistika.get_tase("edasi")


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
    global viga
    global tippimiste_arv
    global kirjutatud_sõnad
    global vigade_arv
    global WPM
    global ainult_korra
    global kell0
    global aeg
    global tekst
    global tase
    if ainult_korra:
        kell0 = time.time()
        ainult_korra = False
    
    tekst = file_to_string(os.path.join("jutt", "edasi" + str(tase) + ".txt"))

    if kirjutamise_järg + 1 >= len(tekst):
        tase += 1
        statistika.tase_ules("edasi")
        kirjutamise_järg = -1
        kirjutatud_tekst = ""
        
 #   tekst = file_to_string(os.path.join("jutt", "edasi1.txt"))
    järgmine_täht = tekst[kirjutamise_järg + 1]  

    win.fill((255, 255, 255))
    kastilaius = 900
    kastipikkus = 400
    kast1 = tekstikast(wx / 2 - kastilaius / 2, 50, kastilaius, kastipikkus)
    if viga:
        kast1.aarise_varv = (255, 0, 0)

    kast1.draw(win)
    kast1.kuva_tekst(win, tekst)

    tagasi = nupp(0, 0, 100, 150, "Tagasi", (0, 0, 170), (255, 255, 255))
    if tagasi.hiire_all(hiir):
        tagasi.varv = (255, 0, 140)
    tagasi.draw(win)
    if tagasi.is_clicked(klikk, hiir):
        win.fill((0, 0, 0))
        vajutus = "start"
        kirjutatud_tekst = ""
        kirjutamise_järg = -1
        return False
    
    nihe_nurgast = 40
    pildilaius = 250
    pildikõrgus = 250
    taimer = pg.transform.scale(pg.image.load(os.path.join("img", "timer.png")), (pildilaius, pildikõrgus))

    win.blit(taimer, (wx - pildilaius - nihe_nurgast, wy - pildikõrgus - nihe_nurgast))

    if klahv != "":
        kirjutatud_tekst += klahv
        kirjutamise_järg += 1
        if tekst[kirjutamise_järg] != kirjutatud_tekst[kirjutamise_järg]:
            kirjutamise_järg -= 1
            kirjutatud_tekst = kirjutatud_tekst[:-1]
            viga = True
            vigade_arv += 1
        else:
            viga = False
            
            aeg = time.time() - kell0
            if klahv == " ":
                kirjutatud_sõnad += 1
    kast1.kuva_tekst(win, kirjutatud_tekst, (0, 200, 0))

    kiiruse_kast = tekstikast(kastilaius - 340, 600, 500, 200, (0, 0, 0))
    kiiruse_kast.aarise_varv = (255, 255, 255)
    kiiruse_kast.draw(win)

    WPM = round(kirjutatud_sõnad / (aeg / 60), 4)
    font = pg.font.SysFont("Arial", 25)
    
    win.blit(font.render("Kirjutatud sõnad: " + str(kirjutatud_sõnad), True, (255, 255, 255)), (kastilaius - 330, 610))
    win.blit(font.render("WPM: " + str(WPM), True, (255, 255, 255)), (kastilaius - 330, 650))

    win.blit(font.render("Vigade arv: " + str(vigade_arv), True, (255, 255, 255)), (kastilaius - 330, 690))
    win.blit(font.render("Aeg: " + str(aeg) + "sekundit", True, (255, 255, 255)), (kastilaius - 330, 730))
    
    if vigade_arv >= 10:
        win.blit(font.render("Proovi täpsem olla!", True, (255, 255, 255)), (kastilaius - 330, 770))
    
    
    
    return True
    


    


