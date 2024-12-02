def split_input_into_lists(input: str) -> list[list[int]]:
    # first split line by newline character
    lines = input.split("\n")
    res: list[list[int]] = []
    for line in lines:
        res.append(list(map(int, line.split(" "))))
    return res


def is_line_valid(line: list[int], dampner_enabled: bool) -> bool:
    if line[0] > line[1]:
        line = list(reversed(line))
    
    should_fail = False
    # now check if line is valid
    for i in range(len(line) - 1):
        if line[i] >= line[i + 1]:
            should_fail = True
            break
        if abs(line[i] - line[i + 1]) > 3:
            should_fail = True
            break

    if should_fail and not dampner_enabled:
        return False
    
    # if dampner is switched on,
    # rerun the function again for all possible removals
    if should_fail and dampner_enabled:
        for i in range(len(line)):
            newline = line.copy()
            newline.pop(i)
            if is_line_valid(newline, False):
                # found a removal that makes the line valid
                return True
        return False

    # if we get here, the line is valid
    return True

def solve_part_one(input: str) -> int:
    lines = split_input_into_lists(input)

    res = 0
    for line in lines:
        if is_line_valid(line, False):
            res += 1
    return res

def solve_part_two(input: str) -> int:
    lines = split_input_into_lists(input)
    res = 0
    for line in lines:
        if is_line_valid(line, True):
            res += 1
    return res

txt_input = open("input.txt").read()
print("part one:", solve_part_one(txt_input))
print("part two:", solve_part_two(txt_input))