import re
# https://regex101.com/r/UUIbWI/1
regex_mul_only = re.compile("mul\([0-9]{1,3},[0-9]{1,3}\)")
regex_all = re.compile("mul\([0-9]{1,3},[0-9]{1,3}\)|don't\(\)|do\(\)")


def find_matches(input: str, mul_only: bool) -> list[str]:
    if mul_only:
        return re.findall(regex_mul_only, input)
    else:
        return re.findall(regex_all, input)


def complete_multiplicaton(mul_string: str) -> int:
    parts = mul_string.strip("mul()").split(",")
    return int(parts[0]) * int(parts[1])


def strip_mul_input_by_do_dont(input: list[str]) -> list[str]:
    should_strip = False
    res: list[str] = []
    DO = "do()"
    DONT = "don't()"
    for instruction in input:
        if instruction == DO:
            should_strip = False
            continue
        elif instruction == DONT:
            should_strip = True
            continue
        if not should_strip:
            res.append(instruction)
    return res


def solve_part_one(input: str) -> int:
    matches = find_matches(input, True)
    return sum(list(map(complete_multiplicaton, matches)))


def solve_part_two(input: str) -> int:
    matches = find_matches(input, False)
    matches = strip_mul_input_by_do_dont(matches)
    return sum(list(map(complete_multiplicaton, matches)))


txt_input = open("input.txt").read()
print("Part one:", solve_part_one(txt_input))
print("Part two:", solve_part_two(txt_input))
