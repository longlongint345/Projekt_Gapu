import pygame as pg
import os
from elements import nupp
from elements import tekstikast

vajutus = ""


# tagastab igale tähele vastava pildi nime
def sorm(taht):
    taht = taht.lower()
    if taht == 'a' or taht == 'q' or taht == '<' or taht == '>':
        return "vasak_vaike"
    if taht == 'w' or taht == 'z' or taht == 's':
        return "vasak_nimeta"
    if taht == 'd' or taht == 'e' or taht == 'x':
        return "vasak_keskmine"
    if taht == 'f' or taht == 'r' or taht == 'c' or taht == 't' or taht == 'g' or taht == 'v':
        return "vasak_nimetis"
    if taht == 'j' or taht == 'h' or taht == 'u' or taht == 'y' or taht == 'm' or taht == 'n' or taht == 'b':
        return "parem_nimetis"
    if taht == 'i' or taht == 'k' or taht == ',' or taht == ';':
        return "parem_keskmine"
    if taht == 'o' or taht == 'l' or taht == '.' or taht == ":" or taht == 'p':
        return "parem_nimeta"
    if taht == "-" or taht == '_' or taht == "ö" or taht == "ä" or taht == 'ü' or taht == 'õ' or taht == '\'':
        return "parem_vaike"
    return "misiganes"


def kuva(win, wx, wy, hiir, klikk):
    global vajutus
    vajutus = ""
    win.fill((255, 255, 255))
    klaius = 900
    kpikkus = 300
    kast1 = tekstikast(wx / 2 - klaius / 2, 50, klaius, kpikkus)
    kast1.draw(win)

    kpikkus = 150
    kast2 = tekstikast(wx / 2 - klaius / 2, wy - kpikkus - 150, klaius, kpikkus)
    kast2.draw(win)

    # pildid
    plaius = 100  # suhe peab olema 5:8
    pkorgus = 160
    parem = pg.transform.scale(pg.image.load(os.path.join("img", "parem.png")), (plaius, pkorgus))
    vasak = pg.transform.scale(pg.image.load(os.path.join("img", "vasak.png")), (plaius, pkorgus))
    # ...
    win.blit(vasak, (75, wy - pkorgus - 75))
    win.blit(parem, (wx - plaius - 75, wy - pkorgus - 75))

    # nupud
    tagasi = nupp(0, 0, 100, 150, "Tagasi", (0, 0, 0), (255, 255, 255))
    if tagasi.hiire_all(hiir):
        tagasi.varv = (0, 0, 255)
    tagasi.draw(win)
    if tagasi.is_clicked(klikk, hiir):
        win.fill((0, 0, 0))
        vajutus = "start"
        return False

    return True
