from functools import reduce

from whereamigeo.mappings import map, word_to_plus_code_mapping


sep = '.'


def get_word(code: str):
    return map[code]


def get_code(word: str):
    return word_to_plus_code_mapping[word]


def get_olc_array(olc: str, inc: int):
    code = olc.replace('+', '')
    return [code[i: i+inc] for i in range(0, len(code), inc)]


def single_char_phrase(olc: str):
    char_arr = get_olc_array(olc, 1)
    return reduce(lambda acc, s: acc + sep + get_word(s), char_arr, '')[1:]


def double_char_phrase(olc: str):
    # Split string into array of 2 char elements.
    char_arr = get_olc_array(olc, 2)
    # Convert coded array to word phrase.
    return reduce(lambda acc, s: acc + sep + get_word(s), char_arr, '')[1:]


def olc_to_phrase(olc: str, single: bool = False):
    if single:
        return single_char_phrase(olc)
    else:
        return double_char_phrase(olc)


def phrase_to_olc(phrase: str):
    word_arr = phrase.split(sep)
    code_arr = [get_code(word_arr[w]) for w in range(0, len(word_arr))]
    code = reduce(lambda acc, c: acc + c, code_arr, '')
    if len(code) % 2 == 0:
        return code[:-2] + '+' + code[-2:]
    return code[:-3] + '+' + code[-3:]
