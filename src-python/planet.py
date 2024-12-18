#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
## Star appearance
The appearance of a star, how big it looks, depends on both its diameter and distance.
Assuming each star has the same mass density, the diameter relative to the Sun depends
equally to their mass as their volume. The volume of a sphere is: 
    V = 4/3 * pi * r^3
Given that the size in inversely proportional to its distance (the planets radius),
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


## Temperature
The program originally uses temperatures in Fahrenheit and Rankine
Conversions to Celsius and Kelvin:
- Tk = (Tf + 459 ) * (5/9)
- Tc = (Tf - 32) * (5/9)
- Tf = Tc * (5/9) + 32
- Tk = Tr * (5/9)
- Tc = Tr * (5/9) - 273
- Tr = Tk * (9/5)
- Tr = (Tc + 273) * (9/5) = 1.8 * Tc + 492


## Radius
The temperature of the planet will be about:
    T = 273 * ( (1-A)*L / D^2 )^0.25
A is the reflectivity (albedo) of the planet,
L is the luminosity of its star in multiples of the sun's power
D is the distance between the planet and the star in Astronomical Units (AU),
The resulting temperature will be in units of Kelvins.
Albedo (A) depends on the surface material:
    Material    Example     Albedo (A)
    Basalt      Moon        0.06
    Iron Oxide  Mars        0.16
    Water+Land  Earth       0.40
    Gas         Jupiter     0.70 
source: https://spacemath.gsfc.nasa.gov/weekly/6Page61.pdf

When calculating the temperature for Earth (A=0.40, L=1, D=1), the result is
240K (-32 Celsius). That is because no greenhouse effect is taken into account.
For a calculation with greenhouse effect, see:
https://astro.sitehost.iu.edu/ala/PlanetTemp/index.html

The program uses the formula to calculate the distance for a given temperature:
    D = sqrt( (273^4 * (1-A)*L) / T^4 )
    D = sqrt( (1-A)*L) / (T/273)^4 )
But instead of Water+Land albedo of 0.40, it uses -0.25, probably for some
compensation for a greenhouse effect. Calculating Earths temperature with this
values gives a more realistic temperature of 288K (16 Celsius).


## Maximum and minimum day temperature
The formula used to calculate the maximum and minimum temperature are:
    max_day_temp = ((1 + 0.025 * day_length / 24) * (1.8 * temperature + 492) - 492) / 1.8
    min_day_temp = ((1 - 0.025 * day_length / 24) * (1.8 * temperature + 492) - 492) / 1.8
The calculation is in Rankine. The planet temperature and the resulting temperatures
are in degrees Celsius and therefore converted to and from Rankine.
It is unknown on what principles the formula is based on.


## Planetary habitability
The appropriate spectral range for habitable stars is considered to be "late F" or "G", to "mid-K".
Source: https://en.wikipedia.org/wiki/Planetary_habitability

