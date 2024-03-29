import pygame as pg
import start
import algope
import edasijoudnud
import lopmatu
import statistika

# https://www.pygame.org/docs/

pg.init()
# akna suurus peaks sõltuma kasutaja ekraani suurusest
akenx = 1600
akeny = 900
aken = pg.display.set_mode((akenx, akeny))

# parem jõudlus
aken.set_alpha(None)
pg.event.set_allowed([pg.QUIT, pg.NOEVENT, pg.MOUSEMOTION, pg.MOUSEBUTTONDOWN, pg.KEYDOWN])

pg.display.set_caption("Projekt Gapu")
hiir = pg.mouse.get_pos()
klick = False
klahv = ""

kaivitus = True
start_screen = True
algope_screen = False
edasijoudnute_screen = False
lopmatu_screen = False
statistika_screen = False

# Main loop
while True:
    # ------------------------------------------------------------
    # Sündmused
    if algope_screen:
        e = pg.event.poll()
        if e.type == pg.NOEVENT:
            pg.time.wait(30)  # vajalik animatsiooni toimimiseks
    else:
        if not kaivitus:
            e = pg.event.wait()
        else:
            e = pg.event.poll()
            kaivitus = False

    if e.type == pg.QUIT:
        statistika.salvesta_sessioon("alg")
        statistika.salvesta_sessioon("edasi")
        statistika.salvesta_sessioon("lopmatu")
        break
    if e.type == pg.MOUSEMOTION:
        hiir = pg.mouse.get_pos()
    if e.type == pg.MOUSEBUTTONDOWN:
        klick = True
    if e.type == pg.KEYDOWN:
        klahv = e.unicode

    # Mis hetkel toimub
    if start_screen:  # algusekraan
        start_screen = start.screen(aken, akenx, akeny, hiir, klick)
        if start.vajutus == "alg":
            algope_screen = True
        elif start.vajutus == "edasi":
            edasijoudnute_screen = True
        elif start.vajutus == "lopmatu":
            lopmatu_screen = True
        elif start.vajutus == "statistika":
            statistika_screen = True
    if algope_screen:  # algõppe moodul
        algope_screen = algope.kuva(aken, akenx, akeny, hiir, klick, klahv)
        if algope.vajutus == "start":
            start_screen = True
    if edasijoudnute_screen:  # edasijõudnute moodul
        edasijoudnute_screen = edasijoudnud.edasijoudnud_main(aken, akenx, akeny, hiir, klick, klahv)
        if edasijoudnud.vajutus == "start":
            start_screen = True
    if lopmatu_screen:  # lõpmatu režiimi moodul
        lopmatu_screen = lopmatu.lopmatu_main(aken, akenx, akeny, hiir, klick, klahv)
        if lopmatu.vajutus == "start":
            start_screen = True
    if statistika_screen:
        statistika_screen = statistika.main_screen(aken, akenx, hiir, klick)
        if statistika.vajutus == "start":
            start_screen = True

    # ------------------------------------------------------------
    klick = False
    klahv = ""
    pg.display.update()

pg.quit()
