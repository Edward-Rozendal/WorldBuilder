## World Builder: A Modest Program for Designing Strange New Worlds 

Poluxxy Araxxanas raised his head and looked at the dismembered corpse of his
foe with nictitating eyes. He clacked the chitin of his mouth opening and raised
his four arms to the huge red sun. The sound tied in his throat uncarried by the
thin air. On this cold day, victory was his. And the taste of it was bitter.

That is what computers and science fiction are about.

Both computers and science fiction offer the possibility of exploring worlds and
futures that could never be explored in reality. Or which would be instantly
fatal if you could. Anyone who uses the computer strictly as a means of freeing
valuable time to work more efficiently is missing part of what computers can do.
World Builder for the TRS-80 is designed to help bridge the gap and per-haps
enrich both science fiction and computers.

## Why a World Builder?
As a science fiction writer, I have an obligation to my readers to design
consistent, believable worlds. This can be a tedious process. There is always
the temptation simply to change the color of chlorophyll from green to blue and
let it go at that. Giving into temptation results in weaker science fiction so
I designed World Builder to help out. After seeing two recent articles in
Creative dealing with astronomy, I decided to modify it for general use.

World Builder is of interest even to those who don't read science fiction. It
has possibilities for use as an educational science program. Consider it a game,
if nothing else. Your first goal is to design a planet on which life can occur.
That is hard enough. The second goal is even harder: create a world that could
be inhabited by humans. You will find that the parameters for life in general
and humanity in particular are tight.

Most of what follows is rather technical. I won't be upset if you wish to skip
it. I will, however, suggest that you read Planets for Man by Stephen Dole and
Isaac Asimov. It is easy reading and fun. Much of this program is based on that
book and on How to Build a Planet by Pout Anderson.

## In the Beginning There Was Light
We begin with a star. The sun of any planetary system is the great thermonuclear
engine that drives the system. Everything else depends on it. The star may be so
large that its formation consumed all the nearby matter. If that is the case,
then there can be no planets. Another possibility is that the star is so small
that its gravity won't hold a planet of any appreciable size. Again, our quest
for a habitable planet has come to a quick end. When the star dies, it will
almost certainly destroy any planet close enough to support life. Therefore we
can't have too old a star. The larger stars come to this end at an early age and
in a most spectacular way-the super nova.

World Builder has two built-in assumptions concerning the star. First, the
program assumes that the star is on the "main sequence" of the
Hertzsprung-Russell diagram (a plot of spectral classes vs. the absolute
magnitude or luminosity of stars). The 1% of all stars that don't fall on the
main sequence are stars being born, which certainly won't have evolved life;
stars that are dying, which have destroyed any life that might have evolved;
and a few odd stars that we can probably ignore safely. The vast majority of
stars settle into a position on the sequence according to their mass and spend
most of their lives there. These are the stars that have the potential to host
life.

The second assumption in World Builder is that the star either is not a binary
star or can be treated as a single star. If the two stars of a binary are close
enough, the planet can orbit both of them at once in what will probably be a
highly eccentric orbit. Life may be possible, although the planet probably won't
be habitable by people due to the extreme seasonal temperature variation. If the
binary stars are far enough apart, then the planet could orbit one while feeling
little impact from the other. 

Consider what life on earth would be like if, instead of having Pluto, we had a
small star. Pluto receives so little energy from the sun that its surface
temperature is just a few degrees above absolute zero. Likewise, our second star
would contribute little energy to us. The result would be a more eccentric orbit
and a light in the sky brighter than anything but the sun and the moon. The main
effect would be on our mythologies.

World Builder contains data on 36 stars including 17 nearby stars felt to have a
reasonable chance (greater than 1% but never more than 6%) of having inhabited
planets. The rest of the stars on the list are well known. The complete' list
includes most of the brightest stars and a few that can't be seen whit the
unaided eye.

Most of the stars are on the main sequence illustrated in Figure 1. The most
significant exceptions are the giants, Rigel, Deneb, Betelgeuse, Antares,
Capella, Aldebaran, Arcturus, and Pollux. Obviously this doesn't begin to
exhaust the eighty gajillion stars, so the program has the option of using
stars not on the list. To use a star not on the list requires the use of either
the spectral class of the star or its absolute magnitude.

## The Business of Designing a Planet
Once we have settled on a star, we can get down to some of the more immediate
matters. Planets come in all sizes and locations. Our own solar system has an
interesting assortment of them. It should be said that the science isn't
precise. Much of what this program does is speculation and approximation. We
have only visited four bodies that could be considered planets. The others we
have either studied from Earth or from "close-ups" of several thousand miles.
At the range of some of these close-ups, we might be able to resolve objects
as small as New Jersey. There would be uncertainty about whether Earth was
inhabited by intelligent beings. Come to think of it, I know some people who
have the some doubts about Oklahoma.

