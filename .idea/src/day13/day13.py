def solve_part_one(earliest_depart_time, bus_list):
    min_id = 0
    min_time_gap = 100000
    for bus in bus_list:
        if bus == "x":
            continue
        else:
            travel_time = int(bus)
            match_time = 0
            while match_time <= earliest_depart_time:
                match_time += travel_time
            if match_time - earliest_depart_time < min_time_gap:
                min_time_gap = match_time - earliest_depart_time
                min_id = travel_time

    return (min_id * min_time_gap)

def solve_part_two(bus_list):
    integer_list = []
    current_times = []
    solution_list = []
    index = 0
    for bus in bus_list:
        if bus == "x":
            index += 1
            continue
        else:
            solution_list.append(index)
            integer_list.append(int(bus))
            current_times.append(0)
            index += 1
    print(solution_list)
    while True:

        for index in range(len(current_times)):
            if index == 0:
                current_times[index] = current_times[index] + integer_list[index]
            else:
                while current_times[index] <= current_times[index - 1]:
                    current_times[index] = current_times[index] + integer_list[index]
        correct = correct_solution(solution_list, current_times)


        if correct:
            return current_times[0]

def correct_solution(solution_list, current_time_list):
    reference = current_time_list[0]
    for i in range(len(current_time_list)):
        if current_time_list[i] != reference + solution_list[i]:
            return False
    return True


file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()

count = 0

depart_time = 0
busses = []

for line in Lines:
    input_line= line.strip()
    if depart_time == 0:
        depart_time = int(input_line)
    else:
        busses = input_line.split(",")
    print("Line {}: {}".format(count, input_line))
    count += 1


print("TASK 1 - sol: {}".format(solve_part_one(depart_time, busses)))

print("TASK 2 - sol: {}".format(solve_part_two(busses)))
