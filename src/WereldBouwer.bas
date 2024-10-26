5 SCREEN 12: CLS
10 FOR i=1 TO 700: COLOR (1): PSET (RND*640, RND*480): NEXT i
15 FOR i=1 TO 100: COLOR (2): PSET (RND*640, RND*480): NEXT i
20 FOR i=1 TO 100: COLOR (3): PSET (RND*640, RND*480): NEXT i
25 LOCATE 8, 30: PRINT "** WERELD BOUWER **"
30 LOCATE 10, 30: PRINT "door Stephen Kimmel"
35 LOCATE 12, 30: PRINT "een programma voor"
40 LOCATE 14, 30: PRINT "de bouw van vreemde"
45 LOCATE 16, 30: PRINT "nieuwe werelden...."

60 DIM sc$(8), m(8), c$(8), s$(36), ls(36), ss$(36), sm(36), mp(15), r(15)
70 FOR i=1 TO 8: READ sc$(i), m(i), c$(i): NEXT i
80 FOR i=1 TO 17: READ s$(i), ss$(i), sm(i): ls(i)=sm(i)^3.5: NEXT i
90 FOR i=18 TO 36: READ s$(i), ss$(i), ls(i): sm(i)=ls(i)^.285714: NEXT i
100 DATA o,100,blauw,b,17,licht blauw,a,3.2,wit,f,1.54,licht geel
110 DATA g,1.02,geel,k,.75,oranje,m,.38,rood,d,0.,rood
120 DATA sol,g2,1.0,alpha centauri a,g4,1.08,alpha centauri b,k1,.88
130 DATA epsilon eridani,k2,.80,tau ceti,g8,.82
140 DATA 70 ophiuchi a,k1,.9,70 ophiuchi b,k5,.65
150 DATA eta cassiopeiae a,f9,.94,eta cassiopeiae b,k6,.58
160 DATA sigma draconis,g9,.82,36 ophiuchi a,k2,.77
170 DATA 36 ophiuchi b,k1,.76,hr-7703,k2,.76
180 DATA delta pavonis,g7,.98,82 eridani,g5,.91
190 DATA beta hydri,g1,1.23,hr-8832,k3,.74
200 DATA sirius,a1,23,canopus,f0,130,vega,a0,52,arcturus,k2,100
210 DATA rigel,b8,52000,capella,g8,145,procyon,f5,7.6
220 DATA achernar,b5,1000,altair,a7,10,betelgeuze,m2,8300
230 DATA aldebaran,k5,160,spica,b1,760,antares,m1,830
240 DATA pollux,k0,33,fomalhaut,a3,13,beta crucis,b0,8300
250 DATA deneb,a2,52000,regulus,b7,160,barnards star,m5,.00044
255 IF INKEY$ = "" THEN GOTO 255 ELSE SCREEN 0

260 CLS: LOCATE 5, 30: PRINT "&& WERELD BOUWER &&"
270 LOCATE 7, 10: PRINT "tik het nr. van de gewenste operatie"
280 LOCATE 9, 10: PRINT "1) gebruik een bekende ster"
290 LOCATE 11, 10: PRINT "2) gebruik een andere ster"
300 LOCATE 13, 10: PRINT "3) druk een lijst van bekende sterren"
310 LOCATE 15, 10: PRINT "4) stop"
320 LOCATE 18, 10: INPUT "Uw keus ";a
330 IF a<1 OR a>4 THEN GOTO 260
340 ON a GOTO 410,550,370,350
350 LOCATE 21, 10: INPUT "weet u zeker dat u wilt stoppen ";a$
360 IF LEFT$(a$, 1)="j" OR LEFT$(a$, 1)="J" THEN END
365 GOTO 260
370 CLS: LOCATE 1, 5: PRINT "Dit zijn de sterren op mijn lijstje:"
380 FOR i=1 TO 18
    390 LOCATE i+2, 5: PRINT s$(i): LOCATE i+2, 40: PRINT s$(i+18)
400 NEXT i
410 LOCATE 22, 5: INPUT "Welke ster zal ik gebruiken";s$
420 IF LEFT$(s$, 1)="g" OR LEFT$(s$, 1)="G" THEN GOTO 260
430 FOR i=1 TO 36
    440 IF s$=s$(i) THEN sk=i: GOTO 470
