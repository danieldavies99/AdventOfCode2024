import re

regex_xmas = re.compile("(?=(XMAS|SAMX))")
regex_mas = re.compile("(?=(MAS|SAM))")


def get_all_horizontal_lines(input: str) -> list[str]:
    return [line for line in input.split("\n")]


def get_all_vertical_lines(horizontal_lines: list[str]) -> list:

    vertical_lines = []
    for i in range(len(horizontal_lines[0])):
        vertical_lines.append("".join([line[i] for line in horizontal_lines]))

    return vertical_lines


def get_diagonal_lines_left_to_right(vertical_lines: list[str]) -> list:
    diagonal_lines = []

    # top left quad
    total_length = len(vertical_lines[0])
    for i in range(total_length):
        current_line = []
        for j in range(i + 1):
            current_line.append(vertical_lines[j][i-j])
        diagonal_lines.append("".join(current_line))

    # bottom right quad
    for i in range(total_length - 1):
        current_line = []
        for j in range(i + 1):
            current_line.append(
                vertical_lines[total_length - 1 - j][total_length - 1 - i + j])
        diagonal_lines.append("".join(current_line))

    return diagonal_lines


def get_diagonal_lines_right_to_left(vertical_lines: list[str]) -> list:
    diagonal_lines = []

    # bottom left quad
    total_length = len(vertical_lines[0])

    for i in range(total_length):
        current_line = []
        for j in range(i + 1):
            current_line.append(vertical_lines[j][total_length - 1 - i + j])
        diagonal_lines.append("".join(current_line))

    # top right quad
    for i in range(total_length - 1):
        current_line = []
        for j in range(i + 1):
            current_line.append(vertical_lines[total_length - 1 - j][i-j])
        diagonal_lines.append("".join(current_line))
    return diagonal_lines


def get_all_diagonal_lines(vertical_lines: list[str]) -> list:
    return get_diagonal_lines_left_to_right(vertical_lines) + get_diagonal_lines_right_to_left(vertical_lines)


def get_char_at(x: int, y: int, vertical_lines: list[str]) -> str:
    if x >= len(vertical_lines) or y >= len(vertical_lines) or x < 0 or y < 0:
        # tried to get  a character out of bounds
        return ""
    return vertical_lines[x][y]


def solve_part_one(input: str) -> int:
    horizontal_lines = get_all_horizontal_lines(input)
    vertical_lines = get_all_vertical_lines(horizontal_lines)
    diagonal_lines = get_all_diagonal_lines(vertical_lines)
    all_lines = horizontal_lines + vertical_lines + diagonal_lines
    sum = 0
    for line in all_lines:
        sum += len(regex_xmas.findall(line))
    return sum


def solve_part_two(input: str) -> int:
    horizontal_lines = get_all_horizontal_lines(input)
    vertical_lines = get_all_vertical_lines(horizontal_lines)

    sum = 0
    for y in range(len(vertical_lines)):
        for x in range(len(vertical_lines)):
            if get_char_at(x, y, vertical_lines) == "A":  # found candidate
                top_left = get_char_at(x - 1, y - 1, vertical_lines)
                top_right = get_char_at(x + 1, y - 1, vertical_lines)
                bottom_left = get_char_at(x - 1, y + 1, vertical_lines)
                bottom_right = get_char_at(x + 1, y + 1, vertical_lines)
                if (
                    ((top_left == "M" and bottom_right == "S") or (
                        top_left == "S" and bottom_right == "M"))
                    and
                    ((top_right == "M" and bottom_left == "S") or (
                        top_right == "S" and bottom_left == "M"))
                ):
                    sum += 1
    return sum


txt_input = open("input.txt").read()
print("Part one:", solve_part_one(txt_input))
print("Part two:", solve_part_two(txt_input))
