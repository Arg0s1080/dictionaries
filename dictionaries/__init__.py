# /usr/bin/python3
# -*- coding: UTF-8 -*-

# GNU General Public License v3.0
#
# Permissions of this strong copyleft license are conditioned on making available
# complete source code of licensed works and modifications, which include larger works
# using a licensed work, under the same license. Copyright and license notices must be
# preserved. Contributors provide an express grant of patent rights.
#
# For more information on this, and how to apply and follow theGNU GPL, see:
# http://www.gnu.org/licenses
#
# (ɔ) Iván Rincón 2019


def arabic() -> dict:
    from .arabic import transliteration
    return transliteration


def cyrillic() -> dict:
    from .cyrillic import transliteration
    return transliteration


def cyrillic_belarussian() -> dict:
    from .cyrillic_belarussian import transliteration
    return transliteration


def cyrillic_bulgarian() -> dict:
    from .cyrillic_bulgarian import transliteration
    return transliteration


def cyrillic_macedonian() -> dict:
    from .cyrillic_macedonian import transliteration
    return transliteration


def cyrillic_serbian() -> dict:
    from .cyrillic_serbian import transliteration
    return transliteration


def cyrillic_ukrainian() -> dict:
    from .cyrillic_ukrainian import transliteration
    return transliteration


def greek() -> dict:
    from .greek import transliteration
    return transliteration


def latin_based() -> dict:
    from dictionaries.latin_based import transliteration
    return transliteration