450 NEXT i
460 LOCATE 24, 5: PRINT "Die ster is mij niet bekend.";
465 IF INKEY$ = "" THEN GOTO 465 ELSE GOTO 260
470 sc=VAL(RIGHT$(ss$(sk), 1))/10
480 s1$=LEFT$(ss$(sk), 1)
490 FOR i=1 TO 7: IF s1$=sc$(i) THEN j=i: GOTO 510
500 NEXT i
510 ms=sm(sk): l=ls(sk): as1=(ms^-2.5)*10
520 p=(1.25-ms/(l^.285714))/.005
530 IF p/100*as1>10 THEN p=1000/as1
540 GOTO 740

550 CLS: LOCATE 3, 5: INPUT "Hoe heet de ster ";s$
560 PRINT: PRINT TAB(5);: INPUT "Wat is de spectraalklasse ";s1$
570 IF s1$ <> "/" AND s1$ <> "?" THEN GOTO 640
580 PRINT: PRINT TAB(5);: INPUT "Absolute magnitude (zon = 4.85) ";m
590 l=2.512^(4.85-m): ms=l^.285714
600 FOR i=1 TO 7: IF m(i)<ms THEN j=i-1: GOTO 620
610 NEXT i
620 s1$=sc$(i-1): sc=INT((ms-m(j))/(m(i)-m(j))*10)/10
630 GOTO 680
640 sc=VAL(RIGHT$(s1$, 1))/10: s1$=LEFT$(s1$, 1)
650 FOR i=1 TO 7: IF s1$=sc$(i) THEN j=i: GOTO 670
660 NEXT i: PRINT: PRINT TAB(5);"Die klasse is mij onbekend.": GOTO 560
670 ms=m(j)-sc*(m(j)-m(j+1))
680 as1=(ms^-2.5)*10
685 z=as1: GOSUB 2650
690 PRINT: PRINT TAB(5);s$;" heeft een verwachte levensduur van "
695 PRINT TAB(5);z;" miljard jaar."
700 PRINT: PRINT TAB(5);: INPUT "Welk percentage (1-100) is voorbij ";p
710 IF p/100*as1<18 THEN GOTO 720
715 PRINT: PRINT TAB(5);"Het universum is circa 18 miljard jaar oud."
717 PRINT: PRINT TAB(5);: INPUT "Wilt u een ander percentage ";a$
718 IF LEFT$(a$, 1)<>"n" AND LEFT$(a$, 1)<>"N" THEN GOTO 690
720 ms=ms*(1.25-.005*p)
730 l=ms^3.5

740 ts=6000*ms^.35
750 ds=ms^.3333
760 CLS: LOCATE 2, 31: PRINT "** STELLAR DATA **": PRINT: PRINT
770 PRINT TAB(10);"De gekozen ster, ";s$: PRINT TAB(10);"is een ";s1$;sc*10;" ster."
780 IF sc>.75 THEN PRINT TAB(10);"Ze is ";c$(j+1);" van kleur,": GOTO 805
790 IF sc<.25 THEN PRINT TAB(10);"Ze is ";c$(j);" van kleur,": GOTO 805
800 PRINT TAB(10);"Ze heeft een kleur tussen ";c$(j);" en ";c$(j+1);","
805 z=ms: GOSUB 2650
810 PRINT TAB(10);"en haar massa is ";z;" zonsmassa's."
815 z=l: GOSUB 2650
820 PRINT TAB(10);"Ze is ";z;" maal zo helder als de zon."
825 z=as1: GOSUB 2650
830 PRINT TAB(10);"Haar verwachte levensduur is": PRINT TAB(10);z;" miljard jaar,"
835 z=p: GOSUB 2650
840 PRINT TAB(10);"waarvan ";z;"%";" of ongeveer "
845 PRINT TAB(10);INT(as1*p+.5)/100;" miljard jaar zijn verstreken."
850 IF p>95 THEN PRINT TAB(10);s$;" ligt op haar sterfbed."
855 z=ts: GOSUB 2650
860 PRINT TAB(10);"Ze heeft een oppervlaktetemperatuur": PRINT TAB(10);"van";z;"graden Kelvin."
870 IF j+sc>2.5 AND j+sc<7 THEN GOTO 880
875 PRINT TAB(10);"Ze heeft waarschijnlijk geen planetenstelsel.": GOTO 890
880 PRINT TAB(10);"Ze heeft mogelijk een planetenstelsel."
890 PRINT TAB(10);s$;" zal sterven als een"
900 IF ms<1.5 THEN PRINT TAB(10);"witte dwerg.": GOTO 940
920 IF ms<10 THEN PRINT TAB(10);"neutronster na een supernova-explosie.": GOTO 940
930 PRINT TAB(10);"zwart gat na een supernova-explosie."
940 PRINT: PRINT TAB(10);: INPUT "Wilt u een andere ster";a$
950 IF LEFT$(a$, 1)="j" OR LEFT$(a$, 1) = "J" THEN GOTO 260

