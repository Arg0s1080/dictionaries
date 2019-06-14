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
