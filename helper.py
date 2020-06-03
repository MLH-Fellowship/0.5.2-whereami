from functools import reduce

from mappings import map


def two_to_word(code: str):
    return map[code]


def olc_to_phrase(olc: str):
    code = olc[:-4]
    # Split string into array of 2 char elements.
    char_arr = [code[i: i+2] for i in range(0, len(code), 2)]
    # Convert coded array to word phrase.
    return reduce(lambda acc, s: acc + "." + two_to_word(s), char_arr, "")[1:]