955 hm=0
960 p=p/100
970 CLS: LOCATE 2, 29: PRINT "** PLANEET-GEGEVENS **"
980 LOCATE 5, 10: PRINT "De aarde heeft een gemiddelde oppervlakte"
985 PRINT TAB(10);"temperatuur van 16 C."
990 PRINT TAB(10);: INPUT "Welke temperatuur wenst u";tp: tp=1.8*tp+492
1000 PRINT: PRINT TAB(10);"Gewenste zwaartekracht aan de oppervlakte"
1005 PRINT TAB(10);"(aarde=1) ";: INPUT g
1010 IF g<=0 THEN PRINT TAB(10);"Enige zwaartekracht is noodzakelijk.": GOTO 1000
1020 rp=SQR(l/(tp/520)^4)
1030 IF rp>ms/5 THEN GOTO 1040
1035 PRINT TAB(10);"Deze planeet bevindt zich te dicht bij"
1037 PRINT TAB(10);"haar zon om stabiel te kunnen zijn.": GOTO 970
1040 pp=SQR(rp^3/ms)
1050 is1=l/rp^2
1060 rm=SQR(1/1.929)
1070 rx=SQR(1/.694)
1080 sa=ds/rp
1090 PRINT: PRINT TAB(10);"Hoe groot moet de planeet zijn"
1095 PRINT TAB(10);"tot de aarde ";: INPUT d
1100 m=g*d^2
1110 IF m>.055 THEN 1120
1115 PRINT TAB(10);"^Deze planeet zal geen zuurstof atmosfeer vasthouden."
1120 IF m<17.6 THEN 1130
1125 PRINT TAB(10);"Deze planeet zal haar waterstof-"
1127 PRINT TAB(10);"atmosfeer niet kwijt raken."
1130 PRINT: PRINT TAB(10);"De baan van de aarde heeft een excentriciteit van"
1140 PRINT TAB(10);".01672 Gewenste excentriciteit (<1) ";: INPUT ec
1150 IF ec>1 THEN GOTO 1140
1160 ca=(1-ec)*rp: fa=(1+ec)*rp
1170 PRINT: PRINT TAB(10);"Wat is de hoek van de rotatie-as": PRINT TAB(10);"(aarde = 23.5 graden)"
1175 PRINT TAB(10);: INPUT t1
1180 IF t1<0 OR t1>90 THEN GOTO 1170

1190 PRINT: PRINT TAB(10);"Hoeveel manen wenst u ";: INPUT mn
1200 IF mn>10 THEN PRINT TAB(10);"Voor het gemak beperken we dat tot 10.": mn=10
1205 DIM mn(mn),mr(mn)
1210 mm=1000: h=0: r=56*g
1220 IF mn<=0 THEN GOTO 1320
1230 FOR i=1 TO mn
    1240 PRINT TAB(10);"Massa maan nr.";i;" (onze maan = 1) ";: INPUT mn(i)
    1250 PRINT TAB(10);"Baanstraal (onze maan = 30) ";: INPUT mr(i)
    1260 IF mr(i)<3*g THEN PRINT TAB(10);"Te dichtbij; ze zal in stukken breken.": GOTO 1250
    1270 IF mr(i)>56*g THEN PRINT TAB(10);"Te ver weg; ze ontsnapt.": GOTO 1250
    1280 mp(i)=SQR(mr(i)^3/m)*4
    1290 IF mr(i)<r THEN mm=mp(i): r=mr(i)
    1300 h=mn(i)*.01235/(mr(i)^3)+h
1310 NEXT i
1320 h2=.85*d^4/m*(ms*333500/(11759*rp)^3+h)
1330 da=1759260!*h2*14+10
1340 IF da>mm THEN da=mm

