def solve_part_one(input_list):
    result = 0
    passport = ""
    for line in input_list:
        if line == "":
            if check_passport(passport):
                result += 1
            passport = ""
        else:
            passport = passport + line + ""
    return result

def solve_part_two(input_list):
    result = 0
    passport = ""
    for line in input_list:
        if line == "":
            if check_passport(passport):
                if validate_passport(passport):
                    result += 1
            passport = ""
        else:
            passport = passport + line + " "
    return result

def check_passport(passport):
    valid = True
    keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for key in keys:
        if key not in passport:
            valid = False
    return valid

def validate_passport(passport):
    passport = passport.strip()
    valid = True
    key_value_pairs = passport.split(" ")
    for key_value in key_value_pairs:
        key = key_value.split(":")[0]
        value = key_value.split(":")[1]
        if key == "byr":
            year = int(value)
            if year < 1920 or year > 2002:
                valid = False
        if key == "iyr":
            year = int(value)
            if year < 2010 or year > 2020:
                valid = False
        if key == "eyr":
            year = int(value)
            if year < 2020 or year > 2030:
                valid = False
        if key == "hgt":
            if value.endswith("in"):
                height = int(value[0:-2])
                if height < 59 or height > 76:
                    valid = False

            elif value.endswith("cm"):
                height = int(value[0:-2])
                if height < 150 or height > 193:
                    valid = False
            else:
                valid = False
        if key == "ecl":
            if value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                valid = False
        if key == "hcl":
            if value.startswith("#") and len(value) == 7:
                color_code = value[1:]
                for ch in color_code:

                    if ((ch < '0' or ch > '9') and (ch < 'a' or ch > 'f')):
                        valid = False
            else:
                valid = False
        if key == "pid":
            if len(value) != 9:
                valid = False
            else:
                if not value.isnumeric():
                    valid = False
    return valid

file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()

input_l = []
for line in Lines:
    input_line= line.strip()
    input_l.append(input_line)


print("TASK 1 - sol: {}".format(solve_part_one(input_l)))

print("TASK 2 - sol: {}".format(solve_part_two(input_l)))
