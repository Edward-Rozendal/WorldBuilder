#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
## temperature - mass relation
Temp in Kelvin = 6000 * mass^0.35
Where is surface-temperature mass relation based on?
6000 Kelvin is approximately the surface temperature of the sun.


## planet probability for planets
 Where is dependency on spectral type for planet probability base on?
"""

from spectral_type import SpectralType


class Star:
    def __init__(self, name):
        self.name = name
        self.spectral_type = None
        self.mass = 0  # Sol masses
        self.luminosity = 0  # Relative to sol luminosity
        self.lifespan = 0  # Billion years
        self.life_fraction = 0  # 0.00 - 1.00

    def temperature(self):
        return 6000 * self.mass ** 0.35

    def description(self):
        txt = []
        line = f"De gekozen ster, {self.name} is een {self.spectral_type.spectral_type} ster."
        txt.append(line)
        color = self.spectral_type.kleur()
        if len(color) == 2:
            line = f"Ze heeft een kleur tussen {color[0]} en {color[1]}"
        else:
            line = f"Ze is {color[0]} van kleur"
        line += f" en haar massa is {self.mass + 0.005:.2f} zonmassa's."
        line += f" Ze is {self.luminosity:.2f} maal zo helder als de zon."
        txt.append(line)
        line = f"Haar verwachte levensduur is {self.lifespan:.2f} miljard jaar"
        line += f" waarvan {self.life_fraction * 100:.0f}% of ongeveer {self.lifespan * self.life_fraction:.2f}"
        line += " miljard jaar zijn verstreken."
        if self.life_fraction > 0.95:
            line += f" {self.name} ligt op haar sterfbed."
        txt.append(line)
        line = f"Ze heeft een oppervlaktetemperatuur van {self.temperature():.0f} Kelvin."
        index = SpectralType.class_letters.index(self.spectral_type.spectral_class)
        if 2.5 < index + 1 + self.spectral_type.class_subdivision / 10 < 7:
            line += " Ze heeft mogelijk een planetenstelsel."
        else:
            line += " Ze heeft waarschijnlijk geen planetenstelsel."
        line += f" {self.name} zal sterven als een"
        if self.mass < 1.5:
            line += " witte dwerg."
        elif self.mass < 10:
            line += " neutronster na een supernove-explosie."
        else:
            line += " zwart gat na een supernova-explosie."
        txt.append(line)
        return txt
