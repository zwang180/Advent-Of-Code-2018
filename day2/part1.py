from utils.parse import parse
from collections import Counter
from functools import reduce

COUNT_TWO = 2
COUNT_THREE = 3

def get_letter_counts(id):
    return Counter(id).values()

def get_two_three_count(id):
    letter_counts = get_letter_counts(id)

    two_count, three_count = 0, 0
    if COUNT_TWO in letter_counts:
        two_count = 1

    if COUNT_THREE in letter_counts:
        three_count = 1

    return two_count, three_count

def calculate_checksum(input):
    two_sum, three_sum = reduce(lambda acc, val: (acc[0] + val[0], acc[1] + val[1]), map(get_two_three_count, parse(input)), (0, 0))
    return two_sum * three_sum
