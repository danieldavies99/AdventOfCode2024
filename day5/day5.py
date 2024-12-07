from dataclasses import dataclass

@dataclass
class Rule:
    x: int
    y: int

def get_update_rules(input: str) -> list[Rule]:
    parts = input.split("\n\n")
    update_rules_string = parts[0]
    update_rules = update_rules_string.split("\n")
    rules: list[Rule] = []
    for rule in update_rules:
        parts = rule.split("|")
        rules.append(Rule(int(parts[0]), int(parts[1])))
    return rules

def get_updates (input: str) -> list[list[int]]:
    parts = input.split("\n\n")
    updates_string = parts[1]
    updates = updates_string.split("\n")
    res: list[list[int]] = []
    for update in updates:
        res.append(list(map(int, update.split(","))))
    return res

def rule_applies(rule: Rule, update: list[int]) -> bool:
    if rule.x in update and rule.y in update:
        return True
    return False

def rule_passes(rule: Rule, update: list[int]) -> bool:
    x_index = update.index(rule.x)
    y_index = update.index(rule.y)
    return x_index < y_index

def all_rules_pass(rules: list[Rule], update: list[int]) -> bool:
    for rule in rules:
        if not rule_applies(rule, update):
            continue
        if not rule_passes(rule, update):
            return False
    return True


def get_middle_number(update: list[int]) -> int:
    return update[len(update) // 2]

def order_update(update: list[int], rules: list[Rule]) -> list[int]:
    # order update based on rules, rules.x should come at some point before rules.y in the update
    
    while not all_rules_pass(rules, update):
        for rule in rules:
            if not rule_applies(rule, update):
                continue
            x_index = update.index(rule.x)
            y_index = update.index(rule.y)
            if x_index > y_index:
                # swap x and y
                update[x_index], update[y_index] = update[y_index], update[x_index]
    return update

def solve_part_one(input: str) -> int:
    rules = get_update_rules(input)
    updates = get_updates(input)

    res = 0
    for update in updates:
        if all_rules_pass(rules, update):
            middle_number = get_middle_number(update)
            print("update passes:", update, "middle number:", middle_number)
            res += middle_number
    return res

def solve_part_two(input: str) -> int:
    rules = get_update_rules(input)
    updates = get_updates(input)

    res = 0
    for update in updates:
        if not all_rules_pass(rules, update):
            update = order_update(update, rules)
            middle_number = get_middle_number(update)
            print("update doesn't pass:", update, "middle number:", middle_number)
            res += middle_number
    return res


txt_input = open("input.txt").read()
print("Part one:", solve_part_one(txt_input))
print("Part two:", solve_part_two(txt_input))