After settling on a star, the most important discretionary item available to us
as planet builders is the average temperature of the planet. Temperature is
probably the single most important factor in determining habitability. It also
sets the approximate radius of the orbit of the planet about its sun. That, in
turn, determines the length of the planet year, and how big the star will appear
from the planet.

The size and location of any moons and the sun will determine how rapidly the
planet rotates. We have a 24-hour day because the tidal forces of our moon have
slowed the Earth down to that point. Jupiter, whose moons are much smaller in
relation to it than our moon is to us, has a day that is less than 10 hours
long. Jupiter is also much farther from the sun, so its tidal forces have little
effect.

The rotation of Venus, despite its having no moon, has been essentially stopped
by tidal forces caused by the sun. The importance of this to the temperature of
the planet is great. The dark side of Mercury gets down to —380°F, while the
temperature on the sun side gets over 600°F. A planet with a shorter day will
have smaller variations in its high and low temperature.

The tilt of the planet on its axis also has a profound impact on the temperature
of the planet. As every school child knows, winter occurs when the portion of
the Earth we happen to be on is tilted away from the sun. Earth has an axis tilt
of nearly 24 degrees. If the tilt were less, then summer and winter would be
more alike. A greater tilt would make a hotter summer and a colder winter.

The final factor contributing to the temperature profile of the planet is its
orbital eccentricity. Planets do not travel in perfect circles but in ellipses.
Eccentricity is a measure of the deviation from a perfect circle. It determines
the perihelion (the point of closest approach to the star) and aphelion (the
point of greatest distance from the star). The closer the planet is to the star
the warmer it is; the further away, the colder.

On Earth, which has a small eccentricity, the variation is a few degrees.
Summers are slightly warmer and winters slightly colder south of the equator.
If we had an eccentricity as high as that of Pluto, the difference would be
substantial.

The gravity of the planet is the last important characteristic that we are free
to set. This contributes significantly to determining the nature of the
atmosphere and the nature of life on the planet. If there is life on Jupiter,
and some scientists are serious about the possibility, then it certainly won't
look human. And it won't be able to survive on Earth.

Gravity directly affects the makeup of the atmosphere. If the gravity is too
high, the planet won't lose its primordial hydrogen; it will be a gas giant.
If the gravity is too low, the planet won't be able to hold onto its oxygen in
gaseous form. The result is a planet with an extremely thin atmosphere similar
to that found on the moon and on Mars.

World Builder does not consider the chemical composition of the atmosphere, and
that is probably a major weakness of the program. World Builder would predict
for Venus an atmosphere slightly thinner than that of Earth. That is not the
case. Venus has a massive atmosphere with a composition radically different from
Earth's, due in part at least to high concentrations of carbon dioxide. In
defense of World Builder it must be said that Venus could be terraformed into
retaining an Earth-like atmosphere.

## The Question of Life
For purposes of this program, I assume that life is a carbon-based chemistry
that requires liquid water in its environment. There are several other
possibilities although we currently have no proof that any of them exist.
Perhaps the most likely are those which don't require liquid water, either
converting ice or water vapor to water in their bodies. However, I don't see
how such life could evolve without a period of liquid water on the planet.

There are four requirements for life in the restricted context of this program.
There must be liquid water at least some of the time. The atmosphere must
contain some oxygen. The star must not have died. And there must be enough time
for life to evolve.

What will that life be like? That is the question. To some extent, we expect it
to look familiar. Function pushes evolution along the same lines. Thus dolphins,
goldfish and sharks have similar form despite having radically different
heritages. A classic example is bats and birds. We should be able to recognize
fish and birds as such no matter what planet they come from.

Land creatures offer a much wider range of variation. No one can say that every
possible combination has been tried on Earth. Some other arrangements might be
highly successful in other environments. Still we should be able to recognize
eyes, legs and mouths. Hands may be a different story, although our design
should work in almost any environment.

Gravity is the primary factor affecting life that is dealt with in World
Builder. High gravity makes it harder to stand up. Anything that isn't hugging
the ground will be more heavily reinforced than it would be on Earth. Bodies and
trees will be thicker and shorter. Rising up on two legs may be impossible.

Low gravity would have the opposite effect. With less pull to overcome, rising
on two legs is easier. Creatures need less reinforcement to overcome gravity.
The air should be thinner, reducing the effect of the wind and the ability to
carry sounds. Beings in a thick, high gravity atmosphere would place a premium
on a streamlined form. Creatures in a low gravity, thin atmosphere won't
consider this such an advantage.

