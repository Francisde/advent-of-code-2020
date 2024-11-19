def solve_part_one(billet_list):
    highest_id = 0
    for billet in billet_list:
        row = get_row(billet)
        col = get_col(billet)
        ticket_id = row * 8 + col
        highest_id = max(highest_id, ticket_id)
    return highest_id

def solve_part_two(billet_list):
    field = [["." for i in range(8)] for j in range(128)]
    my_id = 0
    ids = []
    for billet in billet_list:
        row = get_row(billet)
        col = get_col(billet)
        ids.append(row * 8 + col)
        field[row][col] = "#"
    for row in field:
        print(row)
    for i in range(128):
        for j in range(8):
            if field[i][j] == ".":
                current_id = i * 8 + j
                if current_id - 1 in ids and current_id + 1 in ids:
                    print("found")
                    my_id = current_id

    return my_id

def get_row(billet):
    lower = 0
    upper = 127
    for i in range(7):
        if billet[i] == "F":
            upper = int(upper - ((upper - lower + 1) / 2))
        if billet[i] == "B":
            lower = int(lower + ((upper - lower + 1) / 2))
    return lower

def get_col(billet):
    lower = 0
    upper = 7
    for i in range(3):
        if billet[7 + i] == "L":
            upper = int(upper - ((upper - lower + 1) / 2))
        if billet[7 + i] == "R":
            lower = int(lower + ((upper - lower + 1) / 2))
    return lower


file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()

count = 0

tickets = []

for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    count += 1
    tickets.append(input_line)


print("TASK 1 - sol: {}".format(solve_part_one(tickets)))

print("TASK 2 - sol: {}".format(solve_part_two(tickets)))
