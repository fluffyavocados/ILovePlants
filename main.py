import sys


def iteration(variable, rules):
    result = ""

    for char in variable:
        found_rule = False
        for rule in rules:
            if rule[0] == char:
                result += rule[1]
                found_rule = True
                break

        if not found_rule:
            result += char

    return result


def l_system(axiom, rules, iterations=10):
    current_var = axiom
    for _ in range(iterations):
        current_var = iteration(current_var, rules)

    return current_var


def main():
    examples = [("A", [("A", "AB"), ("B", "A")]),
                ("0", [("1", "11"), ("0", "1[0]0")])]

    example = 1
    if len(sys.argv) > 1:
        example = int(sys.argv[1])

    lsystem = examples[example - 1]

    print(l_system(lsystem[0], lsystem[1]))


main()

# print(l_system("A", [("A", "AB"), ("B", "A")], 7))
