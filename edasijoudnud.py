import pygame as pg
import os
from elements import nupp
from elements import tekstikast

vajutus = ""


def edasi_main(aken, ax, ay, hiir, klikk, klahv):
    global vajutus
    vajutus = ""
    aken.fill((255, 255, 255))

    tagasi_nupp = nupp(0, 0, 100, 100, "tagasi", (0, 255, 0))

    if tagasi_nupp.hiire_all(hiir):
        tagasi_nupp.varv = (255, 0, 0)
    tagasi_nupp.draw(aken)
    if tagasi_nupp.is_clicked(klikk, hiir):
        vajutus = "start"
        aken.fill((0, 0, 0))
        return False

    return True
