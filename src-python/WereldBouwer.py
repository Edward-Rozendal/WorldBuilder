"""
A modest program for designing stage new worlds.

The original was written in BASIC by Stephen Kimmel and published in the June 1983 issue of
[Creative Computing Magazine](https://archive.org/details/CreativeComputing198306/page/n263/mode/2up).

This version is based on the Dutch translation made by Steven Bolt and Carl Koppeschaar
and published in January 1984 in the monthly magazine [KIJK](https://www.kijkmagazine.nl/).
"""
import math
from os import system, name


def clear_screen():
    if name == 'nt':
        # for windows
        system('cls')
    else:
        # for mac and linux (here, os.name is 'posix')
        system('clear')


def title_screen():
    clear_screen()
    print("\n** WERELD BOUWER **\n")
    print("door Stephen Kimmel")
    print("een programma voor")
    print("de bouw van vreemde")
    print("nieuwe werelden....", end='')
    _ = input()


def cnv(z):
    """ Convert degrees fahrenheit to degrees celsius"""
    return ((z - 32) / 0.18 + 0.5) / 10


sc2 = ["o", "b", "a", "f", "g", "k", "m", "d"]
m2 = [100, 17, 3.2, 1.54, 1.02, 0.75, 0.38, 0.0]
c2 = ["blauw", "licht blauw", "wit", "licht geel", "geel", "oranje", "rood", "rood"]

s2 = ["sol", "alpha centauri a", "alpha centauri b", "epsilon eridani", "tau ceti",
      "70 ophiuchi a", "70 ophiuchi b", "eta cassiopeiae a", "eta cassiopeiae b",
      "sigma draconis", "36 ophiuchi a", "36 ophiuchi b", "hr-7703", "delta pavonis",
      "82 eridani", "beta hydri", "hr-8832", "sirius", "canopus", "vega", "arcturus",
      "rigel", "capella", "procyon", "achernar", "altair", "betelgeuze", "aldebaran",
      "spica", "antares", "pollux", "fomalhaut", "beta crucis", "deneb", "regulus",
      "barnard's star"]
ss2 = ["g2", "g4", "k1", "k2", "g8", "k1", "k5", "f9", "k6",
       "g9", "k2", "k1", "k2", "g7", "g5", "g1", "k3", "a1",
       "f0", "a0", "k2", "b8", "g8", "f5", "b5", "a7", "m2",
       "k5", "b1", "m1", "k0", "a3", "b0", "a2", "b7", "m5"]
sm_begin = [1.0, 1.08, 0.88, 0.80, 0.82, 0.9, 0.65, 0.94, 0.58,
            0.82, 0.77, 0.76, 0.76, 0.98, 0.91, 1.23, 0.74]
ls_end = [23.0, 130.0, 52.0, 100.0, 52000.0, 145.0, 7.6, 1000.0, 10.0, 8300.0,
          160.0, 760.0, 830.0, 33.0, 13.0, 8300.0, 52000.0, 160.0, 0.00044]
sm2 = []
ls2 = []


def init_data():
    sm2.extend(sm_begin)
    for i in range(len(ls_end)):
        sm2.append(ls_end[i] ** 0.285714)
    for i in range(len(sm_begin)):
        ls2.append(sm_begin[i] ** 3.5)
    ls2.extend(ls_end)


def menu_screen():
    clear_screen()
    print("\n&& WERELD BOUWER &&\n")
    print("tik het nr. van de gewenste operatie\n")
    print("1) gebruik een bekende ster")
    print("2) gebruik een andere ster")
    print("3) druk een lijst van bekende sterren")
    print("4) stop\n")
    return input("Uw keus: ")


def list_stars():
    clear_screen()
    print("Dit zijn de sterren op mijn lijstje:\n")
    for i in range(18):
        print(f"  {s2[i]:<38}{s2[i + 18]}")


def select_known_star():
    s = input("\nWelke ster zal ik gebruiken? ")
    sk = 0
    try:
        sk = s2.index(s)
    except ValueError:
        _ = input("Die ster is mij niet bekend.")
        return
    sc = int(ss2[sk][1]) / 10
    s1 = ss2[sk][0]
    ms = sm2[sk]
    l = ls2[sk]
    as1 = pow(ms, -2.5) * 10
    p = (1.25 - ms / pow(l, 0.285714)) / 0.005
    if (p / 100 * as1) > 10:
        p = 1000 / as1
    show_stellar_data(s, s1, sc, ms, l, as1, p)
    a = input("\nWilt u een andere ster? ")
    if len(a) > 0 and a[0].lower() in ('j', 'y'):
        return
    while True:
        if planet_data(s, s1, sc, ms, l, as1, p):
            break


