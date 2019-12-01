import os
import pygame as pg
from elements import nupp
from elements import tekstikast


def tase_ules(mooduli_nimi):  # kutsuda välja, kui kasutaja on läbinud mingis moodulis ühe taseme
    if mooduli_nimi not in ("alg", "edasi", "lopmatu"):
        raise Exception("Funktsioonis tase üles sobimatu mooduli nimi.")
    with open(os.path.join("data", "progress.txt"), "r+") as f:
        data = f.readlines()
        if not data:
            f.write("0\n0\n0")
            f.seek(0)
            data = f.readlines()
        for x in range(len(data)):
            data[x] = data[x].strip()
        # esimene rida on algõppele, teine edasijõudnutele ja kolmas lõpmatu mooduli oma
        f.seek(0)
        f.truncate()  # kustutab faili sisu
        if mooduli_nimi == "alg":
            f.write(str(int(data[0]) + 1) + "\n" + data[1] + "\n" + data[2])
        elif mooduli_nimi == "edasi":
            f.write(data[0] + "\n" + str(int(data[1]) + 1) + "\n" + data[2])
        elif mooduli_nimi == "lopmatu":
            f.write(data[0] + "\n" + data[1] + "\n" + str(int(data[2]) + 1))


# faili algseadistamiseks tuleb selle sisu lihtsalt kuskil mujal ära kustutada

def salvesta_sessioon(mooduli_nimi):  # kutsuda välja kui kasutaja vajutab tagasi nuppu (enne muutujate reset'i)
    # ideaalis peaks lisama võimaluse, et see ka X-nuppu vajutades toimuks
    import algope
    import edasijoudnud
    from lopmatu import aeg, WPM
    if mooduli_nimi not in ("alg", "edasi", "lopmatu"):
        raise Exception("Funktsioonis salvesta_sessioon sobimatu mooduli nimi.")

    if mooduli_nimi == "alg":
        pass
    elif mooduli_nimi == "edasi":
        pass
    elif mooduli_nimi == "lopmatu":
        # fail sisaldab harjutamiseks kulunud aega, üleüldist keskmist WPM'i (vastavalt esimesel ja teisel real)
        with open(os.path.join("data", "lopmatu_stat.txt"), "r+") as f:
            data = f.readlines()
            if not data:
                f.write("0\n0")
                f.seek(0)
                data = f.readlines()

            for x in range(len(data)):
                data[x] = data[x].strip()

            aeg_kogu = float(data[0]) + aeg
            keskminewpm = (float(data[1]) + WPM) / 2
            f.seek(0)
            f.truncate()
            f.write(str(aeg_kogu) + "\n" + str(keskminewpm))


def get_stat(mooduli_nimi):  # tagastab listi koos soovitud andmetega (järjekord vastav failis olevale)
    if mooduli_nimi not in ("alg", "edasi", "lopmatu"):
        raise Exception("Funktsioonis get_stat sobimatu mooduli nimi.")
    output = []
    if mooduli_nimi == "alg":
        pass
    elif mooduli_nimi == "edasi":
        pass
    elif mooduli_nimi == "lopmatu":
        with open(os.path.join("data", "lopmatu_stat.txt"), "r") as fsisse:
            for x in fsisse.readlines():
                x = x.strip()
                output.append(float(x))
    if output:
        return output
    else:
        return 10 * [0]  # pikkus suurem kui max statistika elementide arv


def get_tase(mooduli_nimi):  # tagastab taseme, kus kasutaja vastavas moodulis on
    if mooduli_nimi not in ("alg", "edasi", "lopmatu"):
        raise Exception("Funktsioonis get_stat sobimatu mooduli nimi.")

    with open(os.path.join("data", "progress.txt"), "r") as fsisse:
        tasemed = []
        for x in fsisse.readlines():
            x = x.strip()
            tasemed.append(int(x))
        if tasemed:
            if mooduli_nimi == "alg":
                return tasemed[0]
            elif mooduli_nimi == "edasi":
                return tasemed[1]
            elif mooduli_nimi == "lopmatu":
                return tasemed[2]
    return 0


vajutus = ""


def main_screen(win, wx, wy, hiir, klikk):
    global vajutus
    vajutus = ""
    win.fill((255, 255, 255))
    # -------------------------------------------------------------------------------------------------------------------
    # nupud
    tagasi = nupp(0, 0, 100, 150, "Tagasi", (0, 0, 170), (255, 255, 255))
    if tagasi.hiire_all(hiir):
        tagasi.varv = (0, 0, 255)
    tagasi.draw(win)
    if tagasi.is_clicked(klikk, hiir):
        vajutus = "start"
        return False

    laius = 350
    pikkus = 75
    reset = nupp(wx / 2 - laius / 2, 0, pikkus, laius, "Kustuta kogu õppeprotsess", (0, 0, 170), (255, 255, 255))
    if reset.hiire_all(hiir):
        reset.varv = (255, 0, 0)
    reset.draw(win)
    if reset.is_clicked(klikk, hiir):
        with open(os.path.join("data", "alg_stat.txt"), "w") as f:
            pass
        with open(os.path.join("data", "edasi_stat.txt"), "w") as f:
            pass
        with open(os.path.join("data", "lopmatu_stat.txt"), "w") as f:
            pass
        with open(os.path.join("data", "progress.txt"), "w") as f:
            pass

    # --------------------------------------------------------------------------------------------------------------
    # tekstikastid
    laius = 400
    pikkus = 500
    info_alg = tekstikast(wx / 2 - laius / 2 - laius, 300, laius, pikkus)
    info_alg.draw(win)
    info_edasi = tekstikast(wx / 2 - laius / 2, 300, laius, pikkus)
    info_edasi.draw(win)
    info_lopmatu = tekstikast(wx / 2 - laius / 2 + laius, 300, laius, pikkus)
    info_lopmatu.draw(win)

    # pealdised
    varv = (0, 0, 0)
    suurus = 32
    font = pg.font.SysFont("Arial", suurus)
    win.blit(font.render("Algõpe:", True, varv), (wx / 2 - laius / 2 - laius + 10, 250))
    win.blit(font.render("Edasijõudnud:", True, varv), (wx / 2 - laius / 2 + 10, 250))
    win.blit(font.render("Lõpmatu:", True, varv), (wx / 2 - laius / 2 + laius + 10, 250))

    suurus = 24
    font = pg.font.SysFont("Arial", suurus)
    # algõpe kast
    win.blit(font.render("Tase: " + str(get_tase("alg")), True, varv), (wx / 2 - laius / 2 - laius + 10, 310))
    # edasijõudnud kast
    win.blit(font.render("Tase: " + str(get_tase("alg")), True, varv), (wx / 2 - laius / 2 + 10, 310))
    # lõpmatu
    win.blit(font.render("Tase: " + str(get_tase("lopmatu")), True, varv), (wx / 2 - laius / 2 + laius + 10, 310))
    win.blit(font.render("Keskmine WPM: " + str(round(get_stat("lopmatu")[1], 2)), True, varv),
             (wx / 2 - laius / 2 + laius + 10, 360))
    win.blit(font.render("Aeg kokku: " + str(int(get_stat("lopmatu")[0])) + " sekundit", True, varv),
             (wx / 2 - laius / 2 + laius + 10, 410))

    return True
