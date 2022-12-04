file = open('day_3/input.txt', 'r')
lines = file.read().splitlines()

def generate_backpack(line):
    middle_index = int( len(line) / 2)
    first_compartment = line[:middle_index]
    second_compartment = line[middle_index:]
    return [first_compartment, second_compartment]

def find_double_item(backpack):
    double_item = set(backpack[0]).intersection(backpack[1])
    return list(double_item)[0]

def calculate_character_scoring(double_item):
    if double_item.islower():
        return ord(double_item)-96
    else:
        return ord(double_item)-38

score = 0
for line in lines:
    backpack = generate_backpack(line)
    double_item = find_double_item(backpack)
    score = score + calculate_character_scoring(double_item)

print(f"The final score is: {score}")