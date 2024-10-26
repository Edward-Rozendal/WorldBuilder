"""
A modest program for designing stage new worlds.

The original was written in BASIC by Stephen Kimmel and published in the June 1983 issue of
[Creative Computing Magazine](https://archive.org/details/CreativeComputing198306/page/n263/mode/2up).

This version is based on the Dutch translation made by Steven Bolt and Carl Koppeschaar
and published in January 1984 in the monthly magazine [KIJK](https://www.kijkmagazine.nl/).
"""

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
    print("")
    print("** WERELD BOUWER **")
    print("")
    print("door Stephen Kimmel")
    print("een programma voor")
    print("de bouw van vreemde")
    print("nieuwe werelden....", end='')
    _ = input()


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
    print("")
    print("&& WERELD BOUWER &&")
    print("")
    print("tik het nr. van de gewenste operatie")
    print("")
    print("1) gebruik een bekende ster")
    print("2) gebruik een andere ster")
    print("3) druk een lijst van bekende sterren")
    print("4) stop")
    print("")
    return input("Uw keus: ")


def list_stars():
    clear_screen()
    print("Dit zijn de sterren op mijn lijstje:")
    print("")
    for i in range(18):
        print("  {:<38}{}".format(s2[i], s2[i + 18]))
    print("")


def select_known_star():
    s = input("Welke ster zal ik gebruiken? ")
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


def define_own_star():
    clear_screen()
    s = input("Hoe heet de ster? ")


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
