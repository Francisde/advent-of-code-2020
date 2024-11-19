
class Bags:

    def __init__(self, name):
        self.name = name
        self.inner_bags = []

    def add_inner_bag(self, bag):
        self.inner_bags.append(bag)

def solve_part_one(rules_list):
    result = 0
    bags_dict = parse_all_colors(rules_list)
    parse_inner_bags(bags_dict, rules_list)
    for bag_string in bags_dict.keys():
        if can_contain(bags_dict, bags_dict[bag_string], [], "shiny gold bag"):
            result += 1
    return result

def solve_part_two(rules_list):
    result = 0
    bags_dict = parse_all_colors(rules_list)
    parse_inner_bags(bags_dict, rules_list)
    return get_total_inner_bags("shiny gold bag", bags_dict) - 1


def get_total_inner_bags(current_bag_string, bags_dict):
    result = 1
    current_bag = bags_dict[current_bag_string]
    for entry in current_bag.inner_bags:
        result += entry[1] * get_total_inner_bags(entry[0].name, bags_dict)
    return result


def can_contain(bags_dict, current_bag, seen_bags, search_one):
    for bag in current_bag.inner_bags:
        if bag[0].name == search_one:
            return True
    for bag in current_bag.inner_bags:
        if bag[0] not in seen_bags:
            new_seen_bags = seen_bags.copy()
            new_seen_bags.append(bag[0])
            result = can_contain(bags_dict, bag[0], new_seen_bags, search_one)
            if result:
                return True
    return False

def parse_all_colors(rules_list):
    bags_dict = dict()
    for rule in rules_list:
        color = rule.split(" contain ")[0]
        bag = Bags(color)
        bags_dict[color] = bag
    return bags_dict

def parse_inner_bags(bags_dict, rules_list):
    for rule in rules_list:
        rule_split = rule.split(" contain ")
        outer_bag = bags_dict[rule_split[0]]
        bags = rule_split[1].split(", ")
        for bag in bags:
            if bag == "no other bag":
                continue
            else:
                quantity = int(bag[0])
                bag_string = bag[2:]
                inner_bag = bags_dict[bag_string]
                outer_bag.add_inner_bag((inner_bag, quantity))



file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()

count = 0


rules = []
for line in Lines:
    input_line= line.strip()
    input_line = input_line.replace(".", "")
    input_line = input_line.replace("bags", "bag")
    print("Line {}: {}".format(count, input_line))
    rules.append(input_line)
    count += 1


print("TASK 1 - sol: {}".format(solve_part_one(rules)))

print("TASK 2 - sol: {}".format(solve_part_two(rules)))
