def split_input_into_lists(input: str) -> tuple[list[int], list[int]]:
    # first split line by newline character
    lines = input.split("\n")
    # then split each line by "   " and assign to list
    list1: list[int] = []
    list2: list[int] = []
    for line in lines:
        list1.append(int(line.split("   ")[0]))
        list2.append(int(line.split("   ")[1]))
    return list1, list2

def sort_lists(list1: list[int], list2: list[int]) -> tuple[list[int], list[int]]:
    # sort each list from smallest to largest
    list1.sort()
    list2.sort()
    return list1, list2

def compare_list_difference(list1: list[int], list2: list[int]) -> int:
    res = 0
    for i in range(len(list1)):
        res += abs(list1[i] - list2[i])
    return res


def solve_part_one(input: str) -> int:#
    list1, list2 = split_input_into_lists(input)
    list1, list2 = sort_lists(list1, list2)
    res = compare_list_difference(list1, list2)
    return res

def count_instances(search: int, list: list[int]) -> int:
    res = 0
    for i in list:
        if i == search:
            res += 1
        if i > search: # our lists are ordered, so we can stop here
            break
    return res

def solve_part_two(input: str) -> int:#
    list1, list2 = split_input_into_lists(input)
    list1, list2 = sort_lists(list1, list2)

    res = 0
    for i in list1:
        res += i * count_instances(i, list2)
    return res


txt_input = open("input.txt").read()
print("part one:",solve_part_one(txt_input))
print("part two:",solve_part_two(txt_input))
