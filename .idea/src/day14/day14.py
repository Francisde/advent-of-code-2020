def solve_part_one(instruction_list):
    mask = ""
    registers = dict()
    for instruction in instruction_list:
        if instruction.startswith("mask"):
            mask = instruction.split(" = ")[1]
        else:
            index_a = instruction.index("[")
            index_b = instruction.index("]")
            register_v = instruction[index_a+1:index_b]
            value = int(instruction.split(" = ")[1])
            for i in range(len(mask)):
                print(mask[-i])
                if mask[-i] == "X":
                    continue
                else:
                    value = set_bit(value, i - 1, int(mask[-i]))
            registers[register_v] = value
    sum = 0
    for register in registers.keys():
        sum += registers[register]
    return sum



def set_bit(v, index, x):
    # https://stackoverflow.com/questions/12173774/how-to-modify-bits-in-an-integer
    mask = 1 << index   # Compute mask, an integer with just bit 'index' set.
    v &= ~mask          # Clear the bit indicated by the mask (if x is False)
    if x:
        v |= mask         # If x was True, set the bit indicated by the mask.
    return v            # Return the result, we're done.


file1 = open('test.txt', 'r')
Lines = file1.readlines()

count = 0
instructions = []

for line in Lines:
    input_line= line.strip()
    instructions.append(input_line)
    print("Line {}: {}".format(count, input_line))
    count += 1


print("TASK 1 - sol: {}".format(solve_part_one(instructions)))

print("TASK 2 - ")
