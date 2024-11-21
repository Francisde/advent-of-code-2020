
def solve_part_one(preamble_length, input_list):
    for i in range(preamble_length , len(input_list)):

        valid = False
        for number1 in input_list[i-preamble_length: i]:
            for number2 in input_list[i-preamble_length: i]:
                if number1 != number2:
                    if number1 + number2 == input_list[i]:
                        valid = True

        if not valid:
            return input_list[i]

def solve_part_two(preamble_length, input_list):
    invalid_number = solve_part_one(preamble_length, input_list)

    for i in range(len(input_list)):
        index = i + 1
        smallest = input_list[i]
        largest = input_list[i]
        sum = smallest
        while sum < invalid_number:
            sum += input_list[index]
            smallest = min(smallest, input_list[index])
            largest = max(largest, input_list[index])
            if sum == invalid_number:

                return smallest + largest
            index += 1



file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()

count = 0

cypher_input = []

for line in Lines:
    input_line= line.strip()
    cypher_input.append(int(input_line))
    print("Line {}: {}".format(count, input_line))
    count += 1


print("TASK 1 - sol: {}".format(solve_part_one(25, cypher_input)))

print("TASK 2 - sol: {}".format(solve_part_two(25,  cypher_input)))