The habitable zone (HZ) is the range of orbits around a star within which a planetary surface
can support liquid water given sufficient atmospheric pressure.
Published estimates for the habitable zone within the Solar System range from 0.38 to 10.0 astronomical units
though arriving at these estimates has been challenging for a variety of reasons.
Dole estimates the inner edge for the sun at 0.725 AU and the outer edge at 1.24 AU.
Source: https://en.wikipedia.org/wiki/Habitable_zone
"""

import math


class Moon:
    def __init__(self, planet, mass, radius, period):
        self.planet = planet
        self.mass = mass  # Moon masses
        self.radius = radius  # Moon = 30
        self.period = period


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
        radius = math.sqrt(((1 + 0.25) * self.star.luminosity) / math.pow((temperature + 273) / 273, 4))
        self.radius = radius
        self.star_size = math.pow(self.star.mass, 0.3333) / radius
        self.year_length = math.sqrt(math.pow(radius, 3) / self.star.mass)
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
        self.max_summer_temp = self.max_day_temp + 1.0556 * self.angle * math.pow(1 + self.eccentricity, 2)
        self.min_winter_temp = self.min_day_temp - 1.0556 * self.angle / math.pow(1 + self.eccentricity, 2)
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

    def moon_info(self, day_length):
        self.moons.sort(key=lambda x: x.radius)
        txt = ["baanstraal  massa   periode"]
        for moon in self.moons:
            txt.append(f"{moon.radius:7.1f} {moon.mass:8.2f} {moon.period / day_length:9.2f} dagen")
        return txt

    def description(self):
        txt = []
        line = f"Deze planeet heeft een gemiddelde oppervlakte temperatuur van {self.temperature:.0f} "
        line += f"graden C. Dit betekent een baanstraal van {self.radius:.2f} astronomische eenheden "
        line += f"({self.radius * 150:.1f} miljoen km.)."
        txt.append(line)
        txt.append(f"Perihelium = {self.perihelium:.2f} ae, Aphelium = {self.aphelium:.2f} ae.")
        txt.append(f"Een jaar is {self.year_length:.2f} aardjaren lang.")
        line = f"{self.star.name} lijkt "
        if self.star_size > 1.5 or self.star_size < 0.75:
            line += "veel "
        if self.star_size > 1:
            line += "groter "
        else:
            line += "kleiner "
        line += "dan onze zon."
        txt.append(line)
        if 0.95 < self.gravity < 1.05:
            txt.append("De zwaartekracht is vrijwel gelijk aan die van de aarde.")
        else:
            line = "Aangezien de zwaartekracht "
            if self.gravity > 1:
                line += "groter is dan op aarde verwachten we een dichtere atmosfeer. De tektonische "
                line += "werking is groter, maar er is ook meer weerstand. We verwachten daarom "
                line += "meer continenten en kleinere bergen; Aardbevingen komen vaker voor en zijn heviger."
            else:
                line += "kleiner is dan op aarde verwachten we een dunnere atmosfeer. Er is minder "
                line += "tektonische werking en ook de weerstand is kleiner. We verwachten "
                line += "daarom minder bergen, maar ze kunnen veel hoger worden. "
                line += "Aardbevingen, als ze al voorkomen, zullen minder hevig zijn."
            txt.append(line)
            line = f"Een zwaartekracht van {self.gravity:.2f} g betekent dat iemand van 80 kilo op deze "
            line += f"planeet {80 * self.gravity:.1f} kilo zou wegen."
            txt.append(line)
        return txt

    def life(self):
        txt = []
        inner_habitable_zone = 0.00012 * self.star.temperature()
        outer_habitable_zone = 0.06452 * math.exp(0.0005 * self.star.temperature())
        live = True
        hm = 0
        line = ""
        if self.mass < 0.055 or self.mass > 17.6:
            line += "Vanwege de slechte atmosfeer "
            live = False
        elif self.radius < inner_habitable_zone or self.radius > outer_habitable_zone:
            line += "Vanwege de afstand tot de zon "
            live = False
        elif self.max_summer_temp < 0 or self.min_winter_temp > 80:
            line += "Aangezien er nooit vloeibaar water is "
            live = False
        elif self.star.lifespan * self.star.life_fraction <= 1.5:
            line += "Aangezien de planeet te jong is "
            live = False
        elif self.star.life_fraction >= 0.95:
            line += f"Aangezien {self.star.name} op haar sterbed ligt "
            live = False
        if live:
            line = "Mogelijk zijn er "
            if self.star.lifespan * self.star.life_fraction < 2 * self.gravity:
                line += "bacterien en blauwgroene algen."
            elif self.star.lifespan * self.star.life_fraction < 3 * self.gravity:
                line += "eencelligen met een kern."
            elif self.star.lifespan * self.star.life_fraction < 4 * self.gravity:
                line += "eenvoudige meercelligen."
            elif self.star.lifespan * self.star.life_fraction <= 4.4 * self.gravity:
                line += "gewervelde waterdieren en planten op het land."
            else:
                line += "grote op het land levende dieren en misschien intelligente wezens."
                txt.append(line)
                if self.gravity >= 1.05:
                    line = "Grotere zwaartekracht betekent een dichtere atmosfeer die grote vogels "
                    line += "kan dragen. Maar zelfs een kleine val is dodelijk, zodat hoge reactiesnelheden "
                    line += "noodzakelijk zijn. In het algemeen zullen levensvormen korter "
                    line += "en steviger zijn dan op aarde."
                    if self.gravity > 1.2:
                        line += " Er zijn geen tweebenige wezens zoals wij."
                    txt.append(line)
                    line = "De dikke atmosfeer verbetert de geluidsoverdracht; daarom zullen "
                    line += "dieren meer op hun gehoor vertrouwen"
                if self.gravity < 0.95:
                    line = "Kleiner zwaartekracht betekent een dunnere atmosfeer. Vogels, als ze "
                    line += "al voorkomen, hebben grote vleugels. Alle levensvormen zullen hoger en "
                    line += "slanker gebouwd zijn dan die op aarde. Tweebenige wezens kunnen zeker voorkomen."
                    txt.append(line)
                    line = "De dunne atmosfeer bemoeilijkt geluidsoverdracht, zodat de dieren "
                    line += "grote of helemaal geen oren zullen hebben. Hun longen moeten groter zijn."
                    if self.temperature >= -230:
                        txt.append(line)
                        line = "Het leven moet zich op een of andere manier beschermen tegen het zonlicht."
                txt.append(line)
                if self.star_size < 0.75:
                    line = "Vanwege de kleine zon zullen de dieren grote ogen hebben of op "
                    line += "andere zintuigen vertrouwen."
                    txt.append(line)
                if self.star_size >= 1.5:
                    line = "Tenzij de atmosfeer veel licht tegenhoudt, zullen de dieren "
                    line += "kleine ogen hebben."
                    txt.append(line)
                if self.max_day_temp - self.min_day_temp >= 30:
                    line = "Vanwege de grote temeratuurvariaties zal het leven zich vooral ondergronds"
                    line += "en onder water bevinden."
                    txt.append(line)
                if (self.temperature < 0 or self.temperature > 30 or
                        self.gravity > 1.5 or self.gravity < 0.68 or
                        self.mass < 0.4 or self.mass > 2.35 or
                        self.day_length > 96 or
                        self.max_summer_temp > 50 or self.min_winter_temp < -35 or
                        self.max_day_temp > 45 or self.min_day_temp < -25):
                    hm = 0
                else:
                    hm = 1
        else:
            line += "zal op deze planeet waarschijnlijk geen leven zijn."
        txt.append(line)
        line = "Mensen zullen deze wereld waarschijnlijk "
        if hm == 0:
            line += "on"
        line += "geschikt vinden om te wonen."
        txt.append(line)
        return txt


def check_radius_calculation():
    print('   ', end='')
    for lum in range(3, 15, 2):
        luminosity = lum / 10
        print(f'     {luminosity:3.1f}', end='')
    print('')
    for temperature in range(6, 20, 2):
        print(f'{temperature:3}', end='')
        for lum in range(3, 15, 2):
            # Original radius calculation
            luminosity = lum / 10
            tp = 1.8 * temperature + 492  # Convert to Rankine
            radius = math.sqrt(luminosity / math.pow(tp / 520, 4))
            print(f'  {radius:6.2f}', end='')
        print('\n   ', end='')
        for lum in range(3, 15, 2):
            # Rewritten radius calculation with same outcome
            luminosity = lum / 10
            radius = math.sqrt(((1 + 0.25) * luminosity) / math.pow((temperature + 273) / 273, 4))
            print(f'  {radius:6.2f}', end='')
        print('\n   ', end='')
        for lum in range(3, 15, 2):
            # Radius calculation using formula with Water+Land albedo
            luminosity = lum / 10
            radius = math.sqrt(((1 - 0.40) * luminosity) / math.pow((temperature + 273) / 273, 4))
            print(f'  {radius:6.2f}', end='')
        print('')


if __name__ == '__main__':
    check_radius_calculation()
