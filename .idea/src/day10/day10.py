
def solve_part_one(adapter_list):
    adapter_list.sort()
    one_jolt_diff = 0
    two_jolt_diff = 0
    three_jolt_diff = 0
    current_value = 0
    for adapter in adapter_list:
        diff = adapter - current_value
        if diff == 1:
            one_jolt_diff += 1
        elif diff == 2:
            two_jolt_diff += 1
        elif diff == 3:
            three_jolt_diff += 1
        else:
            print("error")
        current_value = adapter
    return one_jolt_diff * three_jolt_diff

def solve_part_two(adapter_list):
    adapter_list.sort()
    get_all_lists_rec(0, adapter_list, [])
    return all_lists

def get_all_lists_rec(current_index, original_list, current_list):
    global all_lists
    # print("i: {}, curr list: {}".format(current_index, current_list))
    # input("weitr?")
    result = []
    if current_index >= len(original_list):
        if original_list[-1] in current_list:
            all_lists += 1
        return

    current_adapter = original_list[current_index]
    if current_index == 0:
        current_list.append(current_adapter)
        get_all_lists_rec(current_index + 1, original_list, current_list)
    elif current_adapter - current_list[-1] > 3:
        return
    else:
        get_all_lists_rec(current_index + 1, original_list, current_list)
        current_list.append(current_adapter)
        get_all_lists_rec(current_index + 1, original_list, current_list)
        current_list.remove(current_adapter)
    return result

all_lists = 0



file1 = open('test.txt', 'r')
Lines = file1.readlines()

count = 0

adapters = []

for line in Lines:
    input_line= line.strip()
    adapters.append(int(input_line))
    print("Line {}: {}".format(count, input_line))
    count += 1
adapters.append(0)
max_adapter = 0
for adapter in adapters:
    max_adapter = max(max_adapter, adapter)
adapters.append(max_adapter + 3)


print("TASK 1 - sol: {}".format(solve_part_one(adapters)))

print("TASK 2 - sol: {}".format(solve_part_two(adapters)))
