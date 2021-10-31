import sys
from turtle import Turtle


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


def l_system(axiom, rules, iterations=7):
    current_var = axiom
    for _ in range(iterations):
        current_var = iteration(current_var, rules)

    return current_var


def draw_example_1(variable):
    turtle = Turtle()
    turtle.speed("fastest")
    turtle.left(90)
    turtle.up()
    turtle.setposition(0, -300)
    turtle.down()

    stack = []

    for char in variable:
        if char == "0":
            turtle.forward(2)
        elif char == "1":
            turtle.forward(2)
        elif char == "[":
            stack.append((turtle.pos(), turtle.heading()))
            turtle.left(45)
        elif char == "]":
            pos, angle = stack.pop()
            turtle.up()
            turtle.setposition(pos[0], pos[1])
            turtle.setheading(angle)
            turtle.down()
            turtle.right(45)
    input()


def draw_example_2(variable):
    turtle = Turtle()
    turtle.speed("fastest")
    turtle.getscreen().tracer(0, 0)
    turtle.up()
    turtle.setposition(-300, -300)
    turtle.down()

    for char in variable:
        if char == "F":
            turtle.forward(10)
        elif char == "+":
            turtle.left(90)
        elif char == "-":
            turtle.right(90)

    turtle.getscreen().update()
    input()


def draw_example_3(variable):
    turtle = Turtle()
    turtle.left(60)
    turtle.speed("fastest")
    turtle.getscreen().tracer(0, 0)
    turtle.up()
    turtle.setposition(-300, -300)
    turtle.down()

    stack = []

    for char in variable:
        if char == "F":
            turtle.forward(2.2)
        elif char == "+":
            turtle.left(25)
        elif char == "-":
            turtle.right(25)
        elif char == "[":
            stack.append((turtle.pos(), turtle.heading()))
        elif char == "]":
            pos, angle = stack.pop()
            turtle.up()
            turtle.setposition(pos[0], pos[1])
            turtle.setheading(angle)
            turtle.down()

    turtle.getscreen().update()

    input()

def draw_example_4(variable):
    turtle = Turtle()
    turtle.speed("fastest")
    turtle.left(90)

    stack = []

    for char in variable:
        if char == "f":
            turtle.forward(10)
        elif char == "L":
            turtle.forward(10)
        elif char == "[":
            stack.append((turtle.pos(), turtle.heading()))
        elif char == "]":
            pos, angle = stack.pop()
            turtle.up()
            turtle.setposition(pos[0], pos[1])
            turtle.setheading(angle)
            turtle.down()
        elif char == "r":
            turtle.right(60)
        elif char == "l":
            turtle.left(60)
    input()

def main():
    examples = [("A", [("A", "AB"), ("B", "A")]),
                ("0", [("1", "11"), ("0", "1[0]0")], draw_example_1),
                ("F", [("F", "F+F-F-F+F")], draw_example_2),
                ("X", [("X", "F+[[X]-X]-F[-FX]+X"), ("F", "FF")], draw_example_3),
                ("L", [("L", "f[rL]lL")], draw_example_4)]

    example = 1
    if len(sys.argv) > 1:
        example = int(sys.argv[1])

    lsystem = examples[example - 1]

    result = l_system(lsystem[0], lsystem[1])
    print(result)

    if len(lsystem) > 2:
        lsystem[2](result)


main()