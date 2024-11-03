#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
## Stellar classification
Most stars are currently classified under the Morgan–Keenan (MK) system.
Each star is assigned a spectral class (a letter) from the older Harvard
spectral classification and a luminosity class using Roman numerals,
forming the star's spectral type.

The Harvard system is a one-dimensional classification scheme. Stars are
grouped according to their spectral characteristics by single letters of
the alphabet, optionally with numeric subdivisions. The O-B-A-F-G-K-M
spectral sequence is actually a sequence in temperature from the hottest
(O type) to the coolest (M type). Each letter class is then subdivided
using a numeric digit with 0 being hottest and 9 being coolest. Fractional
numbers are allowed.
The sequence has been expanded with classes for other stars and star-like
objects that do not fit in the classical system, such as class D for white
dwarfs and classes S and C for carbon stars.

In the MK system, a luminosity class is added to the spectral class using
Roman numerals:

    Luminosity class  Description
    --------------------------------------------------------
    0 or Ia+          hypergiants or
                      extremely luminous supergiants
    Ia                luminous supergiants
    Iab               intermediate-size luminous supergiants
    Ib                less luminous supergiants
    II                bright giants
    III               normal giants
    IV                subgiants
    V                 main-sequence stars (dwarfs)
    sd (or VI)        subdwarfs
    D (or VII)        white dwarfs

Additional nomenclature, in the form of lower-case letters, can follow the
spectral type to indicate peculiar features of the spectrum.

Other modern stellar classification systems, such as the UBV system, are
based on color indices—the measured differences in three or more color
magnitudes. Those numbers are given labels such as "U−V" or "B−V", which
represent the colors passed by two standard filters (e.g. Ultraviolet,
Blue and Visual)

Source: https://en.wikipedia.org/wiki/Stellar_classification
"""


class InvalidSpectralType(Exception):
    def __init__(self, message):
        self.message = message


class SpectralType:
    class_letters = ['O', 'B', 'A', 'F', 'G', 'K', 'M']
    class_mass = [100, 17, 3.2, 1.54, 1.02, 0.75, 0.38, 0.0]
    class_colors = ["blue", "pale blue", "white", "pale yellow", "yellow", "orange", "red", "red"]
    class_kleuren = ["blauw", "licht blauw", "wit", "licht geel", "geel", "oranje", "rood", "rood"]

    @classmethod
    def type_from_mass(cls, mass):
        if mass >= cls.class_mass[0]:
            return SpectralType("A0")
        index = 1
        while mass <= cls.class_mass[index]:
            index = index + 1
        class_mass = cls.class_mass[index - 1]
        next_class_mass = cls.class_mass[index]
        sub = int(((class_mass - mass) / (class_mass - next_class_mass)) * 10)
        return SpectralType(f"{cls.class_letters[index - 1]}{sub}")

    def __init__(self, spectral_type):
        """Parse a stellar classification string. Throw InvalidSpectralType if invalid."""
        if spectral_type is None or len(spectral_type) < 1:
            raise InvalidSpectralType("No spectral type")
        self.spectral_class = spectral_type[0].upper()
        if self.spectral_class not in self.class_letters:
            raise InvalidSpectralType(f"Invalid spectral class '{self.spectral_class}'")
        if len(spectral_type) < 2:
            raise InvalidSpectralType("Missing spectral class subdivision")
        if not spectral_type[1].isdigit():
            raise InvalidSpectralType(f"Invalid spectral class subdivision '{spectral_type[1]}'")
        self.class_subdivision = int(spectral_type[1])
        self.luminosity_class = ''
        self.nomenclature = ''
        additions = spectral_type[2:]
        if len(additions) > 0:
            if additions[0] == '.':
                if len(additions) < 2:
                    raise InvalidSpectralType("Missing spectral class subdivision fraction")
                if not additions[1].isdigit():
                    raise InvalidSpectralType(f"Invalid spectral class subdivision fraction '{additions[1]}'")
                self.class_subdivision += float(additions[1]) / 10
                additions = additions[2:]
            if len(additions) > 0:
                if additions[:3] in ['Ia+', 'Iab', 'III', 'VII']:
                    self.luminosity_class = additions[:3]
                    self.nomenclature = additions[3:]
                else:
                    if additions[:2] in ['Ia', 'Ib', 'II', 'IV', 'sd', 'VI']:
                        self.luminosity_class = additions[:2]
                        self.nomenclature = additions[2:]
                    else:
                        if additions[0] in ['0', 'V', 'D']:
                            self.luminosity_class = additions[0]
                            self.nomenclature = additions[1:]
                        else:
                            raise InvalidSpectralType(f"Invalid luminosity class / addition '{additions}'")
        self.spectral_type = f"{self.spectral_class}{self.class_subdivision}{self.luminosity_class}{self.nomenclature}"

    def mass(self):
        index = self.class_letters.index(self.spectral_class)
        return (self.class_mass[index] -
                self.class_subdivision * (self.class_mass[index] - self.class_mass[index + 1]) / 10)

    def color(self):
        index = self.class_letters.index(self.spectral_class)
        if self.class_subdivision < 2.5:
            return [self.class_colors[index]]
        if self.class_subdivision > 7.5 or self.spectral_class == 'M':
            return [self.class_colors[index + 1]]
        return [self.class_colors[index], self.class_colors[index + 1]]

    def kleur(self):
        index = self.class_letters.index(self.spectral_class)
        if self.class_subdivision < 2.5:
            return [self.class_kleuren[index]]
        if self.class_subdivision > 7.5 or self.spectral_class == 'M':
            return [self.class_kleuren[index + 1]]
        return [self.class_kleuren[index], self.class_kleuren[index + 1]]


def test_spectral_type(spectral_type):
    try:
        st = SpectralType(spectral_type)
        print(f"Spectral type: {spectral_type} -> {st.spectral_type}")
        print(f"  - class       : {st.spectral_class}")
        print(f"  - subdivision : {st.class_subdivision}")
        print(f"  - luminosity  : {st.luminosity_class}")
        print(f"  - nomenclature: {st.nomenclature}")
        print(f"  - mass        : {st.mass()}")
        print(f"  - color       : {st.color()}")
        print(f"  - kleur       : {st.kleur()}")
    except InvalidSpectralType as e:
        print(f"InvalidSpectralType: {e.message} ({spectral_type})")


def test_type_from_pass(mass):
    print(f"Mass {mass} --> {SpectralType.type_from_mass(mass).spectral_type}")


if __name__ == '__main__':
    test_spectral_type(None)
    test_spectral_type("")
    test_spectral_type("Q")
    test_spectral_type("k")
    test_spectral_type("km")
    test_spectral_type("g2")
    test_spectral_type("g5")
    test_spectral_type("g8")
    test_spectral_type("m3.")
    test_spectral_type("g3.b")
    test_spectral_type("O3.5")
    test_spectral_type("g2Q")
    test_spectral_type("g2Ia")
    test_spectral_type("g2Ia+")
    test_spectral_type("g2Iab")
    test_spectral_type("g2Ib")
    test_spectral_type("g2Ic")
    test_spectral_type("g2IIc")
    test_spectral_type("g2V")
    test_spectral_type("B0.5III")
    test_spectral_type("M4.0V")
    test_spectral_type("K0III")
    test_spectral_type("k3sd")
    test_spectral_type("B1.5Vnne")

    print("")
    test_type_from_pass(110)
    test_type_from_pass(90)
    test_type_from_pass(20)
    test_type_from_pass(17)
    test_type_from_pass(3.3)
    test_type_from_pass(1)
    test_type_from_pass(0.2)
    test_type_from_pass(0.1)
