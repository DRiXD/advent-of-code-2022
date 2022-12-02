file = open('day_2/input.txt', 'r')
lines = file.readlines()

strategy_plan = []
for line in lines:
    strategy_plan.append((line[0], line[2]))

def calulate_points(mapping, strategy):
    points = []
    for turn in strategy:
        points.append(mapping[turn])
    return points


# Y = Paper, X = Rock, Z = Scissor  
# A = Rock, B = Paper, C = Scissor
points_dict = {
    ('A', 'X'): 4,
    ('A', 'Y'): 8,
    ('A', 'Z'): 3,
    ('B', 'X'): 1,
    ('B', 'Y'): 5,
    ('B', 'Z'): 9,
    ('C', 'X'): 7,
    ('C', 'Y'): 2,
    ('C', 'Z'): 6,
}

print(f"The final points are: {sum(calulate_points(points_dict, strategy_plan))}")

# Part Two
# A = Rock 1, B = Paper 2, C = Scissor 3
# X = Loose, Y = Draw, Z = Win  
points_dict_two = {
    ('A', 'X'): 3,
    ('A', 'Y'): 4,
    ('A', 'Z'): 8,
    ('B', 'X'): 1,
    ('B', 'Y'): 5,
    ('B', 'Z'): 9,
    ('C', 'X'): 2,
    ('C', 'Y'): 6,
    ('C', 'Z'): 7,
}
print(f"The final points are: {sum(calulate_points(points_dict_two, strategy_plan))}")
