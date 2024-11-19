def solve_part_two(input_l):
    result = 0
    current_result = []

    for row in input_l:
        if row != "":
            current_result.append(set(list(row)))
        else:
            if len(current_result) == 1:
                result += len(current_result[0])
                current_result = []
            else:
                final_set = current_result[0]
                for set_ in current_result:
                    final_set = final_set.intersection(set_)
                result += len(final_set)
                current_result = []

    return result

def solve_part_one(input_l):
    result = 0
    current_result = []

    for row in input_l:
        if row != "":
            current_result += list(row)
        else:
            result += len(set(current_result))
            current_result = []

    return result


file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()

input_list = []

for line in Lines:
    input_line= line.strip()
    input_list.append(input_line)


print("TASK 1 - sol: {}".format(solve_part_one(input_list)))

print("TASK 2 - sol: {}".format(solve_part_two(input_list)))
