def solve_part_one(input_list):
    current_x = 0
    current_y = 0
    facing = "E"
    for instruction in input_list:
        code = instruction[0]
        value = int(instruction[1:])
        if code == "N":
            current_y += value
        if code == "S":
            current_y -= value
        if code == "E":
            current_x += value
        if code == "W":
            current_x -= value
        if code == "L" or code == "R":
            facing = turn_ship(facing, value, code)
        if code == "F":
            if facing == "N":
                current_y += value
            if facing == "S":
                current_y -= value
            if facing == "E":
                current_x += value
            if facing == "W":
                current_x -= value
        # print((current_x, current_y))
    return abs(current_x) +  abs(current_y)

def solve_part_two(input_list):
    current_x = 0
    current_y = 0
    waypoint_x = 10
    waypoint_y = 1
    facing = "E"
    for instruction in input_list:
        code = instruction[0]
        value = int(instruction[1:])
        if code == "N":
            waypoint_y += value
        if code == "S":
            waypoint_y -= value
        if code == "E":
            waypoint_x += value
        if code == "W":
            waypoint_x -= value
        if code == "L" or code == "R":
            relative_x = waypoint_x - current_x
            relative_y = waypoint_y - current_y
            new_relatives = rotate_waypoint(value, code, relative_x, relative_y)
            waypoint_x = current_x + new_relatives[0]
            waypoint_y = current_y + new_relatives[1]
        if code == "F":
            relative_x = waypoint_x - current_x
            relative_y = waypoint_y - current_y
            waypoint_x += (value * relative_x)
            waypoint_y += (value * relative_y)
            current_x += (value * relative_x)
            current_y += (value * relative_y)
    return abs(current_x) +  abs(current_y)

def rotate_waypoint(degree, direction, relative_x, relative_y):
    new_relative_x = relative_x
    new_relative_y = relative_y
    if direction == "L":
        direction = "R"
        degree = 360 - degree
    if direction == "R":
        while degree > 0:
            new_relative_x = relative_y
            new_relative_y = - relative_x
            relative_x = new_relative_x
            relative_y = new_relative_y
            degree -= 90
    return (relative_x, relative_y)



def turn_ship(old_facing, degree, direction):
    direction_degree_dict = dict()
    direction_degree_dict["N"] = 0
    direction_degree_dict["E"] = 90
    direction_degree_dict["S"] = 180
    direction_degree_dict["W"] = 270
    degree_direction_dict = dict()
    degree_direction_dict["0"] = "N"
    degree_direction_dict["90"] = "E"
    degree_direction_dict["180"] = "S"
    degree_direction_dict["270"] = "W"
    facing_degree = direction_degree_dict[old_facing]
    if direction == "L":
        new_facing_degree = (facing_degree - degree) % 360
        return degree_direction_dict["{}".format(new_facing_degree)]
    if direction == "R":
        new_facing_degree = (facing_degree + degree) % 360
        return degree_direction_dict["{}".format(new_facing_degree)]

file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()

count = 0

instructions = []

for line in Lines:
    input_line= line.strip()
    instructions.append(input_line)
    print("Line {}: {}".format(count, input_line))
    count += 1


print("TASK 1 - sol: {}".format(solve_part_one(instructions)))

print("TASK 2 - sol: {}".format(solve_part_two(instructions)))
