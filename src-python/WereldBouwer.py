"""
A modest program for designing stage new worlds.

The original was written in BASIC by Stephen Kimmel and published in the June 1983 issue of
[Creative Computing Magazine](https://archive.org/details/CreativeComputing198306/page/n263/mode/2up).

This version is based on the Dutch translation made by Steven Bolt and Carl Koppeschaar
and published in January 1984 in the monthly magazine [KIJK](https://www.kijkmagazine.nl/).
"""
import math
import os
from spectral_type import SpectralType, InvalidSpectralType
from star import Star
from star_db import star_list, get_star


def clear_screen():
    if os.name == 'nt':
        # for windows
        os.system('cls')
    else:
        # for mac and linux (here, os.name is 'posix')
        os.system('clear')


def format_print(ident, width, lines):
    for line in lines:
        while True:
            print(' ' * ident, end='')
            if len(line) < width:
                print(line)
                break
            pos = line[:width + 1].rfind(' ')
            print(line[:pos])
            line = line[pos+1:]


def confirm(question):
    while True:
        answer = input(question)
        if len(answer) > 0:
            if answer[0].lower() in ('j', 'y'):
                return True
            if answer[0].lower() == 'n':
                return False


def title_screen():
    clear_screen()
    format_print(10, 50, [
        "\n\n",
        "** WERELD BOUWER **\n",
        "door Stephen Kimmel",
        "een programma voor",
        "de bouw van vreemde",
        "nieuwe werelden....\n",
        "(Druk op Enter)"
    ])
    _ = input()


def cnv(z):
    """ Convert degrees fahrenheit to degrees celsius"""
    return ((z - 32) / 0.18 + 0.5) / 10


def menu_screen():
    clear_screen()
    format_print(10, 50, [
        "\n\n",
        "      && WERELD BOUWER &&\n",
        "tik het nr. van de gewenste operatie\n",
        "1) gebruik een bekende ster",
        "2) gebruik een andere ster",
        "3) druk een lijst van bekende sterren",
        "4) stop\n"
    ])
    return input("          Uw keus: ")


def list_stars():
    clear_screen()
    print("Dit zijn de sterren op mijn lijstje:\n")
    stars = star_list()
    rows = int(len(stars) / 2)
    for i in range(rows):
        print(f"  {stars[i]:<38}{stars[i + rows]}")


def select_known_star():
    name = input("\nWelke ster zal ik gebruiken? ")
    star = get_star(name)
    if star is None:
        _ = input("Die ster is mij niet bekend.")
        return
    show_stellar_data(star)
    if confirm("\nWilt u een andere ster? "):
        return
    return star


def define_own_star():
    clear_screen()
    s = input("Hoe heet de ster? ")
    star = Star(s)
    mass = 0.0
    l = 0.0
    p = 0
    while True:
        s1 = input("\nWat is de spectraalklasse? ")
        if len(s1) == 0 or s1[0] in ('/', '?'):
            m = float(input("\nAbsolute magnitude ( zon=4.85 )? "))
            l = 2.512 ** (4.85 - m)
            mass = l ** 0.285714
            star.spectral_type = SpectralType.type_from_mass(mass)
            break
        elif len(s1) == 2:
            try:
                star.spectral_type = SpectralType(s1)
            except InvalidSpectralType:
                print("\nDie klasse is mij onbekend.")
                continue
            mass = star.spectral_type.mass()
            break
        else:
            print("<letter><cijfer> verwacht")
            continue
    as1 = mass ** -2.5 * 10
    while True:
        print(f"\n{s} heeft een verwachte levensduur van ")
        print(f"{as1:.1f} miljard jaar ")
        p = float(input("\nWelk percentage (1-100) is voorbij? "))
        if p / 100 * as1 < 18:
            break
        print("\nHet universum is circa 18 miljard jaar oud.")
        if confirm("\nWilt u een ander percentage? "):
            break
    mass = mass * (1.25 - 0.005 * p)
    l = mass ** 3.5
    star.mass = mass
    star.luminosity = l
    star.lifespan = as1
    star.life_fraction = p / 100
    show_stellar_data(star)
    if confirm("\nWilt u een andere ster? "):
        return
    return star


def show_stellar_data(star):
    clear_screen()
    format_print(10, 50, [
        "\n\n",
        "** STELLAR DATA **\n"
    ])
    format_print(10, 50, star.description())