def define_own_star():
    clear_screen()
    s = input("Hoe heet de ster? ")
    sc = 0
    ms = 0.0
    l = 0.0
    p = 0
    while True:
        s1 = input("\nWat is de spectraalklasse? ")
        if len(s1) == 0 or s1[0] in ('/', '?'):
            m = float(input("\nAbsolute magnitude ( zon=4.85 )? "))
            l = 2.512 ** (4.85 - m)
            ms = l ** 0.285714
            for i in range(1, len(m2) - 1):
                if m2[i] < ms:
                    j = i - 1
                    break
            else:
                print("\nMassa error.")
                continue
            s1 = sc2[i - 1]
            sc = int(((ms - m2[j]) / (m2[i] - m2[j]) * 10)) / 10
            break
        elif len(s1) == 2:
            try:
                sc = int(s1[1]) / 10
                s1 = s1[0].lower()
            except ValueError:
                print("\nDie klasse is mij onbekend.")
                continue
            j = 0
            for i in range(len(sc2) - 1):
                if s1 == sc2[i]:
                    j = i
                    break
            else:
                print("\nDie klasse is mij onbekend.")
                continue
            ms = m2[j] - sc * (m2[j] - m2[j + 1])
            break
        else:
            print("<letter><cijfer> verwacht")
            continue
    as1 = ms ** -2.5 * 10
    while True:
        print(f"\n{s} heeft een verwachte levensduur van ")
        print(f"{as1:.1f} miljard jaar ")
        p = float(input("\nWelk percentage (1-100) is voorbij? "))
        if p / 100 * as1 < 18:
            break
        print("\nHet universum is circa 18 miljard jaar oud.")
        a = input("\nWilt u een ander percentage? ")
        if len(a) == 0 or a[0].lower() not in ('j', 'y'):
            break
    ms = ms * (1.25 - 0.005 * p)
    l = ms ** 3.5
    show_stellar_data(s, s1, sc, ms, l, as1, p)
    a = input("\nWilt u een andere ster? ")
    if len(a) > 0 and a[0].lower() in ('j', 'y'):
        return
    while True:
        if planet_data(s, s1, sc, ms, l, as1, p):
            break


def show_stellar_data(s, s1, sc, ms, l, as1, p):
    j = sc2.index(s1)
    ts = 6000 * ms ** 0.35
    clear_screen()
    print("** STELLAR DATA **\n")
    print(f"De gekozen ster, {s} is een {s1}{int(sc * 10)} ster.")
    if sc > 0.75:
        print(f"Ze is {c2[j + 1]} van kleur,")
    elif sc < 0.25:
        print(f"Ze is {c2[j]} van kleur,")
    else:
        print(f"Ze heeft een kleur tussen {c2[j]} en {c2[j + 1]}")
    print(f"en haar massa is {ms + 0.005:.2f} zonmassa's.")
    print(f"Ze is {l:.2f} maal zo helder als de zon.")
    print(f"Haar verwachte levensduur is {as1:.2f} miljard jaar")
    print(f"waarvan {p:.0f}% of ongeveer {(as1 * p + 0.5) / 100:.2f}")
    print("miljard jaar zijn verstreken.")
    if p > 95:
        print(f"{s} ligt op haar sterfbed.")
    print(f"Ze heeft een oppervlaktetemperatuur van {ts:.0f} Kelvin.")
    if 2.5 < j + 1 + sc < 7:
        print("Ze heeft mogelijk een planetenstelsel.")
    else:
        print("Ze heeft waarschijnlijk geen planetenstelsel.")
    print(f"{s} zal sterven als een")
    if ms < 1.5:
        print("witte dwerg.")
    elif ms < 10:
        print("neutronster na een supernove-explosie.")
    else:
        print("zwart gat na een supernova-explosie.")


def planet_data(s, s1, sc, ms, l, as1, p):
    hm = 0
    p = p / 100
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
    rp = math.sqrt(l / (tp / 520) ** 4)
    if rp <= ms / 5:
        print("\nDeze planeet bevindt zich te dicht bij haar zon")
        print("om stabiel te zijn.")
        _ = input("Druk op Enter")
        return False
    pp = math.sqrt(rp ** 3 / ms)
    rm = math.sqrt(1 / 1.929)
    rx = math.sqrt(1 / 0.694)
    ds = ms ** 0.3333
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
            mn.append(float(input(f"\nMassa maan nr.{i + 1} (onze maan = 1)? ")))
            while True:
                tmp = float(input("\nBaanstraal (onze maan = 30)? "))
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
    h2 = 0.85 * d ** 4 / m * (ms * 333500 / (11759 * rp) ** 3 + h)
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
    print("\nDruk op Enter voor")
    _ = input("informatie over het manenstelsel.")

    if mcnt > 0:
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

    _ = input("Druk op Enter")
    return True


if __name__ == '__main__':
    title_screen()
    init_data()
    a = '0'
    while a != '4':
        a = menu_screen()
        if a == '2':
            define_own_star()
        if a == '3':
            list_stars()
        if a == '1' or a == '3':
            select_known_star()
