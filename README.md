# WorldBuilder
A modest program for designing stage new worlds.

The original was written by Stephen Kimmel and published in the June 1983 issue of
[Creative Computing Magazine](https://archive.org/details/CreativeComputing198306/page/n263/mode/2up).
For background information, the author refers to
["Planets for Man"](https://www.rand.org/pubs/commercial_books/CB183-1.html) by Stephen H. Dole and Isaac Asimov
and to "How to Build a Planet" [Poul Anderson](https://openlibrary.org/authors/OL24072A/Poul_Anderson).

## KIJK
Over time, different variations have emerged. A Dutch translation was made by Steven Bolt and Carl Koppeschaar
and published in January 1984 in the monthly magazine [KIJK](https://www.kijkmagazine.nl/).
For calculations of the ecosphere they also refer to
["Habitable Planets for Man"](https://www.rand.org/pubs/commercial_books/CB179-1.html) by Stephen H. Dole.

## Karen Hedlund
Karen Hedlund keyed in the program as listed in Creative Computing Magazine.
The source file and the accompanying documentation were downloaded from an unkown
source more than 20 years ago but seem to be no longer present on the Internet.

## Chris Croughton
The file planet.bas was found in the evolve package of Chris "Keris" Croughton.
It was downloaded from http://www.keris.net but that site, as well as the
mirror site http://www.keris.demon.co.uk and http://www.firedrake.org/keris,
is no longer available. The obvious reason is that Chris “Keris” Croughton
[lost his life](http://file770.com/chris-croughton-killed-in-accident/)
in a head-on traffic accident on November 10, 2011.

## projectrho
The file world.bas was extracted from [projectrho](http://www.projectrho.com/world.bas)
some time ago. The website contained no description, not even a link to the source file.
It does not seem to be present anymore.

## Updated versions
The orginal source code, as well as its variants, is rather old and specific for
some computer and BASIC version. Therefore, both the orginal version from Stephen Kimmel
as well as the Dutch version from the KIJK magazine are adapted to work with
[QB64](https://github.com/Galleondragon/qb64).

## Python version
The port to QB64 is kept close to the original code. Therefore, it is still old and
unstructured BASIC code. It really needs good refactoring. But instead of refactoring
the BASIC code, it is ported to [Python](https://www.python.org/) first. The Python
version is based on the Dutch version from the KIJK magazine. The initial version is
a simple BASIC to Python translation with some elementary functions extracted.
Further refactoring should provide descriptive variable names, clear functions,
documented algorithms, etc.