1350 CLS: LOCATE 2, 29: PRINT "** PLANEET-GEGEVENS **"
1353 z=da: GOSUB 2650
1355 LOCATE 5, 10: PRINT "Een dag duurt op deze planeet": PRINT TAB(10);"ongeveer ";z;" uur."
1360 PRINT TAB(10);"Een jaar duurt "; INT(87660/da*pp+.5)/10;" dagen."
1365 PRINT TAB(10);"De hoek van de rotatie-as heeft de "
1367 PRINT TAB(10);"volgende invloeden op het klimaat:"
1370 hi=(1+.025*da/24)*tp-460: lo=(1-.025*da/24)*tp-460
1380 IF lo<-460 THEN lo=-460
1385 z=hi: GOSUB 2700
1390 PRINT TAB(10);"De maximumtemperatuur is vandaag": PRINT TAB(10);z;" graden C."
1395 z=lo: GOSUB 2700
1400 PRINT TAB(10);"Vannacht zal de temperatuur dalen": PRINT TAB(10);"tot ";z;" graden C."
1410 sh=hi+1.9*t1*(1+ec)^2: ll=lo-1.9*t1/(1+ec)^2
1420 IF ll<-460 THEN ll=-460
1425 z=sh: GOSUB 2700
1430 PRINT TAB(10);"'s Zomers kan de temperatuur stijgen": PRINT TAB(10);"tot ";z;" graden C."
1435 z=ll: GOSUB 2700
1440 PRINT TAB(10);"'s Winters verwachten we een minium": PRINT TAB(10);"van ";z;" graden C."
1450 IF sh>32 AND ll<175 THEN GOTO 1455
1453 PRINT TAB(10);"Er zijn perioden waarin geen vloeibaar water kan bestaan."
1455 PRINT: PRINT TAB(10);"Tik een willekeurige toets voor"
1457 PRINT TAB(10);"informatie over het manenstelsel."
1459 IF INKEY$ = "" THEN GOTO 1459
1460 IF mn<=0 THEN GOTO 1600
1470 IF mn=1 THEN GOTO 1570
1480 FOR i=1 TO mn: f=O: FOR k=1 TO mn-i
        1490 IF mr(k+1)>=mr(k) THEN 1540
        1500 t=mr(k): mr(k)=mr(k+1): mr(k+1)=t
        1510 t=mn(k): mn(k)=mn(k+1): mn(k+l)=t
        1520 t=mp(k): mp(k)=mp(k+1): mp(k+1)=t
        1530 f=1
    1540 NEXT k
    1550 IF f=0 THEN 1570
1560 NEXT i

1570 CLS: LOCATE 2, 29: PRINT "** HET MANENSTELSEL **"
1580 LOCATE 5, 10: PRINT "baanstraal  massa   periode": PRINT
1585 FOR i=1 TO mn: z=mp(i)/da: GOSUB 2650
1590 PRINT TAB(12);mr(i);TAB(23);mn(i);TAB(31);z;" dagen": NEXT i
1600 PRINT: PRINT TAB(10);"Wilt u een ander stelsel ";: INPUT a$
1610 IF LEFT$(a$, 1)="j" OR LEFT$(a$, 1)="J" THEN GOTO 1190

