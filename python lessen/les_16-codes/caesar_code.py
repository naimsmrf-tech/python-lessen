"""
Past een Caeser substitutiecode toe, die elke letter een aantal posities in het alfabet verschuift.

Bijvoorbeeld, als we verschuiven met 5, wordt de letter "A" "F" en "X" wordt "C".
"""

def encrypt(bericht, sleutel):
    """Returned de gegeven boodschap versleuteld met een Caesar code."""
    return pas_code_toe(bericht, sleutel)

def decrypt(bericht, sleutel):
    """Returned de gegeven boodschap ontsleuteld met een Caesar code."""
    return pas_code_toe(bericht, -sleutel)

def pas_code_toe(bericht, schift):
    """Returned het bericht alfabetisch verschoven met het gegeven aantal posities."""
    nieuw_bericht = ""
    for karakter in bericht:
        nieuw_bericht += schift_karakter(karakter, schift)

    return nieuw_bericht

def schift_karakter(karakter, schift):
    """Returned de letter alfabetisch verschoven met het gegeven aantal posities."""
    alfabet = "abcdefghijklmnopqrstuvwxyz"

    # nummers, symbolen en witruimte karakters blijven hetzelfde.
    if karakter.lower() not in alfabet:
        return karakter

    # Vind het karakter dat verschoven is.
    nieuwe_index = alfabet.index(karakter.lower()) + schift
    verschoven_letter = alfabet[nieuwe_index % len(alfabet)]

    # Bewaar de hoofdletters.
    if karakter.isupper():
        verschoven_letter = verschoven_letter.upper()

    return verschoven_letter
