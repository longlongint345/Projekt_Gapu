import pygame as pg
import os
from elements import nupp
from elements import tekstikast

vajutus = ""
kirjutatud_tekst = ""
kirjutamise_jarg = -1
counter = 0
viga = False


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
    if taht == " ":
        return "parem_poial"
    return "misiganes"


def file_to_string(pathtofnimi):
    sone = ""
    with open(pathtofnimi, "r") as fsisse:
        for x in fsisse.readlines():
            tmp = x.strip().split(" ")
            sone += " ".join(tmp)
    return sone


def klahvi_asukoht(k):
    moot = 60
    algx = 410
    algy = 526
    k = k.lower()
    rida0 = "1234567890+"
    rida01 = "!\"#¤%&/()=?"
    rida02 = "¹@£$½¬{[]}\\"
    rida1 = "qwertyuiopüõ"
    rida2 = "asdfghjklöä'"
    rida3 = "<zxcvbnm,.-"
    erandid = "€šž>|;:_ "
    if k in rida0:
        return ((rida0.index(k) * moot + algx, algy))
    elif k in rida01:
        return ((rida01.index(k) * moot + algx, algy))
    elif k in rida02:
        return ((rida02.index(k) * moot + algx, algy))
    elif k in rida1:
        algy += moot
        algx = (algx + (algx + moot)) / 2
        return ((rida1.index(k) * moot + algx, algy))
    elif k in rida2:
        algy += (2 * moot)
        algx = (((algx + (algx + moot)) / 2) + (algx + moot)) / 2
        return ((rida2.index(k) * moot + algx, algy))
    elif k in rida3:
        algy += (3 * moot)
        algx = ((((algx + (algx + moot)) / 2) + (algx + moot)) / 2) - (moot / 2)
        return ((rida3.index(k) * moot + algx, algy))
    elif k in erandid:  # NB! erandid lisada
        if k == " ":
            return (590, 766)
    else:
        raise Exception("Ei leia tähte andmebaasist.")


def kuva(win, wx, wy, hiir, klikk, klahv):
    global vajutus
    global kirjutatud_tekst
    global kirjutamise_jarg
    global counter
    global liikumine
    global viga
    vajutus = ""

    tekst = file_to_string(os.path.join("data", "test.txt"))
    jargmine_taht = tekst[kirjutamise_jarg + 1]  # NB! et teksti lõpus listist välja ei läheks

    win.fill((255, 255, 255))
    klaius = 900
    kpikkus = 400
    kast1 = tekstikast(wx / 2 - klaius / 2, 50, klaius, kpikkus)
    if viga:
        kast1.aarise_varv = (255, 0, 0)
    kast1.draw(win)
    kast1.kuva_tekst(win, tekst)

    nihe_nurgast = 75
    kpikkus = 300
    kast2 = tekstikast(wx / 2 - klaius / 2 - 10, wy - kpikkus - 10 - nihe_nurgast, klaius + 20, kpikkus + 20)
    kast2.draw(win)

    # pildid
    plaius = 125  # suhe peab olema 5:8
    pkorgus = 200
    parem = pg.transform.scale(pg.image.load(os.path.join("img", "parem.png")), (plaius, pkorgus))
    vasak = pg.transform.scale(pg.image.load(os.path.join("img", "vasak.png")), (plaius, pkorgus))
    klaviatuur = pg.transform.scale(pg.image.load(os.path.join("img", "Estonian.png")), (900, 300))

    win.blit(vasak, (nihe_nurgast, wy - pkorgus - nihe_nurgast))
    win.blit(parem, (wx - plaius - nihe_nurgast, wy - pkorgus - nihe_nurgast))
    win.blit(klaviatuur, (wx / 2 - 900 / 2, wy - 300 - nihe_nurgast))

    # helendavate (läbipaistvus) klahvide kujutamine
    if jargmine_taht != " ":
        pind = pg.Surface((60, 60))
        pind.set_alpha(150)
        pind.fill((255, 255, 0))
        win.blit(pind, (klahvi_asukoht(jargmine_taht)[0], klahvi_asukoht(jargmine_taht)[1]))
    elif jargmine_taht == " ":
        pind = pg.Surface((6 * 60, 60))
        pind.set_alpha(150)
        pind.fill((255, 255, 0))
        win.blit(pind, (klahvi_asukoht(jargmine_taht)[0], klahvi_asukoht(jargmine_taht)[1]))

    # nupud
    tagasi = nupp(0, 0, 100, 150, "Tagasi", (0, 0, 170), (255, 255, 255))
    if tagasi.hiire_all(hiir):
        tagasi.varv = (0, 0, 255)
    tagasi.draw(win)
    if tagasi.is_clicked(klikk, hiir):  # moodulist väljumine ja muutujate algseadistamine
        win.fill((0, 0, 0))
        vajutus = "start"
        kirjutatud_tekst = ""
        kirjutamise_jarg = -1
        counter = 0
        return False

    # teksti sisestamine
    if klahv != "":
        kirjutatud_tekst += klahv
        kirjutamise_jarg += 1
        if tekst[kirjutamise_jarg] != kirjutatud_tekst[kirjutamise_jarg]:
            kirjutamise_jarg -= 1
            kirjutatud_tekst = kirjutatud_tekst[:-1]
            viga = True
            counter = 0
            # kirjutamisveale saab reageerida siit
    kast1.kuva_tekst(win, kirjutatud_tekst, (0, 200, 0))

    # animatsiooni(de) kuvamine
    anim = sorm(jargmine_taht)
    if counter <= 5:
        if anim[0] == 'p':
            win.blit(pg.transform.scale(pg.image.load(os.path.join("img", anim + ".png")), (plaius, pkorgus)),
                     (wx - plaius - nihe_nurgast, wy - pkorgus - nihe_nurgast))
        elif anim[0] == 'v':
            win.blit(pg.transform.scale(pg.image.load(os.path.join("img", anim + ".png")), (plaius, pkorgus)),
                     (nihe_nurgast, wy - pkorgus - nihe_nurgast))
        counter += 1
    elif counter <= 10:
        counter += 1
    else:
        viga = False
        counter = 0

    return True
