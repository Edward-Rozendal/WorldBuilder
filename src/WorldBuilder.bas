5 SCREEN 12: CLS
10 FOR i=1 TO 700: COLOR (1): PSET (RND*640, RND*480): NEXT i
15 FOR i=1 TO 100: COLOR (2): PSET (RND*640, RND*480): NEXT i
17 FOR i=1 TO 100: COLOR (3): PSET (RND*640, RND*480): NEXT i
20 LOCATE 8, 30: PRINT "** WORLD BUILDER **"
30 LOCATE 10, 30: PRINT "BY STEPHEN KIMMEL"
40 LOCATE 12, 30: PRINT "A PROGRAM FOR DESIGNING WORLDS"
50 LOCATE 14, 30: PRINT "WHERE NO MAN HAS BEEN BEFORE"

60 DIM SC$(8),M(8),C$(8),S$(36),LS(36),SS$(36),SM(36),MP(15),R(15)
70 FOR I=1TO8:READ SC$(I),M(I),C$(1):NEXT I
80 FOR I=1TO17;READ S$(I),SS$(I),SM(I);LS(I)=SM(I)[3.5:NEXT
90 FOR I=18TO36;READ SS(I),SS$(1),LS(I):SM(I)=LS(I)[.285714:NEXT
100 DATA 0,100,BLUE,B,17,PALE BLUE,A,3.2,WHITE,F,1.54,PALE YELLOW
110 DATA G,1.02,YELLOW,K,.75,0RANGE,M,.38,RED,D,O.,RED
120 DATA SOL,G2,1.0,ALPHA CENTURI A,G4,1.08,ALPHA CENTURI B,K1,.88
130 DATA EPSILON ERIDANI,K2,.80,TAU CETI,G8,.82
140 DATA 70 OPHIUCHI A,K1,.9,70 OPHIUCHI B,K5,.65
150 DATA ETA CASSIOPEIAE A,F9,.94,ETA CASSIOPEIAE B,K6,.58
160 DATA SIGMA DRACONIS,G9,.82,36 OPHIUCHI A,R2,.77
170 DATA 36 OPHIUCHI B,K1,.76,HR 7703,K2,.76 
180 DATA DELTA PAVONIS,G7,.98,82 ERIDANI,G5,.91
190 DATA BETA HYDRI,G1,1.23,HR 8832,K3,.74
200 DATA SIRIUS,A1,23,CANOPUS,F0,130,VEGA,A0,52,ARCTURUS,K2,100
210 DATA RIGEL,B8,52000,CAPELLA,G8,145,PROCYON,F5,7.6
220 DATA ACHERNAR,B5,1000,ALTAIR,A7,10,BETELGEUSE,M2,8300
230 DATA ALDEBARAN,K5,160,SPICA,B1,760,ANTARES,M1,830
240 DATA POLLUX,K0,33,FOMALHAUT,A3,13,BETA CRUCIS,B0,8300
250 DATA DENEB,A2,52000,REGULUS,B7,160,BARNARD'S STAR,M5,.00044
260 CLS:PRINT"WORLD BUILDER"
270 PRINT"ENTER THE NUMBER FOR THE OPTION YOU WANT"
280 PRINT:PRINT"1....USE A KNOWN STAR"
290 PRINT"2....USE A STAR NOT ON LIST"
300 PRINT"3....LIST KNOWN STARS"
310 PRINT"4....QUIT"
320 INPUT"YOUR CHOICE";A
330 IF A<1 OR A>4 GOTO 260
340 ON A GOTO 410 ,550 ,370 ,350
350 INPUT"ARE YOU SURE YOU WANT TO QUIT":A$
360 IF ASC(A$)=89 THEN END ELSE GOTO 260
370 CLS:PRINT"I KNOW THE FOLLOWING STARS"
380 FOR I=1TO 12
390 PRINTS$(I);TAB(20);S$(I+12);TAB(40);S$(I+24)
400 NEXT I
410 INPUT"WHICH STAR SHOULD I USE";S$
420 IF SS="NONE" OR S$="" THEN 260
430 FOR I=1TO 36
440 IF S$=S$(I) THEN SK=I:GOTO 470
450 NEXT I
460 PRINT"I DON'T KNOW THAT STAR" : GOTO 270
470 SC=VAL(RIGHTS(SS$(SK),1))/10
480 Sl$=LEFT$(SS$(SK),1)
490 FOR I=1TO7:IF Sl$=SC$(I) THEN J=I:GOTO 510
500 NEXT I
510 MS=SM(SK):L=LS(SK):AS,MS(-2.5)*10
520 P=(1.25-MS/(L(.285714))/.005
530 IF P/100*AS>10 THEN P=1000/AS
540 GOTO 740
550 INPUT"WHAT IS THE STAR'S NAME";S$
560 INPUT"WHAT IS THE STAR'S SPECTRAL CLASS";S1$
570 IF S1$<>"" GOTO 640
580 INPUT"WHAT IS THE ABSOLUTE MAGNITUDE (SUN=4.85)";M
590 L=EXP(1.94-.4*M): <S=L[.285714
600 FOR I=1TO7:IF M(I)<MS THEN J=I-1:GOTO 620
610 NEXT I
620 S1$=SC$(I-1):SC=INT((MS-M(J))/(M(I)-M(J)))/10
630 GOTO 680
640 SC=VAL(RIGHTS(S1$,1))/10 : Sl$=LEFTS(S1$,1)
650 FOR I=1TO7:IF Sl$=SC$(I) THEN J=I:GOTO 670
660 NEXT I:PRINT"I DON'T KNOW THAT CLASS":GOTO 560
670 MS=M(J)-SC*(M(J)-M(J+1))
680 AS=MS(-2.5)*10
690 PRINTS$;" HAS AN EXPECTED LIFE OF ";AS;" BILLION YEARS"
700 INPUT"WHAT PERCENT (1-100) HAS ALREADY PASSED";P
710 IF F/100*AS>12 PRINT"THE BIG BANG OCCURED 12 BILLION YEARS AGO.": INPUT"IS THIS WHAT YOU WANT";A$:IF ASC(AS)<>89 THEN 690
720 MS=MS*(1.25-.005*P)
730 L=MS[3.5
740 TS=6000*MS[.35
750 DS=MS[.3333
760 CLS:PRINT"STELLAR DATA"
770 PRINT"THE SELECTED STAR, ";S$;", IS A ";S1$,SC*10;" STAR"
780 IF SC>.75 PRINT"IS ";C$(J+1) : GOTO 810
790 IF SC<.25 PRINT"IS ";C$(J) GOTO 810
800 PRINT"IS BETWEEN ";C$(J);" AND ";C$(J+1)
810 PRINT"HAS A MASS OF ";MS;" TIMES THAT OF THE SUN"
820 PRINT"IT IS ";L;" TIMES AS BRIGHT AS THE SUN"
830 PRINT"THE STAR HAS AN EXPECTED LIFESPAN OF";AS;" BILLION YEARS"
840 PRINT"OF WHICH IT HAS LIVED";P;"% OR ABOUT";AS*P/100;"BILLION YEARS."
850 IF P>95 PRINT" THE STAR IS IN ITS DEATH THROES."
860 PRINT"IT HAS A SURFACE TEMPERATURE OF ";TS;" DEGREES KELVIN"
870 IF J+SC<2.5 OR J+SC>7 PRINT"AND IS BELIEVED TO HAVE NO PLANETS":GOTO 890
880 PRINT"AND MAY HAVE PLANETS"
890 PRINT"THIS STAR WILL DIE AS A ";
900 IF MS<1.5 PRINT"WHITE DWARF": GOTO 940
910 IF MS<4.0 PRINT"NEUTRON STAR": GOTO 940
920 IF MS<10. PRINT"NEUTRON STAR AFTER GOING NOVA":GOTO 940
930 PRINT"BLACK HOLE AFTER GOING SUPER NOVA"
940 INPUT"ANOTHER STAR";A$
950 IF ASC(A$)=89 THEN 260
960 P=P/100
970 CLS:PRINT"THE MAIN PLANET OF INTEREST"
980 PRINT"THE EARTH HAS AN AVERAGE SURFACE TEMPERATURE OF 60 DEGREES"
990 INPUT"WHAT SURFACE TEMPERATURE WOULD YOU LIKE";TP:TP=TP+460
1000 INPUT"DESIRED SURFACE GRAVITY (EARTH=1)";G
1010 IF G<=0 PRINT"THE PLANET MUST HAVE SOME GRAVITY":GOTO 1000
1020 RP=SQR(L/(TP/520)[4)
1030 IF RP<MS/5 PRINT"THIS PLANET IS TOO CLOSE TO BE STABLE.":GOTO 980 
1040 PP=SQR(RP[3/MS)
1050 IS=L/RP[2
1060 RM=.00012*TS
1070 RX=.06452*EXP(.0005*TS)
1080 SA=DS/RP
1090 INPUT"HOW BIG SHOULD THE PLANET BE RELATIVE TO EARTH",D
1100 M=G*D[2
1110 IF M<.055 PRINT"THE PLANET WON'T RETAIN AN OXYGEN ATMOSPHERE"
1120 IF M>17.6 PRINT"THE PLANET WON'T LOSE ITS HYDROGEN ATMOSPHERE"
1130 PRINT"EARTH'S ORBIT HAS AN ECCENTRCITY OF .01672"
1140 INPUT"WHAT IS THE ORBITAL ECCENTRICITY ( <1)";EC
1150 IF EC>1 THEN 1140
1160 CA=(1-EC)*RP : FA=(1+EC)*RP
1170 INPUT"HOW DOES THE AXIS TILT (EARTH=23.5 DEGREES)";TI
1180 IF TI<0 OR TI>90 THEN 1170
1190 INPUT"HOW MANY MOONS DOES THE PLANET HAVE";MN
1200 IF MN>10 PRINT"FOR CONVENIENCE WE'LL LIMIT THIS TO 10":MN=10
1210 MM=1000:H=0:R=56*G
1220 IF MN<=0 THEN 1320
1230 FOR I=1TOMN
1240 PRINT"MASS OF MOON #";I;" (OUR MOON=1)";:INPUT MN(I)
1250 INPUT"ORBIT (OUR MOON=30)";MR(I)
1260 IF MR(I)<3*G PRINT"THE MOON IS TOO CLOSE AND WILL BREAK UP":GOTO 1250
1270 IF MR(I)>56*G PRINT"THE MOON IS TOO FAR AND WILL DRIFT AWAY":GOTO 1250
1280 MP(I)=SQR(MR(I)[3/M)*4
1290 IF MR(I)<R THEN MM=MP(I):R=MR(I)
1300 H=MN(I)*.01235/(MR(I)[3)+H
1310 NEXT I
1320 H2=.85*D[4/M*(MS*333500/(11759*RP)[3+H)
1330 DA=1.75926E+06*H2*14+10
1340 IF DA>MM THEN DA=MM
1350 CLS:PRINT"THIS PLANET'S DAY SHOULD BE ABOUT";DA;" HOURS LONG."
1360 PRINT"THAT MAKES ITS YEAR";8766/DA*PP;"DAYS LONG. WITH A TILT OF";TI
1370 H1=1+.025*DA/24)*TP-460 LO=(1-.025*DA/24)*TP-460
1380 IF LO<-460 THEN LO=-460
1390 PRINT"TODAY'S HIGH TEMPERATURE SHOULD BE";HI;" DEGREES F."
1400 PRINT"TONIGHT'S EXPECTED LOW IS";LO;" DEGREES F."
1410 SH=HI+1.9*TI*(1+EC[12 : LL=L0-1.9*TI/(1+EC)[2
1420 IF LL<-460 THEN LL=-460
1430 PRINT"THIS SUMMER WE EXPECT IT TO GET UP TO";SH
1440 PRINT"THIS WINTER IT SHOULD DROP DOWN TO";LL
1450 IF SH<32 OR LL>175 PRINT"THERE ARE TIMES WHEN NO LIQUID WATER EXISTS."
1460 IF MN<=0 GOTO 1600
1470 IF MN=1 GOTO 1570
1480 FOR I=170 MN:F=0:FOR K=1TOMN-I
1490 IF MR(K+1)>=MR(K) THEN 1540
1500 T=MR(K):MR(K)=MR(K+1):MR(K+1)=T
1510 T=MN(K):MN(K)=MN(K+1):MN(K+1)=T
1520 T=MP(K):MP(K)=MP(K+1):MP(K+1)=T
1530 F=1
1540 NEXT K
1550 IF F=0 THEN 1570
1560 NEXT I
1570 PRINT:PRINT"YOUR SELECTED SYSTEM OF MOONS"
1580 PRINT"ORBIT","MASS","PERIOD"
1590 FOR I=1TOMN:PRINTMR(I),MN(I),MP(I);"HOURS ";MP(I)/DA;" DAYS":NEXTI
1600 INPUT"WANT A DIFFERENT SET OF MOONS";AS
1610 IF ASC(A$)=89 THEN 1190
1620 CLS:PRINT"PLANETARY DATA"
1630 PRINT"OUR PRINCIPAL PLANET OF INTEREST HAS AN AVERAGE SURFACE"
1640 PRINT"TEMPERATURE OF";TP-460;" DEGREES F. THIS REQUIRES AN ORBIT"
1650 PRINT"OF";RP;" ASTRONOMICAL UNITS (";RP*93;" MILLION MILES)"
1660 PRINT"CLOSEST APPROACH =";CA;" AU: GREATEST DISTANCE =";FA;" AU"
1670 PRINT"THIS ALSO MEANS IT HAS A YEAR THAT IS";PP;" YEARS LONG"
1680 PRINT"THE STAR APPEARS";
1690 IF SA>1.5 OR SA <.75 PRINT" MUCH";
1700 IF SA >1. PRINT" LARGER";: ELSE PRINT" SMALLER";
1710 PRINT" THAN OUR SUN."
1720 IF G>.95 AND G<1.05 PRINT"GRAVITY IS ESSENTIALLY THE SAME AS EARTH'S" :GOTO 1780
1730 PRINT"SINCE OUR PLANET HAS A GRAVITY";:IF G<1 THEN 1760
1740 PRINT" GREATER THAN EARTH'S WE EXPECT"
1750 PRINT"A THICKER ATMOSPHERE. THERE IS GREATER TECTONIC ACTION AND MORE GREATER RESISTING FORCES. THUS WE EXPECT MORE CONTINENTS AND SHORTER MOUNTAINS. EARTHQUAKES SHOULD BE MORE FREQUENT AND MORE SEVERE.":GOTO1780
1760 PRINT" LESS THAN EARTH'S WE EXPECT"
1770 PRINT"A THINNER ATMOSPHERE. THERE IS LESS TECTONIC ACTION AND LESS RESISTANCE. THUS WE EXPECT FEWER MOUNTAINS BUT THEY MAY BE MUCH TALLER. EARTHQUAKES, IF ANY, WILL BE LESS SEVERE."
1780 PRINT"A GRAVITY OF ";G;" MEANS THAT IF YOU WEIGH 200 POUNDS"
1790 PRINT"YOU WOULD WEIGH";G*200;" ON OUR PLANET"
1800 INPUT"WOULD YOU LIKE A NEW GRAVITY";A$
1810 IF ASC(AS)=89 THEN 1000
1820 CLS:PRINT"L1FE ???"
1830 IF M<.055 OR M>17.6 PRINT"BECAUSE OF THE BAD ATMOSPHERE ":GOTO2080 
1840 IF RP<RM OR RP>RX PRINT"BECAUSE OF THE LEVEL OF RADIATION ":GOTO2080
1850 IF SH<32 OR LL>175 PRINT"SINCE LIQUID WATER NEVER OCCURS ":GOTO 2080
1860 IF AS*P <1.5 PRINT"THE PLANET IS TOO YOUNG TO HAVE EVOLVED LIFE":GOTO 2080
1870 IF P>.95 PRINT"SINCE THE STAR IS IN ITS DEATH THROES ":GOTO 2080
1880 PRINT"THERE MAY BE SOME ";
1890 IF AS*P<2*G PRINT"BACTERIA AND BLUE GREEN ALGAE":GOTO2060
1900 IF AS*P<3*G PRINT"SINGLE CELL LIFE WITH NUCLEUS":GOTO2060
1910 IF AS*P<4*G PRINT"SIMPLE MULTICELLED LIFE":GOTO2060
1920 IF AS*P<4.4*G PRINT"WATER VERTEBRATES AND LAND PLANTS":GOTO2060
1930 PRINT"MAJOR LAND ANIMALS AND PERHAPS INTELLIGENCE"
1940 IF G<.95 THEN 1990
1950 IF G<1.05 THEN 2030
1960 PRINT"HIGNER GRAVITY MEANS A THICK ATMOSPHERE WHICH WILL SUPPORT LARGEBIRDS. IT ALSO MEANS THAT SHORT FALLS COULD BE FATAL SO REACTIONTIMES SHOULD BE VERY SHORT. ALL LIFE FORMS WILL BE SHORTER AND STOCKIER THAN ON EARTH."
1970 IF G>1.2 PRINT"THERE ARE NO TWO LEGGED ANIMALS."
1980 PRINT"THE THICK ATMOSPHERE IMPROVES SOUND TRANSMISSION SO THE ANIMALS MAY WILL RELY MORE ON HEARING.":GOTO2030
1990 PRINT"LOWER GRAVITY MEANS A THINNER ATMOSPHERE. BIRDS, IF ANY, WILL HAVE LARGER WINGS. ALL LIFE FORMS SHOULD BE TALLER AND MORE SLENDER THAN ON EARTH."
2000 PRINT"IT THERE PROBABLY ARE MANY TWO LEGGED ANIMALS."
2010 PRINT"THE THIN ATMOSPHERE HURTS SOUND TRANSMISSION SO ANIMALS WILL EITHER HAVE LARGE EARS OR NONE. LUNGS WILL BE MUCH LARGER."
2020 IF TP>75 PRINT"SOME FORM OF RADIATION PROTECTION WILL BE NECESSARY."
2030 IF SA<.75 PRINT"BECAUSE OF THE SMALL SUN, WE EXPECT ANIMALS TO HAVE LARGE EYES OR TO RELY ON OTHER SENSES."
2040 IF SA>1.5 PRINT"UNLESS THE ATMOSPHERE IS OBSCURED, WE EXPECT RELIANCE ON SIGHT USING RELATIVELY SMALL EYES."
2050 IF HI-LO>50 PRINT"EXTREME TEMPERATURE VARIATIONS FAVOR UNDERGROUND AND UNDERWATER LIFEFORMS."
2060 IF(TP-460)<32 OR (TP-460)>86 OR G>1.5 OR G<.68 OR M<.4 OR M>2.35 OR DA>96 OR SH>120 OR LL<-30 OR HI>110 OR LO<-10 THEN HM=O ELSE HM1
2070 GOTO 2090
2080 PRINT"THERE APPEARS TO BE NO LIFE ON THIS PLANET."
2090 PRINT"THIS PLANET ";:IF HM=1 PRINT"MIGHT BE";:ELSE PRINT"WOULDN'T BE";
2100 PRINT" CONSIDERED HABITABLE BY MAN."
2110 INPUT"WANT ANOTHER PLANET";A$
2120 IF ASC(A$)=89 THEN 970
2130 CLS:PRINT"OTHER PLANETS"
2140 INPUT"HOW MANY PLANETS WOULD YOU LIKE";NP
2150 IF NP>15 PRINT"FOR CONVENIENCE WE'LL LIMIT THIS TO 15":NP=15
2160 IF NP<=1 THEN 2600
2170 AM=1180/SQR(MS)-M*SQR(RP)
2180 R(1)=RP:MP(1)=M
2190 FOR I=2TONP
2200 CLS
2210 PRINT"OUR SOLAR SYSTEM IS LAID OUT LIKE THIS:"
2220 PRINT"PLANET      MASS      DISTANCE FROM SUN"
2230 PRINT"MERCURY     .055       .387"
2240 PRINT"VENUS       .815       .723"
2250 PRINT"EARTH        1.0        1.0"
2260 PRINT"MARS        .108       1.524"
2270 PRINT"JUPITER     317.9      5.203"
2280 PRINT"SATURN       95.2      9.539"
2290 PRINT"URANUS       14.6      19.18"
2300 PRINT"NEPTUNE      17.2      30.06"
2310 PRINT"PLUTO       .100       39.44"
2320 PRINT"MASS FOR PLANET #";I;:INPUTMP(I)
2330 IF MP(I)>1000 PRINT"A BODY THIS LARGE WOULD BECOME A STAR.":GOTO 2320
2340 INPUT"DISTANCE FROM STAR";R(I)
2350 IF R(I)<MS/5  PRINT"PLANET IS TOO CLOSE TO SUN":GOTO2340
2360 IF R(I)>56*MS PRINT"PLANET IS TOO FAR FROM THE SUN":GOTO 2340
2370 FOR K=1TOI-1:IF R(K)>.9*R(I) AND R(K)<1.1*R(I) THEN 2430
2380 NEXT K
2390 A1=MP(I)*S4R(R(I))
2400 IF Al>AM PRINT"THE PLANET HAS TOO MUCH MASS FOR SYSTEM":GOTO 2210
2410 AM=AM-Al
2420 NEXT I:GOTO 2450
2430 PRINT"THIS PLANET IS TOO CLOSE TO OTHER PLANETS TO HAVE A STABLE ORBIT"
2440 GOTO 2210
2450 FOR I=1TONP:F=0:FOR K=1TONP-I
2460 IF R(K+1)>=R(K) THEN 2500
2470 T=R(K):R(K)=R(K+1):R(K+1)=T
2480 T=MP(K):MP(K)=MP(K+1):MP(K+1)=T
2490 F=1
2500 NEXT K
2510 IF F=0 THEN 2530
2520 NEXT I
2530 PRINT"PLANET #       MASS            ORBIT"
2540 FOR I=1TONP
2550 PRINT,I,MP(1),R(I):
2560 IF R(I)>RM AND R(I)<RX AND MP(I)>.055 AND MP(I)<17.6 PRINT"LIFE?" ELSE PRINT" "
2570 NEXT I
2580 INPUT"WOULD YOU LIKE TO TRY ANOTHER SYSTEM";A$
2590 IF ASC(AS)=89 THEN 2130
2600 INPUT"WOULD YOU LIKE TO TRY ANOTHER STAR";A$
2610 IF ASC(AS)=89 THEN 260
2620 END
