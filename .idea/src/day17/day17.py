import util.util

def solve_part_two(grid_input, length):
    for i in range(6):
        # input("next step?")
        new_grid = util.util.deepcopy_4d(grid_input)
        for x in range(1, length - 1):
            for y in range(1, length - 1):
                for z in range(1, length - 1):
                    for w in range(1, length - 1):
                        active_count = 0
                        for i in [x-1, x, x+1]:
                            for j in [y-1, y, y+1]:
                                for k in [z-1, z, z+1]:
                                    for l in [w-1, w, w+1]:
                                        if grid_input[i][j][k][l] == "#":
                                            active_count += 1
                        # if active_count > 0:
                        #     print(active_count)
                        if grid_input[x][y][z][w] == "#":
                            if active_count == 3 or active_count == 4:
                                new_grid[x][y][z][w] = "#"
                            else:
                                new_grid[x][y][z][w] = "."
                        else:
                            if active_count == 3:
                                new_grid[x][y][z][w] = "#"
                            else:
                                new_grid[x][y][z][w] = "."
        grid_input = new_grid
        # util.util.print_3d(grid_input)
    result = 0
    for slice in grid_input:
        for row in slice:
            for rrow in row:
                for char in rrow:
                    if char == "#":
                        result += 1
    return result

def solve_part_one(grid_input, length):
    for i in range(6):
        # input("next step?")
        new_grid = util.util.deepcopy_3d(grid_input)
        for x in range(1, length - 1):
            for y in range(1, length - 1):
                for z in range(1, length - 1):
                    active_count = 0
                    for i in [x-1, x, x+1]:
                        for j in [y-1, y, y+1]:
                            for k in [z-1, z, z+1]:
                                if grid_input[i][j][k] == "#":
                                    active_count += 1
                    if grid_input[x][y][z] == "#":
                        if active_count == 3 or active_count == 4:
                            new_grid[x][y][z] = "#"
                        else:
                            new_grid[x][y][z] = "."
                    else:
                        if active_count == 3:
                            new_grid[x][y][z] = "#"
                        else:
                            new_grid[x][y][z] = "."
        grid_input = new_grid
        # util.util.print_3d(grid_input)
    result = 0
    for slice in grid_input:
        for row in slice:
            for char in row:
                if char == "#":
                    result += 1
    return result


def init_grid(length, start_slice):
    grid = [[['.' for i in range(length)] for i in range(length)] for i in range(length)]
    # get middle slice
    middle = length // 2
    middle_slice = grid[middle]

    x_offset = middle - (len(start_slice) // 2)
    y_offset = middle - (len(start_slice[0]) // 2)
    print(x_offset)
    for i in range(len(start_slice)):
        for j in range(len(start_slice[i])):
            middle_slice[y_offset + i][x_offset + j] = start_slice[i][j]
    return grid

def init_grid_part_two(length, start_slice):
    grid = [[[['.' for i in range(length)] for i in range(length)] for i in range(length)] for i in range(length)]
    # get middle slice
    middle = length // 2
    middle_slice = grid[middle][middle]

    x_offset = middle - (len(start_slice) // 2)
    y_offset = middle - (len(start_slice[0]) // 2)
    for i in range(len(start_slice)):
        for j in range(len(start_slice[i])):
            middle_slice[y_offset + i][x_offset + j] = start_slice[i][j]
    return grid

file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()

count = 0
start_slice = []

for line in Lines:
    input_line= line.strip()
    start_slice.append(list(input_line))
    print("Line {}: {}".format(count, input_line))
    count += 1

grid_length = 25
grid = init_grid(grid_length, start_slice)
# util.util.print_3d(grid)
print("TASK 1 - sol: {}".format(solve_part_one(grid, grid_length)))

grid = init_grid_part_two(grid_length, start_slice)

print("TASK 2 - sol: {}".format(solve_part_two(grid, grid_length)))
