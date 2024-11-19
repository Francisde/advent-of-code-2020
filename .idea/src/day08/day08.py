def solve_part_one(instruction_list):
    global accumulator
    seen_instructions = []
    instruction_pointer = 0
    while True:
        instruction = instruction_list[instruction_pointer]
        if instruction_pointer in seen_instructions:
            return accumulator
        seen_instructions.append(instruction_pointer)

        if instruction.startswith("nop"):
            instruction_pointer += 1
            continue
        elif instruction.startswith("acc"):
            value = int(instruction.split(" ")[1])
            accumulator += value
            instruction_pointer += 1
            continue
        elif instruction.startswith("jmp"):
            value = int(instruction.split(" ")[1])
            instruction_pointer += value
            continue

def solve_part_two(instruction_list):
    global accumulator
    for i in range(len(instruction_list)):
        new_instruction_list = instruction_list.copy()
        if new_instruction_list[i].startswith("acc"):
            continue
        elif new_instruction_list[i].startswith("nop"):
            new_instruction_list[i] = new_instruction_list[i].replace("nop", "jmp")
        elif new_instruction_list[i].startswith("jmp"):
            new_instruction_list[i] = new_instruction_list[i].replace("jmp", "nop")
        seen_instructions = []
        instruction_pointer = 0
        accumulator = 0
        valid = True
        while True:

            if instruction_pointer >= len(new_instruction_list):
                valid = True
                break
            instruction = new_instruction_list[instruction_pointer]
            if instruction_pointer in seen_instructions:
                valid = False
                break
            seen_instructions.append(instruction_pointer)

            if instruction.startswith("nop"):
                instruction_pointer += 1
                continue
            elif instruction.startswith("acc"):
                value = int(instruction.split(" ")[1])
                accumulator += value
                instruction_pointer += 1
                continue
            elif instruction.startswith("jmp"):
                value = int(instruction.split(" ")[1])
                instruction_pointer += value
                continue
        if valid:
            return accumulator


file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()

count = 0

instructions = []

for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    count += 1
    instructions.append(input_line)


accumulator = 0


print("TASK 1 - sol: {}".format(solve_part_one(instructions)))

print("TASK 2 - sol: {}".format(solve_part_two(instructions)))