1620 CLS: LOCATE 2, 29: PRINT "** PLANEET GEGEVENS **"
1630 PRINT " Deze planeet heeft een gemiddelde"
1635 z=tp-460: GOSUB 2700
1640 PRINT " oppervlakte-temperatuur van ";z: PRINT " graden C.";
1645 PRINT " Dit betekent een baanstraal"
1647 z=rp: GOSUB 2650
1650 PRINT " van ";z;" astronomische eenheden"
1655 PRINT " (";z*150;" miljoen km.)."
1660 z=ca: GOSUB 2650: PRINT " Perihelium = ";z;"ae": PRINT " Aphelium = ";
1665 z=fa: GOSUB 2650: PRINT z;"ae."
1670 z=pp: GOSUB 2650: PRINT " Een jaar is ";z;" aardejaren lang."
1680 PRINT " ";s$;" lijkt";
1690 IF sa>1.5 OR sa<.75 THEN PRINT " veel"
1700 IF sa>1 THEN PRINT " groter";: GOTO 1710
1705 PRINT " kleiner";
1710 PRINT " dan onze zon."
1720 IF g<.95 OR g>1.05 THEN GOTO 1730
1725 PRINT " De zwaartekracht is vrijwel gelijk": PRINT " aan die van de aarde."
1727 GOTO 1800
1730 PRINT " Aangezien de zwaartekracht";: IF g<1 THEN GOTO 1760
1740 PRINT " groter is": PRINT " dan op aarde verwachten we"
1750 PRINT " een dichtere atmosfeer. De tektonische"
1752 PRINT " werking is groter maar er is ook"
1754 PRINT " meer weerstand. We verwachten daarom"
1756 PRINT " meer continenten en kleinere bergen;"
1758 PRINT " Aardbevingen komen vaker voor en zijn": PRINT " heviger.": GOTO 1780
1760 PRINT " kleiner is": PRINT " dan op aarde verwachten we"
1770 PRINT " een dunnere atmosfeer. Er is minder"
1772 PRINT " tektonische werking en ook de"
1774 PRINT " weerstand is kleiner. We verwachten"
1776 PRINT " daarom minder bergen, maar ze kunnen": PRINT " veel hoger worden."
1778 PRINT " Aardbevingen, als ze al voorkomen,"
1779 PRINT " zullen minder hevig zijn."
1780 PRINT " Een zwaartekracht van";g;"g betekent"
1785 PRINT " dat iemand van 80 kilo op deze"
1787 PRINT " planeet ";g*80;"kilo zou wegen."
1800 INPUT " Wilt u een andere zwaartekracht";a$
1810 IF LEFT$(a$, 1)="j" OR LEFT$(a$, 1)="J" THEN GOTO 1000
1810 ifleft$(a$,1)="j"then1000

