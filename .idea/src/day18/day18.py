def solve_part_one(expressions):
    total_sum = 0
    for expression in expressions:
        result = solve_expression(expression)
        total_sum += int(result)
    return total_sum

def solve_part_two(expressions):
    total_sum = 0
    for expression in expressions:
        result = solve_expression_part_two(expression)
        total_sum += int(result)
    return total_sum

def solve_expression(expression):

    # first find and solve all sub_expressions
    has_sub_expression = True
    while has_sub_expression:
        has_sub_expression = False
        depth = 0
        opening = 0
        for i in range(len(expression)):
            if expression[i] == "(" and depth == 0:
                opening = i
                has_sub_expression = True
                depth = 1
            elif expression[i] == "(" and depth > 0:
                depth += 1
            elif expression[i] == ")" and depth > 1:
                depth -= 1
            elif expression[i] == ")" and depth == 1:
                depth -= 1

                sub_result = solve_expression(expression[opening + 1 :i])
                expression = expression.replace(expression[opening:i + 1], sub_result)

                break

    expression_list = expression.split(" ")

    result = int(expression_list[0])
    next_opp_add = False
    for i in expression_list[1:]:
        if i == "+":
            next_opp_add = True
        elif i == "*":
            next_opp_add = False
        else:
            if next_opp_add:
                result += int(i)
            else:
                result *= int(i)

    return "{}".format(result)

def solve_expression_part_two(expression):

    # first find and solve all sub_expressions
    has_sub_expression = True
    while has_sub_expression:
        has_sub_expression = False
        depth = 0
        opening = 0
        for i in range(len(expression)):
            if expression[i] == "(" and depth == 0:
                opening = i
                has_sub_expression = True
                depth = 1
            elif expression[i] == "(" and depth > 0:
                depth += 1
            elif expression[i] == ")" and depth > 1:
                depth -= 1
            elif expression[i] == ")" and depth == 1:
                depth -= 1

                sub_result = solve_expression_part_two(expression[opening + 1 :i])
                expression = expression.replace(expression[opening:i + 1], sub_result)

                break

    # solve all additions first
    expression_list = expression.split(" ")
    while "+" in expression_list:
        first_plus = expression_list.index("+")
        sub_expression = "{} {} {}".format(expression_list[first_plus - 1], expression_list[first_plus], expression_list[first_plus + 1])
        sub_result = solve_expression(sub_expression)
        new_expression_list = []
        for i in range(len(expression_list)):
            if i == first_plus - 1 or i == first_plus + 1:
                continue
            if i == first_plus:
                new_expression_list.append(sub_result)
            else:
                new_expression_list.append(expression_list[i])
        expression_list = new_expression_list

    result = int(expression_list[0])
    next_opp_add = False
    for i in expression_list[1:]:
        if i == "+":
            next_opp_add = True
        elif i == "*":
            next_opp_add = False
        else:
            if next_opp_add:
                result += int(i)
            else:
                result *= int(i)

    return "{}".format(result)



file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()

expression_list = []

for line in Lines:
    input_line= line.strip()
    expression_list.append(input_line)


print("TASK 1 - sol: {}".format(solve_part_one(expression_list)))

print("TASK 2 - sol: {}".format(solve_part_two(expression_list)))
