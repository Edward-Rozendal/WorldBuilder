                              WORLDBR.BAS

WORLDBR is a program designed to build solar systems with planets
which could support humaniod life forms, which is a great aid to science
fiction writers, although it can be used as a game.  The program was
written by Stephen Kimmel and appeared in the June 1983 issue of
Creative Computing Magazine.  In the a later issue he stated that he has
an updated, enhanced listing available, but whether he still supports
the program is anyone's guest.   His address is (unless he's moved since
publication) is 4756 S. Irvington Place, Tulsa, Oklahoma 74135.  I keyed
in the program, incorporating the modifications that appeared in the
magazine a few months later, and configured it for Kaypros.  The program
is based on the 1970 edition of Habitable Planets For Man by Stephen
Dole and Isaac Asimov, and How to Build a Planet by Poul Anderson.

No knowledge of astronomy is necessary to use the program.  The
first question the program asks is about the star desired.  You are
given a choice of using stars already known to the program, or choosing
one of your own.  To use a star not already in the program, you enter
the absolute magnitude of the star or its spectral class.  Now don't
panic--the absolute magnitude of the star is a decimal number indicating
how many times brighter the star is than our own sun.  For best results
enter a .9 to 1.5.  The spectral class refers to the star's location on
the HR diagram, a combination of a letter and a number.  In descending
order, from hot stars to cool stars, the classes are O, B, A, F, G, K,
or M, combined with 1, 2, 3, 4, 5, 6, 7, or 8, with our sun usually
referred to as G3 or G2.  The program will respond with data about the
star's lifetime. You are then asked how much of this lifetime has
passed.  The program will then tell you the star's brightness, mass and
temperature, along with its possibility of supporting planets bearing
life.

The next section deals with your selection of the life-bearing
planet.  You are then asked questions about the temperature (in
fahrenheit, thankfully!) that you want the your planet to have, surface
gravity in relationship to earth's, size (diameter) in relationship to
earth's, and orbit eccentricity.  Be careful with the eccentricity, as
it is NOT relative to earth's; an eccentricity of 1 will send your
planet crashing into the sun at its closest approach.  For best results,
use the figure quoted for earth, or a lower one.  You are then asked for
the number of degrees the planet tilts on its axis (away from perfectly
upright); some tilt is desirable, to prevent the equator from being too
hot to be habitable, and 90 degrees is the programmed limit.

The next segment deals with the planet's moons, which determine the
length of its day.  You may select up to ten moons, and then are asked
to supply the masses and orbits, based on units of our moon.  When this
is completed, the program will give you temperature ranges for your
planet in summer, winter and average, length of day and year, orbit in
relationship to earth's, data about the moon system, and go on to
describe the possible lifeforms on the planets surface.

If your planet doesn't meet your needs, you can build another or go
on to add up to fourteen more planets to your system, although
unfortunately with these additional planets you are limited to inputing
only the mass and distance from the sun.  You are given a table of our
solar system as a guideline.

Error trapping is the best I've seen in any program.  It will not
allow you to put a moon or planet too close to another or the sun, where
the forces of gravity would crush it, or so far that it would drift
away.

For anyone not familiar with basic programs, sweep the program onto
your Mbasic disk, call for MBASIC at the command line.  At the ok type
RUN "WORLDBR" carriage return.  After exiting the program, type SYSTEM
to get back to CP/M.  It shouldn't be necessary to do a save function
unless you've tinkered with the source code, and if you do it with
Wordstar in the non-document mode, not even then.  Have fun!

For further reference, I kept a copy of the original article, or
you can find it in the UCLA engineering Math Science Library on the
eighth floor of Boelter Hall.  The main branch of the Santa Monica
Public Library has a copy of the first edition of the Dole-Asimov book,
copyright 1964.

                         -Karen Hedlund, Feb. 3, 1986
                          (213) 394-6523
