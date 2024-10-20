5 print"S": fori=1to40:poke33792+rnd(1)*60*i,42:nexti
10 y=34038:forii=1to13
15 fori=yto(y+23):pokei,32:nexti
20 y=y+40:nextii
25 print"^        ** WERELD BOUWER **"
30 print"^        door Stephen Kimmel"
35 print"^        een programma voor"
40 print"^        de bouw van vreemde"
45 print"^        nieuwe werelden...."
60 dimsc$(8),m(8),c$(8),s$(36),ls(36),ss$(36),sm(36),mp(15),r(15)
70 fori=1to8:readsc$(i),m(i),c$(i):nexti
80 fori=1to17:reads$(i),ss$(i),sm(i):ls(i)=sm(i)^3.5:nexti
90 fori=18to36:reads$(i),ss$(i),ls(i):sm(i)=ls(i)^.285714:nexti
100 datao,100,blauw,b,17,licht blauw,a,3.2,wit,f,1.54,licht geel
110 datag,1.02,geel,k,.75,oranje,m,.38,rood,d,0.,rood
120 datasol,g2,1.0,alpha centauri a,g4,1.08,alpha centauri b,k1,.88
130 dataepsilon eridani,k2,.80,tau ceti,g8,.82
140 data70 ophiuchi a,k1,.9,70 ophiuchi b,k5,.65
150 dataeta cassiopeiae a,f9,.94,eta cassiopeiae b,k6,.58
160 datasigma draconis,g9,.82,36 ophiuchi a,k2,.77
170 data36 ophiuchi b,k1,.76,hr-7703,k2,.76
180 datadelta pavonis,g7,.98,82 eridani,g5,.91
190 databeta hydri,g1,1.23,hr-8832,k3,.74
200 datasirius,a1,23,canopus,f0,130,vega,a0,52,arcturus,k2,100
210 datarigel,b8,52000,capella,g8,145,procyon,f5,7.6
220 dataachernar,b5,1000,altair,a7,10,betelgeuze,m2,8300
230 dataaldebaran,k5,160,spica,b1,760,antares,m1,830
240 datapollux,k0,33,fomalhaut,a3,13,beta crucis,b0,8300
250 datadeneb,a2,52000,regulus,b7,160,barnards star,m5,.00044
260 fori=1to50:a$="wait":nexti:print"S^        && WERELD BOUWER &&"
270 print"^tik het nr. van de gewenste operatie"
280 print"^1) gebruik een bekende ster"
290 print"^2) gebruik een andere ster"
300 print"^3) druk een lijst van bekende sterren"
310 print"^4) stop"
320 input"^uw keus";a
330 ifa<1ora>4goto260
340 onagoto410,550,370,350
350 input"^weet u zeker dat u wilt stoppen";a$
360 ifleft$(a$,1)="j"thenend
365 goto260
370 print"S^Dit zijn de sterren op mijn lijst:"
380 fori=1to18:iflen(a$(i))<10thenprint" ";s$(i)+"         ",s$(i+18):goto400
390 print" ";s$(i) ,s$(i+18)
400 nexti
410 input"^welke ster zal ik gebruiken";s$
420 ifleft$(s$,1)="g"then260
430 fori=1to36
440 ifs$=s$(i)thensk=i:goto470
450 nexti
460 print"S^Die ster is mij niet bekend.":goto260
470 sc=val(right$(ss$(sk),1))/10
480 s1$=left$(ss$(sk),1)
490 fori=1to7:ifs1$=sc$(i)thenj=i:goto510
500 nexti
510 ms=sm(sk):l=ls(sk):as=(ms^-2.5)*10
520 p=(1.25-ms/(l^.285714))/.005
530 ifp/100*as>10thenp=1000/as
540 goto740
550 input"^Hoe heet de ster";s$
560 input"^Wat is de spectraalklasse";s1$
570 ifs1$<>"/"goto640
580 input"Absolute magnitude (zon = 4.85)";m
590 l=2.512^(4.85-m):ms=l^.285714
600 fori=1to7:ifm(i)<msthenj=i-1:goto620
610 nexti
620 s1$=sc$(i-1):sc=int((ms-m(j))/(m(i)-m(j))*10)/10
630 goto680
640 sc=val(right$(s1$,1))/10:s1$=left$(s1$,1)
650 fori=1to7:ifs1$=sc$(i)thenj=i:goto670
660 nexti:print"^Die klasse is mij onbekend.":goto560
670 ms=m(j)-sc*(m(j)-m(j+1))
680 as=(ms^-2.5)*10
685 z=as:gosub2650
690 print"^";s$;" heeft een verwachte":print"^Levensduur van ";z;" miljard";
695 print" jaar."
700 input"^Welk percentage (1-100) is voorbij";p
710 ifp/100*as<18then720
715 print"^Het universum is circa 18 miljard jaar":print"^oud. ";
717 input"Wilt u een ander percentage";a$:ifleft$(a$,1)sg"n"then690
720 ms=ms*(1.25-.005*p)
730 l=ms^3.5
740 ts=6000*ms^.35
750 ds=ms^.3333
760 print"S^       ** STELLAR DATA **"
770 print"^De gekozen ster, ";s$:print" is een ";s1$;sc*10;" ster."
780 ifsc>.75thenprint" Ze is ";c$(j+1);" van kleur,":goto805
790 ifsc<.25thenprint" Ze is ";c$(j);" van kleur,":goto805
800 print" Ze heeft een kleur tussen":print" ";c$(j);" en ";c$(j+1);","
805 z=ms:gosub2650
810 print" en haar massa is ";z;" zonsmassa's."
815 z=l:gosub2650
820 print" Ze is ";z;" maal zo helder":print" als de zon."
825 z=as:gosub2650
830 print" Haar verwachte levensduur is ":printz;" miljard jaar,"
835 z=p:gosub2650
840 print" waarvan ";z;"%";" of ongeveer"
845 printint(as*p+.5)/100;" miljard jaar zijn verstreken."
850 ifp>95thenprint" ";s$;" ligt op haar sterfbed."
855 z=ts: gosub2650
860 print" Ze heeft een oppervlaktetemperatuur"
865 print" van ";z;" graden Kelvin."
870 ifj+sc>2.5andj+sc<7then880
875 print" Ze heeft waarschijnlijk geen":print" planetenstelsel.":goto890
880 print" Ze heeft mogelijk een planetenstelsel."
890 print" ";s$;" zal sterven als een"
900 ifms<1.5thenprint" witte dwerg.":goto940
920 ifms<10thenprint" neutronster na een supernova-explosie.":goto940
930 print" zwart gat na een supernova-explosie."
940 input"^Wilt u een andere ster";a$
950 ifleft$(a$,1)="j"then260
955 Hm=0
960 p=p/100
970 print"S^      ** PLANEET-GEGEVENS **"
980 print"^De aarde heeft een gemiddelde"
985 print"^oppervlakte-temperatuur van 16 C."
990 input"^Welke temperatuur wenst u";tp:tp=1.8*tp+492
1000 print"^Gewenste zwaartekracht aan de":input"^oppervlakte (aarde = 1)";g
1010 ifg=0thenprint"^Enige zwaartekracht is noodzakelijk.":goto1000
1020 rp=sqr(l/(tp/520)^4)
1030 if rp>ms/5then1040
1035 print" Deze planeet bevindt zich te dicht bij"
1037 print" haar zon om stabiel te kunnen zijn.":goto970
1040 pp=sqr(rp^3/ms)
1050 is=l/rp^2
1060 rm=sqr(1/1.929)
1070 rx=sqr(1/.694)
1080 sa=ds/rp
1090 print"^Hoe groot moet de planeet zijn"
1095 input"^in verhouding tot de aarde";d
1100 m=g*d^2
1110 ifm>.055then1120
1115 print"^Deze planeet zal geen zuurstof atmosfeer":print" vasthouden."
1120 ifm<17.6then1130
1125 print"Deze planeet zal haar waterstof-"
1127 print" atmosfeer niet kwijt raken."
1130 print"^De baan van de aarde heeft een":print"^excentriciteit van .01672"
1140 input"^Gewenste excentriciteit ( <1)";ec
1150 ifec>1then1140
1160 ca=(1-ec)*rp:fa=(1+ec)*rp
1170 print"^Wat is de hoek van de rotatite-as"
1175 input"^(aarde = 23.5 graden)";t1
1180 ift1<0ort1>90then1170
1190 input"^Hoeveel manen wenst u";mn
1200 ifmn>10thenprint"^Voor het gemak beperken we dat tot 10.":mn=10
1205 dim mn(mn),mr(mn)
1210 mm=1000:h=0:r=56*g
1220 ifmn<=0then1320
1230 fori=1tomn
1240 print"^Massa maan nr.";i;" (onze maan = l)";:inputmn(i)
1250 input"^Baanstraal (onze maan = 30)";mr(i)
1260 ifmr(i)<3*gthenprint"^Te dichtbij; ze zal in stukken breken.":goto1250
1270 ifmr(i)>56*gthenprint"^Te ver weg; ze ontsnapt.":goto1250
1280 mp(i)=sqr(mr(i)^3/m)*4
1290 ifmr(i)<rthenmm=mp(i):r=mr(i)
1300 h=mn(i)*.01235/(mr(i)^3)+h
1310 nexti
1320 h2=.85*d^4/m*(ms*333500/(11759*rp)^3+h)
1330 da=1.75926e+06*h2*14+10
1340 ifda>mmthenda=mm
1350 print"S^       ** PLANEET-GEGEVENS **"
1353 z=da:gosub2650
1355 print"^Een dag duurt op deze planeet":print" ongeveer ";z;" uur."
1360 print" Een jaar duurt ";int(87660/da*pp+.5)/10;" dagen."
1365 print" De hoek van de rotatie-as heeft de"
1367 print" volgende invloeden op het klimaat:"
1370 hi=(1+.025*da/24)*tp-460:lo=(1-.025*da/24)*tp-460
1380 iflo<-460thenlo=-460
1385 z=hi:gosub2700
1390 print" De maximum temperatuur is vandaag":printz;" graden C."
1395 z=lo:gosub2700
1400 print" Vannacht zal de temperatuur dalen":print" tot";z;" graden C."
1410 sh=hi+1.9*t1*(1+ec)^2:ll=lo-1.9*t1/(1+ec)^2
1420 ifll<-460thenll=-460
1425 z=sh:gosub2700
1430 print" 's Zomers kan de temperatuur stijgen":print" tot ";z;" graden C."
1435 z=ll:gosub2700
1440 print" 's Winters verwachten we een minimum":print" van ";z;" graden C."
1450 ifsh>32andll<175then1455
1453 print" Er zijn perioden waarin geen":print" vloeibaar water kan bestaan."
1455 print"^Tik een willekeurige toets voor"
1457 print" informatie over het manenstelsel."
1459 geta$:ifa$=""then1459
1460 ifmn<=0then1600
1470 ifmn=1then1570
1480 fori=1tomn:f=O:fork=1tomn-i
1490 ifmr(k+1)>=mr(k)then1540
1500 t=mr(k):mr(k)=mr(k+1):mr(k+1)=t
1510 t=mn(k):mn(k)=mn(k+1):mn(k+l)=t
1520 t=mp(k):mp(k)=mp(k+1):mp(k+1)=t
1530 f=1
1540 nextk
1550 iff=0then1570
1560 nexti
1570 print"S^      ** HET MANENSTELSEL **"
1580 print"^baanstraal  massa   periode"
1585 fori=1tomn:z=mp(i)/da:gosub2650
1590 printmr(i),"  ";mn(i),z;"dagen":nexti
1600 input"^Wilt u een ander stelsel";a$
1610 ifleft$(a$,l)="j"then1190
1620 print"S^       ** PLANEET GEGEVENS **"
1630 print"^Deze planeet heeft een gemiddelde"
1635 z=tp-460:gosub2700
1640 print" oppervlakte-temperatuur van ";z:print" graden C.";
1645 print" Dit betekent een baanstraal"
1647 z=rp:gosub2650
1650 print" van ";z;" astronomische eenheden"
1655 print" (";z*150;" miljoen km.)."
1660 z=ca:gosub2650:print" Perihelium = ";z;"ae":print" Aphelium = ";
1665 z=fa:gosub2650:printz;"ae."
1670 z=pp:gosub2650:print" Een jaar is ";z;" aardejaren lang."
1680 print" ";s$;" lijkt";
1690 ifsa>1.5orsa<.75thenprint" veel";
1700 ifsa>1thenprint" groter":goto1710
1705 print" kleiner"
1710 print" dan onze zon."
1720 ifg<.95org>1.05then1730
1725 print" De zwaartekracht is vrijwel gelijk":print" aan die van de aarde."
1727 goto1800
1730 print" Aangezien de zwaartekracht";:ifg<1then1760
1740 print" groter is":print" dan op aarde verwachten we"
1750 print" een dichtere atmosfeer. De tektonische"
1752 print" werking is groter maar er is ook"
1754 print" meer weerstand. We verwachten daarom"
1756 print" meer continenten en kleinere bergen;"
1758 print" Aardbevingen komen vaker voor en zijn":print" heviger.":goto1780
1760 print" kleiner is":print" dan op aarde verwachten we"
1770 print" een dunnere atmosfeer. Er is minder"
1772 print" tektonische werking en ook de"
1774 print" weerstand is kleiner. We verwachten"
1776 print" daarom minder bergen, maar ze kunnen":print" veel hoger worden."
1778 print" Aardbevingen, als ze al voorkomen,"
1779 print" zullen minder hevig zijn."
1780 print" Een zwaartekracht van";g;"g betekent"
1785 print" dat iemand van 80 kilo op deze"
1787 print" planeet ";g*80;"kilo zou wegen."
1800 input" Wilt u een andere zwaartekracht";a$
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