1820 print"S^         ** LEVEN? **"
1830 ifm<.055orm>17.6thenprint"^Vanwege de slechte atmosfeer":goto2080
1840 ifrp<rmorrp>rxthenprint"^Vanwege de afstand tot de zon":goto2080
1850 ifsh<32orll>175thenprint"^Aangezien er nooit vloeibaar water is": goto2080
1860 ifas*p>1.5then1870
1865 print"^De planeet is te jong; er kan nog"
1867 print" geen leven zijn ontstaan.":goto2090
1870 ifp<.95then1880
1875 print"^Aangezien ";s$;" op haar":print" sterfbed ligt":goto2080
1880 print"^Mogelijk zijn er ";
1890 ifas*p<2*gthenprint"bacterien en":print" blauwgroene algen.":goto2060
1900 ifas*p<3*gthenprint"eencelligen met":print" een kern.":goto2060
1910 ifas*p<4*gthenprint"eenvoudige":print" meercelligen.":goto2060
1920 ifas*p>4.4*gthen1930
1925 print"gewervelde":print" waterdieren en planten op het land.":goto2060
1930 print"grote op het land":print" levende dieren en misschien"
1935 print" intelligente wezens."
1940 ifg<.95then1990
1950 ifg<1.05then2030
1960 print" Grotere zwaartekracht betekent een"
1961 print" dichtere atmosfeer die grote vogels"
1962 print" kan dragen. Maar zelfs een kleine val"
1963 print" is dodelijk, zodat hoge reactiesnel-"
1964 print" heden noodzakelijk zijn. In het"
1965 print" algemeen zullen levensvormen korter"
1966 print" en steviger zijn dan op aarde."
1970 ifg>1.2thenprint" Er zijn geen tweebenige wezens":print" zoals wij."
1980 print" De dikke atmosfeer verbetert de"
1981 print" geluidsoverdracht; daarom zullen"
1982 print" dieren meer op hun gehoor vertrouwen.":goto2030
1990 print" Kleinere zwaartekracht betekent een"
1991 print" dunnere atmosfeer. Vogels, als ze"
1992 print" al voorkomen, hebben grote vleugels."
1993 print" Alle levensvormen zullen hoger en"
1994 print" slanker gebouwd zijn dan die op aarde."
2000 print" Tweebenige wezens kunnen zeker":print" voorkomen."
2010 print" De dunne atmosfeer bemoeilijkt"
2011 print" geluidsoverdracht, zodat de dieren"
2012 print" grote of helemaal geen oren zullen"
2013 print" hebben. Hun longen moeten groter zijn."
2020 iftp<75then2030
2025 print" Het leven moet zich op een of andere"
2026 print" manier beschermen tegen het zonlicht."
2030 ifsa>.75then2040
2032 print" Vanwege de kleine zon zullen de"
2034 print" dieren grote ogen hebben of op"
2036 print" andere zintuigen vertrouwen."
2040 ifsa<1.5then2050
2042 print" Tenzij de atmosfeer veel licht"
2044 print" tegenhoudt, zullen de dieren"
2046 print" kleine ogen hebben."
2050 ifhi-lo<50then2060
2052 print" Vanwege de grote temperatuurvariaties"
2054 print" zal het leven zich vooral ondergronds"
2056 print" en onder water bevinden."
2060 if(tp-460)<32or(tp-460)>86org>1.5org<.68orm<.4orm>2.35thenhm=0:goto2090
2065 ifda>96orsh>120orll<-30orhi>110orlo<-10thenhm=O:goto2090
2070 hm=1:goto2090
2079 print"bewoonbaar vinden."
2080 print" zal op deze planeet waarschijnlijk":print" geen leven zijn."
2090 print" Mensen zullen deze wereld"
2095 print" waarschijnlijk ";:ifhm=0thenprint"on";
2100 print"bewoonbaar vinden."
2110 input"^Wilt u een andere planeet";a$
2120 ifleft$(a$,1)="j"then970
2130 print"S^       ** ANDERE PLANETEN **"
2140 print"^Hoeveel planeten moet het stelsel"
2145 print" van ";s$;:input" bevatten";np
2150 ifnp>15thennp=15:print"^We moeten dat beperken tot vijftien."
2160 ifnp<=1then2600
2170 am=1180/sqr(ms)-m*sqr(rp)
2180 r(1)=rp:mp(1)=m
2190 fori=2tonp
2200 print"S"
2210 print"^Ons eigen zonnestelsel ziet er zo uit:"
2220 print"^  planeet    massa      baanstraal"
2230 print"^  Mercurius    0.055     0.387"
2240 print"   Venus        0.815     0.723"
2250 print"   Aarde        1.0       1.0"
2260 print"   Mars         0.108     1.524"
2270 print"   Jupiter    317.9       5.203"
2280 print"   Saturnus    95.2       9.539"
2290 print"   Uranus      14.6      19.18"
2300 print"   Neptunus    17.2      30.06"
2310 print"   Pluto         .1      39.44"
2315 print"^Massa in aardmassa's, afstand in":print" astronomische eenheden."
2320 print"^Massa planeet nr.";i;:inputmp(i)
2330 ifmp(i)<1000then2340
2335 print"^Een hemellichaam van deze afmetingen"
2337 print" Wordt een ster.":goto2320
2340 input"^Baan straal";r(i)
2350 ifr(i)>ms/5then2360
2355 print"^Te dicht bij de zon. De planeet zal"
2357 print" in stukken breken.":goto2340
2360 ifr(i)<56*msthen2370
2365 print"^Te ver weg. De planeet zal aan het"
2367 print" stelsel ontsnappen.":goto2340
2370 fork=1toi-1:ifr(k)>.9*r(i)andr(k)<1.1*r(i)then2430
2380 nextk
2390 a1=mp(i)*sqr(r(i))
2400 ifa1<amthen2410
2405 print"^Deze planeet heeft teveel massa om"
2407 print" In het stelsel te passen.":goto2210
2410 am=am-a1
2420 nexti:goto2450
2430 print"^Deze planeet is te dicht bij andere"
2435 print" planeten om een stabiele baan te":print" hebben."
2440 goto2210
2450 fori=1tonp:f=0:fork=1tonp-i
2460 ifr(k+1)>=r(k)then2500
2470 t=r(k):r(k)=r(k+1):r(k+1)=t
2480 t=mp(k):mp(k)=mp(k+1):mp(k+1)=t
2490 f=1
2500 nextk
2510 iff=0then2530
2520 nexti
2530 print"^planeet nr.  massa  baanstraal"
2540 fori=1tonp
2550 printi,mp(i),r(i);
2560 ifr(i)>rmandr(i)<rxandmp(i)>.055andmp(i)<17.6thenprint" leven?"
2565 print" "
2570 nexti
2580 input"^Wilt u een ander stelsel proberen";a$
2590 ifleft$(a$,1)="j"then2130
2600 input"^Wilt u een andere ster proberen";a$
2610 ifleft$(a$,1)="j"then260
2620 end
2650 z=int(z*100+.5)/100:return
2700 z=int((z-32)/.18+.5)/10:return
