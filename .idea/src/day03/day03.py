def solve_part_one(input_l, right, down):
    grid = generate_field(input_l, 100)
    seen_trees = 0
    current_x = 0
    current_y = 0
    while current_y < len(grid):
        if grid[current_y][current_x] == "#":
            seen_trees += 1
        current_x += right
        current_y += down
    return seen_trees

def solve_part_two(input_l):
    result = 1
    seen_trees = []
    seen_trees.append(solve_part_one(input_l, 1, 1))
    seen_trees.append(solve_part_one(input_l, 3, 1))
    seen_trees.append(solve_part_one(input_l, 5, 1))
    seen_trees.append(solve_part_one(input_l, 7, 1))
    seen_trees.append(solve_part_one(input_l, 1, 2))
    for i in seen_trees:
        result *= i
    return result

def generate_field(input_l, repeat):
    result = []
    for line in input_l:
        row = []
        for i in range(repeat):
            row += list(line)
        result.append(row)
    return result


file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()

input_list = []
for line in Lines:
    input_line= line.strip()
    input_list.append(input_line)


print("TASK 1 - sol: {}".format(solve_part_one(input_list, 3, 1)))

print("TASK 2 - sol: {}".format(solve_part_two(input_list)))
