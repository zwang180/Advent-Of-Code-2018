def parse(input):
    return map(lambda str: str.strip(), input.split('\n'))

def parse_to_int(input):
    return map(lambda str: int(str), parse(input))