And humans? Will they be able to live on the planet? I have taken the
restrictions to be those shown in Figure 2.

```
Temperature:
    Mean Annual Temperature     min 32°F
                                max 86°F
    High Daily Mean             less than 120°F
    Low Daily Mean              greater than —10°F
Gravity                         min .68 (Earth= 1.)
                                max 1.5
Mass                            min .4
                                max 2.35
Day less                        than 96 hours
Surface Water                   Liquid < 90%
Prevailing Wind                 <50 mph 
Atmosphere:
    Pressure                    min 2 psia
                                max 50 psia
    Oxygen, partial pressure    min 50 mmHg
                                max 400 mmHg
Other Life 
```
Figure 2. Requirements for human habitability

One requirement is for other life. Without an existing biosphere with all its
delicate balances and support systems, we would be living in an artificial
environment. Without photosynthesis to regenerate oxygen, we would have to
generate it ourselves. Again, there is little point in leaving the relative
comfort and safety of our space craft if we must rebuild it on the surface of
the planet. Of course, you might terraform an otherwise uninhabitable planet,
but that is a matter beyond the scope of this program.

## Thoughts on Earth
At first glance, Earth appears to have a unique position in the cosmos. You
couldn't adjust the parameters of World Builder too much without making it
uninhabitable. This really doesn't come as a surprise. Of the four bodies we
have visited, Earth, Mars, Venus, and the moon, only Earth has what is
unquestionably life.

There probably is no life anywhere else in our solar system. The only other
candidates are long shots. Isolated pockets on Mars and the clouds of Jupiter
don't seem particularly promising and Saturn's moon, Titan, is only slightly
better. If the assumptions of this program are correct, we have no better
than a fifty-fifty chance of finding a habitable planet within 25 light years
of Earth.

Earth is the nearly perfect home for humanity but not because it was created
that way. Humanity was created, by whatever means, to be perfectly at home on
Earth. We grew up here. We wouldn't expect to do any better on most other
planets than we would expect a sparrow to do under water. If we had grown up
on Titan, a —200°F methane pool would seem perfect for a hot summer's swim.

Is Earth the sole harbor of life in the black sea of space? I. can't believe
that it is. There are billions and billions of stars (sorry, Carl) out there
and at least an equal number of planets. If there is no life anywhere else in
the universe then that is a waste unparalleled by anything in creation. The
probability that Earth is the exclusive home for life is well over a billion
to one. It might be, but I wouldn't bet on it.

