from part1 import parse
from itertools import cycle

def get_first_duplicate(input):
    freq = 0
    freq_memory = { freq: freq}

    all_changes = parse(input)
    for change in cycle(all_changes):
        freq += change
        if freq in freq_memory:
            return freq
        else:
            freq_memory[freq] = change
