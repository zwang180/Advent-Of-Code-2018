from utils.parse import parse
from itertools import product

def return_if_equal(l, r, getter, default):
    l_attr = getter(l)
    r_attr = getter(r)
    return l_attr if l_attr == r_attr else default

def generate_all_product(ids):
    return product(ids, repeat=2)

def find_match_chars(l, r):
    length = return_if_equal(l, r, lambda val: len(val), 0)
    expect_length = length - 1

    # will work since each each elem is str already
    matches = ''.join(map(lambda chars: return_if_equal(chars[0], chars[1], lambda char: char, ''), zip(l, r)))
    return matches if len(matches) == expect_length else None

def get_correct_common(input):
    for l, r in generate_all_product(parse(input)):
        matches = find_match_chars(l, r)
        if matches:
            return matches
