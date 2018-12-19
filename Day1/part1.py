def parse(input):
    return map(lambda str: int(str), input.split('\n'))

def calculate_sum(input):
    return sum(parse(input))
