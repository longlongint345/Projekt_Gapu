import pygame as pg
import start
import algope
import edasijoudnud
import lopmatu

# https://www.pygame.org/docs/

pg.init()
# akna suurus peaks sõltuma kasutaja ekraani suurusest
akenx = 1600
akeny = 900
aken = pg.display.set_mode((akenx, akeny))
pg.display.set_caption("Projekt Gapu")
hiir = pg.mouse.get_pos()
klick = False
klahv = ""

start_screen = True
algope_screen = False
edasijoudnute_screen = False
lopmatu_screen = False

# Main loop
while True:
    # ------------------------------------------------------------
    # Sündmused
    if algope_screen:
        e = pg.event.poll()
        if e.type == pg.NOEVENT:
            pg.time.wait(30)  # vajalik animatsiooni toimimiseks
    else:
        e = pg.event.wait()


    if e.type == pg.QUIT:
        break
    if e.type == pg.MOUSEMOTION:
        hiir = pg.mouse.get_pos()
    if e.type == pg.MOUSEBUTTONDOWN:
        klick = True
    if e.type == pg.KEYDOWN:
        klahv = e.unicode

    # Mis hetkel toimub
    if start_screen:  # algusekraan
        start_screen = start.screen(aken, akenx, hiir, klick)
        if start.vajutus == "alg":
            algope_screen = True
        elif start.vajutus == "edasi":
            edasijoudnute_screen = True
        elif start.vajutus == "lopmatu":
            lopmatu_screen = True
    if algope_screen:  # algõppe moodul
        algope_screen = algope.kuva(aken, akenx, akeny, hiir, klick, klahv)
        if algope.vajutus == "start":
            start_screen = True
    if edasijoudnute_screen:  # edasijõudnute moodul
        edasijoudnute_screen = edasijoudnud.edasijõudnud_main(aken, akenx, akeny, hiir, klick, klahv)
        if edasijoudnud.vajutus == "start":
            start_screen = True
    if lopmatu_screen:  # lõpmatu režiimi moodul
        lopmatu_screen = lopmatu.lopmatu_main(aken, akenx, akeny, hiir, klick, klahv)
        if lopmatu.vajutus == "start":
            start_screen = True

    # ------------------------------------------------------------
    klick = False
    klahv = ""
    pg.display.update()

pg.quit()
