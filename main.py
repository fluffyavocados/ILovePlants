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


print(l_system("A", [("A", "AB"), ("B", "A")], 7))
