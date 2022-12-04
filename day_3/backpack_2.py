file = open('day_3/input.txt', 'r')
lines = file.read().splitlines()

def generate_backpacks(n, lines):
    print(n)
    first_backpack = lines[n]
    second_backpack = lines[n+1]
    third_backpack = lines[n+2]
    return [first_backpack, second_backpack, third_backpack]

def find_common_item(backpacks):
    result = set(backpacks[0])
    for s in backpacks[1:]:
        result.intersection_update(s)
    return list(result)[0]

def calculate_character_scoring(double_item):
    if double_item.islower():
        return ord(double_item)-96
    else:
        return ord(double_item)-38

score = 0
n = 0
while n < len(lines):
    backpacks = generate_backpacks(n, lines)
    common_item = find_common_item(backpacks)
    score = score + calculate_character_scoring(common_item)
    n = n + 3

print(f"The final score is: {score}")