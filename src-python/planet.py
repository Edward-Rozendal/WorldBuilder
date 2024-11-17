#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


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

    def set_radius(self, radius):
        self.radius = radius
        ds = self.star.mass**0.3333
        self.star_size = ds / radius
        self.year_length = math.sqrt(radius**3 / self.star.mass)

    def set_mass(self, mass):
        self.mass = mass

    def set_gravity(self, gravity):
        self.gravity = gravity

    def set_temperature(self, temperature):
        self.temperature = temperature
        self.__calc_temp()

    def set_day_length(self, day_length):
        self.day_length = day_length
        self.year_days = int(87660 / day_length * self.year_length + .5) / 10
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
