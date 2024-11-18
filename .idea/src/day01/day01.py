def solve_part_one(input_list):
    result = 0
    for int1 in expense_list:
        for int2 in expense_list:
            if int1 != int2:
                if int1 + int2 == 2020:
                    return int1 * int2
    return result

def solve_part_two(input_list):
    result = 0
    for int1 in expense_list:
        for int2 in expense_list:
            for int3 in expense_list:
                if int1 != int2 and int1 != int3 and int2 != int3:
                    if int1 + int2 + int3 == 2020:
                        return int1 * int2 * int3
    return result

file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()

count = 0

expense_list = []

for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    expense_list.append(int(input_line))
    count += 1


print("TASK 1 - sol: {}".format(solve_part_one(expense_list)))

print("TASK 2 - sol: {}".format(solve_part_two(expense_list)))