## World Builder sample run.
```
WORLD BUILDER
ENTER THE NUMBER FOR THE OPTION YOU WANT 

1....USE A KNOWN STAR
2....USE A STAR NOT ON LIST
3....LIST KNOWN STARS
4....QUIT YOUR CHOICE? 3_ 

I KNOW THE FOLLOWING STARS
SOL                 HR 7703           ACHERNAR
ALPHA CENTURI A     DELTA PAVONIS     ALTAIR
ALPHA CENTURI B     82 ERIDANI        BETELGEUSE
EPSILON ERIDANI     BETA HYDRI        ALDEBARAN
TAU CETI            HR 8832           SPICA
70 OPHIUCHI A       SIRIUS            ANTARES
70 OPHIUCHI B       CANOPUS           POLLUX
ETA CASSIOPEIAE A   VEGA              FOMALHAUT
ETA CASSIOPEIAE B   ARCTURUS          BETA CRUCIS
SIGMA DRACONIS      RIGEL             DENEB
36 OPHIUCHI A       CAPELLA           REGULUS
36 OPHIUCHI B       PROCYON           BARNARD'S STAR
WHICH STAR SHOULD I USE? TAU CETI_ 

STELLAR DATA
THE SELECTED STAR, TAU CETI, IS A G 8 STAR
IS ORANGE
HAS A MASS OF .82 TIMES THAT OF THE SUN
IT IS .499285 TIMES AS BRIGHT AS THE SUN
THE STAR HAS AN EXPECTED LIFESPAN OF 16.4235 BILLION YEARS
OF WHICH IT HAS LIVED 50.0001 % OR ABOUT 8.21175 BILLION YEARS. 

IT HAS A SURFACE TEMPERATURE OF 5597.4 DEGREES KELVIN
AND MAY HAVE PLANETS
THIS STAR WILL DIE AS A WHITE DWARF
ANOTHER STAR? NO 

THE MAIN PLANET OF INTEREST
THE EARTH HAS AN AVERAGE SURFACE TEMPERATURE OF 60 DEGREES
WHAT SURFACE TEMPERATURE WOULD YOU LIKE? 50
DESIRED SURFACE GRAVITY (EARTH.1)? .85
HOW BIG SHOULD THE PLANET BE RELATIVE TO EARTH? .75 

EARTH'S ORBIT HAS AN ECCENTRCITY OF .01672
WHAT IS THE ORBITAL ECCENTRICITY ( <1)? .02
HOW DOES THE AXIS TILT (EARTH.23.5 DEGREES)? 10
HOW MANY MOONS DOES THE PLANET HAVE? 2
MASS OF MOON # 1 (OUR MOON.1)? .5
ORBIT (OUR MOON.30)? 20
MASS OF MOON # 2 (OUR MOON.1)? .2
ORBIT (OUR MOON=30)? 40_

THIS PLANET'S DAY SHOULD BE ABOUT 27.1068 HOURS LONG.
THAT MAKES ITS YEAR 224.842 DAYS LONG. WITH A TILT OF 10
TODAY'S HIGH TEMPERATURE SHOULD BE 64.4005 DEGREES F.
TONIGHT'S EXPECTED LOW IS 35.5995 DEGREES F.
THIS SUMMER WE EXPECT IT TO GET UP TO 84.1681
THIS WINTER IT SHOULD DROP DOWN TO 17.3373 

YOUR SELECTED SYSTEM OF MOONS
ORBIT            MASS         PERIOD
20                .5           517.41 HOURS 19.0878 DAYS
40                .2           1463.45 HOURS 53.9886 DAYS
WANT A DIFFERENT SET OF MOONS? NO_ 

PLANETARY DATA
OUR PRINCIPAL PLANET OF INTEREST HAS AN AVERAGE SURFACE
TEMPERATURE OF 50 DEGREES F. THIS REQUIRES AN ORBIT
OF .734582 ASTRONOMICAL UNITS ( 68.3162 MILLION MILES)
CLOSEST APPROACH = .719891 AU. GREATEST DISTANCE .749274 AU
THIS ALSO MEANS IT HAS A YEAR THAT IS .695271 YEARS LONG
THE STAR APPEARS LARGER THAN OUR SUN.
SINCE OUR PLANET HAS A GRAVITY LESS THAN EARTH'S WE EXPECT
A THINNER ATMOSPHERE. THERE IS LESS TECTONIC ACTION AND LESS
RESISTANCE. THUS WE EXPECT FEWER MOUNTAINS BUT THEY MAY BE MUCH
TALLER. EARTHQUAKES, IF ANY, WILL BE LESS SEVERE.
A GRAVITY OF .85 MEANS THAT IF YOU WEIGH 200 POUNDS
YOU WOULD WEIGH 170 ON OUR PLANET
WOULD YOU LIKE A NEW GRAVITY? NO 

LIFE ???
THERE MAY BE SOME MAJOR LAND ANIMALS AND PERHAPS INTELLIGENCE
LOWER GRAVITY MEANS A THINNER ATMOSPHERE. BIRDS, IF ANY, WILL
HAVE LARGER WINGS. ALL LIFE FORMS SHOULD BE TALLER AND MORE
SLENDER THAN ON EARTH.
IT THERE PROBABLY ARE MANY TWO LEGGED ANIMALS.
THE THIN ATMOSPHERE HURTS SOUND TRANSMISSION SO ANIMALS WILL
EITHER HAVE LARGE EARS OR NONE. LUNGS WILL BE MUCH LARGER.
SOME FORM OF RADIATION PROTECTION WILL BE NECESSARY.
THIS PLANET MIGHT BE CONSIDERED HABITABLE BY MAN.
WANT ANOTHER PLANET? NO_ 

OUR SOLAR SYSTEM IS LAID OUT LIKE THIS:
PLANET      MASS      DISTANCE FROM SUN
MERCURY     .055       .387
VENUS       .815       .723
EARTH        1.0        1.0
MARS        .108       1.524
JUPITER     317.9      5.203
SATURN       95.2      9.539
URANUS       14.6      19.18
NEPTUNE      17.2      30.06
PLUTO       .100       39.44
MASS FOR PLANET # 2 ? 2000
A BODY THIS LARGE WOULD BECOME A STAR.
MASS FOR PLANET # 2 ? 400
DISTANCE FROM STAR? 4_ 

PLANET #       MASS            ORBIT
 1               .8              .5 
 2               .478125         .734582 LIFE?
 3               .45             .9 LIFE?
 4               10              40
WOULD YOU LIKE TO TRY ANOTHER SYSTEM? NO
WOULD YOU LIKE TO TRY ANOTHER STAR? NO
READY
```