def planet_data(star):
    hm = 0
    clear_screen()
    print("\n** PLANEET-GEGEVENS **\n")
    print("De aarde heeft een gemiddelde oppervlakte")
    print("temperatuur van 16 graden Celsius.")
    tp = int(input("Welke temperatuur wenst u? "))
    tp = 1.8 * tp + 492
    g = -1.0
    while g <= 0:
        print("\nGewenste zwaartekracht aan de oppervlakte")
        g = float(input("(aarde=1)? "))
        if g <= 0:
            print("Enige zwaartekracht is noodzakelijk.")
    rp = math.sqrt(star.luminosity / (tp / 520) ** 4)
    if rp <= star.mass / 5:
        print("\nDeze planeet bevindt zich te dicht bij haar zon")
        print("om stabiel te zijn.")
        _ = input("Druk op Enter")
        return False
    pp = math.sqrt(rp ** 3 / star.mass)
    rm = math.sqrt(1 / 1.929)
    rx = math.sqrt(1 / 0.694)
    ds = star.mass ** 0.3333
    sa = ds / rp
    print("\nHoe groot moet de planeet zijn in verhouding")
    d = float(input("tot de aarde? "))
    m = g * d ** 2
    if m < 0.055:
        print("Deze planeet zal geen zuurstofatmosfeer vasthouden.")
    if m > 17.6:
        print("Deze planeet zal haar waterstofatmosfeer niet kwijtraken.")
    ec = 2
    while ec > 1:
        print("\nDe baan van de aarde heeft een excentriciteit")
        ec = float(input("van 0.01672 Gewenste excentriciteit (<1)? "))
    ca = (1 - ec) * rp
    fa = (1 + ec) * rp
    t1 = 100
    while t1 < 0 or t1 > 90:
        print("\nWat is de hoek van de rotatie-as (aarde =23.5 graden)?")
        t1 = float(input())

    mcnt = int(input("\nHoeveel manen wenst u? "))
    if mcnt > 10:
        print("Voor het gemak beperken we dat tot 10.")
        mcnt = 10
    mm = 1000
    h = 0
    r = 56 * g
    mn = []
    mr = []
    mp = []
    if mcnt > 0:
        for i in range(mcnt):
            mn.append(float(input(f"Massa maan nr.{i + 1} (onze maan = 1)? ")))
            while True:
                tmp = float(input("Baanstraal (onze maan = 30)? "))
                if tmp < 3 * g:
                    print("Te dichtbij; ze zal in stukken breken.")
                    continue
                if tmp > 56 * g:
                    print("Te ver weg; ze ontsnapt.")
                    continue
                break
            mr.append(tmp)
            mp.append(math.sqrt(tmp ** 3 / m) * 4)
            if mr[i] < r:
                mm = mp[i]
                r = mr[i]
            h = mn[i] * 0.01235 / (mr[i] ** 3) + h
    h2 = 0.85 * d ** 4 / m * (star.mass * 333500 / (11759 * rp) ** 3 + h)
    da = 1759260 * h2 * 14 + 10
    if da > mm:
        da = mm

    clear_screen()
    print("\n\n** PLANEET-GEGEVENS **")
    print(f"\nEen dag duurt op deze planeet ongeveer {da:.2f} uur")
    yd = int(87660 / da * pp + .5) / 10
    print(f"Een jaar duurt {yd:.1f} dagen")
    print("De hoek van de rotatie-as heeft de volgende")
    print("invloeden op het klimaat:")
    hi = (1 + 0.025 * da / 24) * tp - 460
    lo = (1 - 0.025 * da / 24) * tp - 460
    if lo < -460:
        lo = -460
    print(f"De maximumtemperatuur is vandaag {cnv(hi):.0f} graden C")
    print(f"Vannacht zal de temperatuur dalen tot {cnv(lo):.0f} graden C")
    sh = hi + 1.9 * t1 * (1 + ec) ** 2
    ll = lo - 1.9 * t1 / (1 + ec) ** 2
    if ll < -460:
        ll = -460
    print(f"'s Zomers kan de temperatuur stijgen tot {cnv(sh):.0f} graden C")
    print(f"'s Winters verwachten we een minium van {cnv(ll):.0f} graden C")
    if sh <= 32 or ll >= 175:
        print("Er zijn perioden waarin geen vloeibaar water kan bestaan.")

    if mcnt > 0:
        _ = input("\nDruk op Enter voor informatie over het manenstelsel.")
        if mcnt > 1:
            for i in range(mcnt):
                f = 0
                for k in range(mcnt - 1):
                    if mr[k + 1] < mr[k]:
                        mr[k], mr[k + 1] = mr[k + 1], mr[k]
                        mn[k], mn[k + 1] = mn[k + 1], mn[k]
                        mp[k], mp[k + 1] = mp[k + 1], mp[k]
                        f = 1
                if f == 0:
                    break
        clear_screen()
        print("\n\n** HET MANENSTELSEL **")
        print("\nbaanstraal  massa   periode\n")
        for i in range(mcnt):
            print(f"{mr[i]:7.1f} {mn[i]:8.2f} {mp[i] / da:9.2f} dagen")

    _ = input("\nDruk op Enter")

    clear_screen()
    print("\n\n** PLANEET-GEGEVENS **\n")
    print("Deze planeet heeft een gemiddelde")
    print(f"oppervlakte temperatuur van {cnv(tp - 460):.0f}")
    print("graden C. Dit betekent een baanstraal")
    print(f"van {rp:.2f} astronomische eenheden")
    print(f"({rp * 150:.1f} miljoen km.).")
    print(f"Perihelium = {ca:.2f} ae")
    print(f"Aphelium = {fa:.2f} ae")
    print(f"Een jaar is {pp:.2f} aardjaren lang.")
    print(f"{star.name} lijkt ", end='')
    if sa > 1.5 or sa < 0.75:
        print("veel ", end='')
    if sa > 1:
        print("groter ", end='')
    else:
        print("kleiner ", end='')
    print("dan onze zon.")
    if 0.95 < g < 1.05:
        print("De zwaartekracht is vrijwel gelijk")
        print("aan die van de aarde.")
    else:
        print("Aangezien de zwaartekracht")
        if g > 1:
            print("groter is dan op aarde verwachten we")
            print("een dichtere atmosfeer. De tektonische")
            print("werking is groter, maar er is ook")
            print("meer weerstand. We verwachten daarom")
            print("meer continenten en kleinere bergen;")
            print("Aardbevingen komen vaker voor en zijn")
            print("heviger.")
        else:
            print("kleiner is dan op aarde verwachten we")
            print("een dunnere atmosfeer. Er is minder")
            print("tektonische werking en ook de")
            print("weerstand is kleiner. We verwachten")
            print("daarom minder bergen, maar ze kunnen")
            print("veel hoger worden.")
            print("Aardbevingen, als ze al voorkomen,")
            print("zullen minder hevig zijn.")
        print("Een zwaartekracht van {:.2f} g betekent".format(g))
        print("dat iemand van 80 kilo op deze")
        print("planeet {:.1f} kilo zou wegen.".format(g * 80))

    _ = input("\nDruk op Enter voor informatie over leven")
    clear_screen()
    print("\n** LEVEN? **\n")
    live = True
    if m < 0.055 or m > 17.6:
        print("Vanwege de slechte atmosfeer")
        live = False
    if rp < rm or rp > rx:
        print("Vanwege de afstand tot de zon")
        live = False
    if sh < 32 or ll > 175:
        print("Aangezien er nooit vloeibaar water is")
        live = False
    if star.lifespan * star.life_fraction <= 1.5:
        print("De planeet is te jong; er kan nog")
        print("geen leven zijn ontstaan.")
        live = False
    if star.life_fraction >= 0.95:
        print(f"Aangezien {star.name} op haar")
        print("sterbed ligt")
        live = False
    if live:
        print("Mogelijk zijn er ", end='')
        if star.lifespan * star.life_fraction < 2 * g:
            print("bacterien en")
            print("blauwgroene algen.")
        elif star.lifespan * star.life_fraction < 3 * g:
            print("eencelligen met")
            print("een kern.")
        elif star.lifespan * star.life_fraction < 4 * g:
            print("eenvoudige")
            print("meercelligen.")
        elif star.lifespan * star.life_fraction <= 4.4 * g:
            print("gewervelde")
            print("waterdieren en planten op het land.")
        else:
            print("grote op het land")
            print("levende dieren en misschien")
            print("intelligente wezens.")
            if g >= 1.05:
                print("Grotere zwaartekracht betekent een")
                print("dichtere atmosfeer die grote vogels")
                print("kan dragen. Maar zelfs een kleine val")
                print("is dodelijk, zodat hoge reactiesnel-")
                print("heden noodzakelijk zijn. In het")
                print("algemeen zullen levensvormen korter")
                print("en steviger zijn dan op aarde.")
                if g > 1.2:
                    print("Er zijn geen tweebenige wezens")
                    print("zoals wij.")
                print("De dikke atmosfeer verbetert de")
                print("geluidsoverdracht; daarom zullen")
                print("dieren meer op hun gehoor vertrouwen")
            if g < 0.95:
                print("Kleiner zwaartekracht betekent een")
                print("dunnere atmosfeer. Vogels, als ze")
                print("al voorkomen, hebben grote vleugels.")
                print("Alle levensvormen zullen hoger en")
                print("slanker gebouwd zijn dan die op aarde.")
                print("Tweebenige wezens kunnen zeker")
                print("voorkomen.")
                print("De dunne atmosfeer bemoeilijkt")
                print("geluidsoverdracht, zodat de dieren")
                print("grote of helemaal geen oren zullen")
                print("hebben. Hun longen moeten groter zijn.")
                if tp >= 75:
                    print("Het leven moet zich op een of andere.")
                print("manier beschermen tegen het zonlicht.")
                if sa <= 0.75:
                    print("Het leven moet zich op een of andere.")
                    print("manier beschermen tegen het zonlicht.")
            if sa < 0.75:
                print("Vanwege de kleine zon zullen de")
                print("dieren grote ogen hebben of op")
                print("andere zintuigen vertrouwen")
            if sa >= 1.5:
                print("Tenzij de atmosfeer veel licht")
                print("tegenhoudt, zullen de dieren")
                print("kleine ogen hebben.")
            if hi - lo >= 50:
                print("Vanwege de grote temeratuurvariaties")
                print("zal het leven zich vooral ondergronds")
                print("en onder water bevinden.")
            if (tp - 460) < 32 or (
                    tp - 460) > 86 or g > 1.5 or g < 0.68 or m < 0.4 or m > 2.35 or da > 96 or sh > 120 or ll < -30 or hi > 110 or lo < -10:
                hm = 0
            else:
                hm = 1
    else:
        print("zal op deze planeet waarschijnlijk.")
        print("geen leven zijn.")
    print("Mensen zullen deze wereld")
    print("waarschijnlijk ", end='')
    if hm == 0:
        print("on", end='')
    print("bewoonbaar vinden.")
    _ = input("\nDruk op Enter")

    clear_screen()
    print("\n** ANDERE PLANETEN **")
    print("\nHoeveel planeten moet het stelsel")
    print(f"van {star.name} ", end='')
    np = int(input("bevatten? "))
    if np > 15:
        print("We moeten dit beperken tot 15.")
        np = 15
    if np <= 1:
        return True
    am = 1180 / math.sqrt(star.mass) - m * math.sqrt(rp)
    rpl = [rp]
    mp = [m]
    for i in range(1, np):
        clear_screen()
        while True:
            print("\nOns eigen zonnestelsel ziet er zo uit:")
            print("\nplaneet     massa      baanstraal\n")
            print("Mercurius     0.055     0.387")
            print("Venus         0.815     0.723")
            print("Aarde         1.0       1.0")
            print("Mars          0.108     1.524")
            print("Jupiter     317.9       5.203")
            print("Saturnus     95.2       9.539")
            print("Uranus       14.6      19.18")
            print("Neptunus     17.2      30.06")
            print("Pluto         0.100    39.44\n")
            print("Massa in aardmassa's, afstand in")
            print("astronmische eenheden.")
            while True:
                mpi = float(input(f"\nMassa planeet nr. {i + 1}? "))
                if mpi < 1000:
                    break
                print("Een hemellichaam van deze afmetingen.")
                print("wordt een ster.")
            while True:
                rpi = float(input("Baanstraal? "))
                if rpi <= star.mass / 5:
                    print("Te dicht bij de zon. De planeet zal")
                    print("in stukken breken.")
                    continue
                if rpi >= 56 * star.mass:
                    print("Te ver weg. De planeet zal aan het")
                    print("stelsel ontsnappen.")
                    continue
                break
            for k in range(0, i):
                if 0.9 * rpi < rpl[k] < 1.1 * rpi:
                    print("Deze planeet is te dicht bij andere")
                    print("planeten om een stabiele baan te")
                    print("hebben.")
                    break
            else:
                a1 = mpi * math.sqrt(rpi)
                if a1 >= am:
                    print("Deze planeet heeft teveel massa om")
                    print("in het stelsel te passen.")
                    continue
                am = am - a1
                rpl.append(rpi)
                mp.append(mpi)
                break
    for i in range(0, np):
        f = False
        for k in range(0, np - (i + 1)):
            if rpl[k + 1] < rpl[k]:
                rpl[k], rpl[k + 1] = rpl[k + 1], rpl[k]
                mp[k], mp[k + 1] = mp[k + 1], mp[k]
                f = True
        if not f:
            break
    print("\n\nPlaneet nr.   massa   baanstraal\n")
    rm = math.sqrt(1 / 1.929)
    rx = math.sqrt(1 / 0.694)
    for i in range(0, np):
        print(f"  {i:2d}    {mp[i]:9.3f}   {rpl[i]:8.3f}  ", end='')
        if rm < rpl[i] < rx and 0.055 < mp[i] < 17.6:
            print("Leven?")
        else:
            print("")

    _ = input("\nDruk op Enter")
    return True


if __name__ == '__main__':
    title_screen()
    a = '0'
    while a != '4':
        star = None
        a = menu_screen()
        if a == '2':
            star = define_own_star()
        if a == '3':
            list_stars()
        if a == '1' or a == '3':
            star = select_known_star()
        if a != '4':
            if star is None:
                continue
            while True:
                if planet_data(star):
                    break
