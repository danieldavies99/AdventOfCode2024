from dataclasses import dataclass
from enum import Enum


class Operation(Enum):
    ADD = 1
    MULTIPLY = 2
    CONCAT = 3


@dataclass
class Equation:
    result: int
    arguments: list[int]


def parse_input(input: str) -> list[Equation]:
    lines = input.split("\n")
    equations: list[Equation] = []
    for line in lines:
        parts = line.split(": ")
        new_equation = Equation(int(parts[0]), list(
            map(int, parts[1].split(" "))))
        equations.append(new_equation)
    return equations


def can_solve(equation: Equation, allowed_operations: list[Operation]) -> bool:
    current_possible_values: list[int] = [equation.arguments[0]]
    for i in range(len(equation.arguments) - 1):
        new_values = []
        for operation in allowed_operations:
            current_values_copy = current_possible_values.copy()
            if operation == Operation.ADD:
                for v in current_values_copy:
                    # print("adding", v, equation.arguments[i + 1])
                    new_values.append(v + equation.arguments[i + 1])
            elif operation == Operation.MULTIPLY:
                for v in current_values_copy:
                    # print("multiplying", v, equation.arguments[i + 1], )
                    new_values.append(v * equation.arguments[i + 1])
            elif operation == Operation.CONCAT:
                for v in current_values_copy:
                    # print("concatenating", v, equation.arguments[i + 1], int(str(v) + str(equation.arguments[i + 1])))
                    new_values.append(
                        int(str(v) + str(equation.arguments[i + 1])))
        current_possible_values = new_values
    # print(current_possible_values)
    return equation.result in current_possible_values


def solve_part_one(input: str) -> int:
    equations = parse_input(input)
    res = 0
    for equation in equations:
        if can_solve(equation, [Operation.ADD, Operation.MULTIPLY]):
            res += equation.result
    return res


def solve_part_two(input: str) -> int:
    equations = parse_input(input)
    res = 0
    for equation in equations:
        if can_solve(equation, [Operation.ADD, Operation.MULTIPLY, Operation.CONCAT]):
            res += equation.result
    return res


txt_input = open("input.txt").read()

print("Part one:", solve_part_one(txt_input))
print("Part two:", solve_part_two(txt_input))
