#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
"""
## Star appearance
The appearance of a star, how big it looks, depends on both its diameter and distance.
Assuming each star has the same mass density, the diameter relative to the Sun depends
equally to their mass as their volume. The volume of a sphere is: 
    V = 4/3 * pi * r^3
Given that the size in inversely proportional to its distance (the Planets radius),
the size relative to the Sun is:
    size = mass^0.3333 / distance

## Year length in Earth years
The length of a year, the orbital period, can be calculated with Kepler’s Third Law:
    P^2 = a^3
Where a is the size of orbit expressed in astronomical units (1 AU equals the average distance
between the Earth and Sun) and P the period measured in (Earth) years.
After applying Newton’s Laws of Motion and Newton’s Law of Gravity, and assuming the mass
of the planet is negligible to the mass of the star, a general form of Kepler’s Third Law
becomes:
    M * P^2 = a^3
With M being the mass of the central star in units of the mass of the Sun. So the orbital
period, in earth years, can be calculated with:
    year_length = sqrt(radius^3 / star.mass)
source: https://people.astro.umass.edu/~weinberg/a114/handouts/concept1.pdf

## Year length in planet days.
An Earth year is 365,25 day * 24 hours per day = 8766 hours long, so:
    year_days = year_length * 8766 / day_length
With year_length in Earth days and day_length in hours.

## Perihelion and Aphelion
Eccentricity is calculated using the following formula:
    eccentricity^2 = 1.0 - semi-minor-axis^2 / semi-major-axis^2

Given the the length of an orbit's major axis and its eccentricity, perihelion and aphelion
distances can be calculated using the following formula:
    perihelion = semi-major-axis * (1.0 - eccentricity)
    aphelion = semi-major-axis * (1.0 + eccentricity)

Earth has a very low eccentricity. This helps keep the planet's supply of solar radiation
relatively consistent throughout the year and means that Earth's eccentricity doesn't have
an extremely noticeable impact on our day-to-day lives. (The tilt of the earth on its axis
has a much more noticeable effect on our lives by causing the existence of seasons.)
source: https://www.sciencing.com/calculate-perihelion-5344973/
"""


class Planet:
    def __init__(self, star):
        self.star = star
        self.radius = 0  # AU (astronomical unit)
        self.year_length = 0  # Earth years
        self.mass = 0  # Earth masses
        self.temperature = 0  # Degrees Celsius
        self.gravity = 0  # Earth gravity
        self.day_length = 0  # Hours
        self.year_days = 0
        self.eccentricity = 0
        self.perihelium = 0  # AU (astronomical unit)
        self.aphelium = 0  # AE AU (astronomical unit)
        self.angle = 0  # degrees
        self.max_day_temp = 0  # Degrees Celsius
        self.min_day_temp = 0  # Degrees Celsius
        self.max_summer_temp = 0  # Degrees Celsius
        self.min_winter_temp = 0  # Degrees Celsius
        self.star_size = 0  # Sun sizes
        self.moons = []

    def set_mass(self, mass):
        self.mass = mass

    def set_gravity(self, gravity):
        self.gravity = gravity

    def set_temperature(self, temperature):
        tp = 1.8 * temperature + 492  # Convert to Rankine
        radius = math.sqrt(self.star.luminosity / (tp / 520) ** 4)
        self.radius = radius
        self.star_size = self.star.mass**0.3333 / radius
        self.year_length = math.sqrt(radius**3 / self.star.mass)
        self.temperature = temperature
        self.__calc_temp()

    def set_day_length(self, day_length):
        self.day_length = day_length
        self.year_days = self.year_length * 8766 / day_length
        self.__calc_temp()

    def set_eccentricity(self, eccentricity):
        self.eccentricity = eccentricity
        self.perihelium = (1 - eccentricity) * self.radius
        self.aphelium = (1 + eccentricity) * self.radius
        self.__calc_year_temp()

    def set_angle(self, angle):
        self.angle = angle
        self.__calc_year_temp()

    def add_moon(self, moon):
        self.moons.append(moon)

    def __calc_temp(self):
        # Algorithm in Rankine
        self.max_day_temp = ((1 + 0.025 * self.day_length / 24) * (1.8 * self.temperature + 492) - 492) / 1.8
        self.min_day_temp = ((1 - 0.025 * self.day_length / 24) * (1.8 * self.temperature + 492) - 492) / 1.8
        if self.min_day_temp < -273:
            self.min_day_temp = -273
        self.__calc_year_temp()

    def __calc_year_temp(self):
        self.max_summer_temp = self.max_day_temp + 1.0556 * self.angle * (1 + self.eccentricity)**2
        self.min_winter_temp = self.min_day_temp - 1.0556 * self.angle / (1 + self.eccentricity)**2
        if self.min_winter_temp < -273:
            self.min_winter_temp = -273

    def climate(self):
        txt = []
        line = f"Een dag duurt op deze planeet ongeveer {self.day_length:.2f} uur. "
        line += f"Een jaar duurt {self.year_days:.1f} dagen."
        txt.append(line)
        line = "De hoek van de rotatie-as heeft de volgende invloeden op het klimaat: "
        line += f"De maximumtemperatuur is vandaag {self.max_day_temp:.0f} graden C. "
        line += f"Vannacht zal de temperatuur dalen tot {self.min_day_temp:.0f} graden C."
        txt.append(line)
        line = f"'s Zomers kan de temperatuur stijgen tot {self.max_summer_temp:.0f} graden C. "
        line += f"'s Winters verwachten we een minium van {self.min_winter_temp:.0f} graden C."
        if self.max_summer_temp <= 0 or self.min_winter_temp >= 80:
            line += " Er zijn perioden waarin geen vloeibaar water kan bestaan."
        txt.append(line)
        return txt
