def solve_puzzle(input_list, stop_index):
    last_number = 0
    last_time_spoken = dict()
    first_time = False
    index = 1
    for i in input_list:
        last_number = i
        last_time_spoken["" + str(i)] = index
        first_time = True
        index += 1
    while index <= stop_index:
        if first_time:
            last_number = 0
            if "0" not in last_time_spoken.keys():
                last_time_spoken["0"] = index
                first_time = True
            else:
                first_time = False

        else:
            diff = index - last_time_spoken["" + str(last_number)] - 1
            last_time_spoken["" + str(last_number)] = index - 1
            if "" + str(diff) not in last_time_spoken.keys():
                last_time_spoken["" + str(diff)] = index
                first_time = True
            else:
                first_time = False
            last_number = diff
        index += 1

    return last_number


# input_l = [2,1,3]
input_l = [13,16,0,12,15,1]


print("TASK 1 - sol: {}".format(solve_puzzle(input_l, 2020)))

print("TASK 2 - sol: {}".format(solve_puzzle(input_l, 30000000)))
