import util.util

def solve_puzzle(grid, threshold, rule):
    old_grid = grid
    changes = True
    while changes:
        changes = False
        new_grid = []
        for row in old_grid:
            new_grid.append(row.copy())
        changes = simulate_one_step(old_grid, new_grid, threshold, rule)

        old_grid = new_grid
    util.util.print_2d(old_grid)
    result = 0
    for row in old_grid:
        for char in row:
            if char == "#":
                result += 1
    return result


def simulate_one_step(old_grid, new_grid, threshold, rule):
    result = False
    for i in range(len(old_grid)):
        for j in range(len(old_grid[i])):
            number_of_occupied_seats = 0
            if rule == 0:
                number_of_occupied_seats = get_number_of_occupied_seats(old_grid, i, j)
            else:
                number_of_occupied_seats = get_number_of_occupied_seats_rule2(old_grid, i, j)
            if old_grid[i][j] == "L" and number_of_occupied_seats == 0:
                new_grid[i][j] = "#"
                result = True
            if old_grid[i][j] == "#" and number_of_occupied_seats >= threshold:
                new_grid[i][j] = "L"
                result = True
    return result

def get_number_of_occupied_seats(grid, i, j):
    result = 0
    if i > 0:
        if j > 0:
            if grid[i-1][j-1] == "#":
                result += 1
        if grid[i-1][j] == "#":
            result += 1
        if j < len(grid[i]) -1:
            if grid[i-1][j+1] == "#":
                result += 1
    if i < len(grid) - 1:
        if j > 0:
            if grid[i+1][j-1] == "#":
                result += 1
        if grid[i+1][j] == "#":
            result += 1
        if j < len(grid[i]) -1:
            if grid[i+1][j+1] == "#":
                result += 1
    if j > 0:
        if grid[i][j-1] == "#":
            result += 1
    if j < len(grid[i]) -1:
        if grid[i][j+1] == "#":
            result += 1
    return result

def get_number_of_occupied_seats_rule2(grid, i, j):
    result = 0
    # check up
    current_i = i -1
    while current_i >=0:
        if grid[current_i][j] == ".":
            current_i -= 1
        elif grid[current_i][j] == "#":
            result += 1
            break
        else:
            break
    # check down
    current_i = i + 1
    while current_i < len(grid):
        if grid[current_i][j] == ".":
            current_i += 1
        elif grid[current_i][j] == "#":
            result += 1
            break
        else:
            break

    # check left
    current_j = j -1
    while current_j >=0:
        if grid[i][current_j] == ".":
            current_j -= 1
        elif grid[i][current_j] == "#":
            result += 1
            break
        else:
            break
    # check right
    current_j = j + 1
    while current_j < len(grid[i]):
        if grid[i][current_j] == ".":
            current_j += 1
        elif grid[i][current_j] == "#":
            result += 1
            break
        else:
            break
    # check left up
    current_j = j - 1
    current_i = i - 1
    while current_j >= 0 and current_i >=0:
        if grid[current_i][current_j] == ".":
            current_j -= 1
            current_i -= 1
        elif grid[current_i][current_j] == "#":
            result += 1
            break
        else:
            break
    # check right down
    current_j = j + 1
    current_i = i + 1
    while current_j < len(grid[i]) and current_i < len(grid):
        if grid[current_i][current_j] == ".":
            current_j += 1
            current_i += 1
        elif grid[current_i][current_j] == "#":
            result += 1
            break
        else:
            break

    # check right up
    current_j = j + 1
    current_i = i - 1
    while current_j < len(grid[i]) and current_i >=0:
        if grid[current_i][current_j] == ".":
            current_j += 1
            current_i -= 1
        elif grid[current_i][current_j] == "#":
            result += 1
            break
        else:
            break
    # check left down
    current_j = j - 1
    current_i = i + 1
    while current_i < len(grid[i]) and current_j >=0:
        if grid[current_i][current_j] == ".":
            current_j -= 1
            current_i += 1
        elif grid[current_i][current_j] == "#":
            result += 1
            break
        else:
            break

    return result



file1 = open('test2.txt', 'r')
Lines = file1.readlines()

count = 0

input_grid = []

for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    count += 1
    input_grid.append(list(input_line))


print("TASK 1 - sol: {}".format(solve_puzzle(input_grid, 4, 0)))

print("TASK 2 - sol: {}".format(solve_puzzle(input_grid, 5, 1)))
