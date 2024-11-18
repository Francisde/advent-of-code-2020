def solve_part_one(input_list):
    valid_passwords = 0
    for entry in password_list:
        split_entry = entry.split(": ")
        password = split_entry[1]
        policy = split_entry[0].replace("-", " ")
        policy = policy.split(" ")
        lower = int(policy[0])
        upper = int(policy[1])
        token = policy[2]
        count = password.count(token)
        if lower <= count and count <= upper:
            valid_passwords += 1
    return valid_passwords

def solve_part_two(input_list):
    valid_passwords = 0
    for entry in password_list:
        split_entry = entry.split(": ")
        password = split_entry[1]
        policy = split_entry[0].replace("-", " ")
        policy = policy.split(" ")
        lower = int(policy[0])
        upper = int(policy[1])
        token = policy[2]
        if (password[lower - 1] == token and password[upper - 1] != token) or (password[lower - 1] != token and password[upper - 1] == token):
            valid_passwords += 1
    return valid_passwords


file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()

count = 0

password_list = []

for line in Lines:
    input_line= line.strip()
    password_list.append(input_line)
    count += 1


print("TASK 1 - sol: {}".format(solve_part_one(password_list)))

print("TASK 2 - sol: {}".format(solve_part_two(password_list)))
