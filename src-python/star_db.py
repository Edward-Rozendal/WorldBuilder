#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A database of stars.

https://science.nasa.gov/sun/facts/
  “sol" is the Latin word for Sun.
https://www.star-facts.com/list-of-stars/
  https://www.star-facts.com/alpha-centauri/
  https://www.star-facts.com/epsilon-eridani-ran/
  https://www.star-facts.com/tau-ceti/
  https://www.star-facts.com/sirius/
  https://www.star-facts.com/canopus/
  https://www.star-facts.com/vega
  https://www.star-facts.com/arcturus/
  https://www.star-facts.com/rigel/
  https://www.star-facts.com/capella/
  https://www.star-facts.com/procyon/
  https://www.star-facts.com/achernar/
  https://www.star-facts.com/altair/
  https://www.star-facts.com/altair/
  https://www.star-facts.com/aldebaran/
  https://www.star-facts.com/spica/
  https://www.star-facts.com/antares/
  https://www.star-facts.com/pollux/
  https://www.star-facts.com/fomalhaut/
  https://www.star-facts.com/deneb/
  https://www.star-facts.com/regulus/
  https://www.star-facts.com/barnards-star/


## Mass-Luminosity Relationship
http://hyperphysics.phy-astr.gsu.edu/hbase/Astro/herrus.html#c3
https://en.wikipedia.org/wiki/Mass%E2%80%93luminosity_relation

For main sequence stars, the luminosity increases with the mass with the approximate
power law:

    L = L0 * (M/M0)^a

Where L0 and M0 re the luminosity and mass of the Sun and 3 < a < 4.
The value of 3.5 is most commonly used for main-sequence stars.

So, the relation between the mass and luminosity of a star is:

    L = M^3.5
    M = L^(1/3.5) = L^0.285714


## Lifespan
https://astronomy.swin.edu.au/cosmos/m/main+sequence+lifetime
http://hyperphysics.phy-astr.gsu.edu/hbase/Astro/startime.html
https://www.atnf.csiro.au/outreach/education/senior/astrophysics/stellarevolution_mainsequence.html

The overall lifespan of a star is determined by its mass. Since stars spend roughly
90% of their lives burning hydrogen into helium on the main sequence (MS), their
‘main sequence lifetime’ is also determined by their mass.

An expression for the main sequence lifetime can be obtained as a function of stellar
mass and is usually written in relation to solar units:

    t ~ t0 * (M0/M)^2.5

Where t0 is the main sequence lifetime of the Sun and M0 it mass.
The Sun, a G-type star with a main sequence lifetime of ~ 10 billion years.
The lifetimes of main sequence stars therefore range from a million years for a 40
solar mass O-type star, to 560 billion years for a 0.2 solar mass M-type star.


## Age
https://www.sciencenews.org/article/star-age-calculation-astronomy-life-cycle
The sun is the only star we know the age of. Everything else is bootstrapped up from there.

https://www.scientificamerican.com/article/how-do-scientists-determi/
A star like our sun is calculated to have a total stable life-span of around 10 billion years;
the sun is now a bit less than half that age (this age is very accurately determined from
radioactive elements in meteorites).

How do you measure the age of a star?
https://www.youtube.com/watch?v=w80z_moI8BU

What is the rationale behind the calculation of the passed lifespan fraction?
The calculation based only on mass and luminosity is useless as for all stars
in this database either the mass is calculated from the luminosity or the
other way around, resulting in lifespan fraction of 0.5 for all stars.
"""

from star import Star
from spectral_type import SpectralType


db_initialized = False

stars_name = [
    "sol", "alpha centauri a", "alpha centauri b", "epsilon eridani", "tau ceti",
    "70 ophiuchi a", "70 ophiuchi b", "eta cassiopeiae a", "eta cassiopeiae b",
    "sigma draconis", "36 ophiuchi a", "36 ophiuchi b", "hr-7703", "delta pavonis",
    "82 eridani", "beta hydri", "hr-8832", "sirius", "canopus", "vega", "arcturus",
    "rigel", "capella", "procyon", "achernar", "altair", "betelgeuze", "aldebaran",
    "spica", "antares", "pollux", "fomalhaut", "beta crucis", "deneb", "regulus",
    "barnard's star"]
starts_spectral_type = [
    "g2", "g4", "k1", "k2", "g8",
    "k1", "k5", "f9", "k6",
    "g9", "k2", "k1", "k2", "g7",
    "g5", "g1", "k3", "a1", "f0", "a0", "k2",
    "b8", "g8", "f5", "b5", "a7", "m2", "k5",
    "b1", "m1", "k0", "a3", "b0", "a2", "b7",
    "m5"]
first_half_stars_mass = [
    1.0, 1.08, 0.88, 0.80, 0.82, 0.9, 0.65, 0.94, 0.58,
    0.82, 0.77, 0.76, 0.76, 0.98, 0.91, 1.23, 0.74]
last_half_stars_luminosity = [
    23.0, 130.0, 52.0, 100.0, 52000.0, 145.0, 7.6, 1000.0, 10.0, 8300.0,
    160.0, 760.0, 830.0, 33.0, 13.0, 8300.0, 52000.0, 160.0, 0.00044]
stars_mass = []
stars_luminosity = []


def star_list():
    """Return a list of all start in the database"""
    return stars_name


def get_star(name):
    """Return a Star instance, or None if the name is not known"""
    if not db_initialized:
        initialize_db()
    try:
        index = stars_name.index(name)
    except ValueError:
        return None
    star = Star(name)
    star.spectral_type = SpectralType(starts_spectral_type[index])
    star.mass = stars_mass[index]
    star.luminosity = stars_luminosity[index]
    star.lifespan = 10 * pow(star.mass, -2.5)
    p = (1.25 - star.mass / pow(star.luminosity, 0.285714)) / 0.005
    if (p / 100 * star.lifespan) > 10:
        p = 1000 / star.lifespan
    star.life_fraction = p / 100
    return star


def initialize_db():
    """Initialize the star database"""
    global db_initialized
    if db_initialized:
        return
    stars_mass.extend(first_half_stars_mass)
    for i in range(len(last_half_stars_luminosity)):
        stars_mass.append(last_half_stars_luminosity[i] ** 0.285714)
    for i in range(len(first_half_stars_mass)):
        stars_luminosity.append(first_half_stars_mass[i] ** 3.5)
    stars_luminosity.extend(last_half_stars_luminosity)
    db_initialized = True
    pass
