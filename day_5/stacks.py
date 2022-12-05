test_start = [
    ['N', 'Z'], 
    ['D', 'C', 'M'], 
    ['P']]

"""
            [Q]     [G]     [M]    
            [B] [S] [V]     [P] [R]
    [T]     [C] [F] [L]     [V] [N]
[Q] [P]     [H] [N] [S]     [W] [C]
[F] [G] [B] [J] [B] [N]     [Z] [L]
[L] [Q] [Q] [Z] [M] [Q] [F] [G] [D]
[S] [Z] [M] [G] [H] [C] [C] [H] [Z]
[R] [N] [S] [T] [P] [P] [W] [Q] [G]
 1   2   3   4   5   6   7   8   9 
"""
input_start = [
    ['Q', 'F', 'L', 'S', 'R'], 
    ['T', 'P', 'G', 'Q', 'Z', 'N'], 
    ['B', 'Q', 'M', 'S'],
    ['Q', 'B', 'C', 'H', 'J', 'Z', 'G', 'T'],
    ['S', 'F', 'N', 'B', 'M', 'H', 'P'],
    ['G', 'V', 'L', 'S', 'N', 'Q', 'C', 'P'],
    ['F', 'C','W'],
    ['M', 'P', 'V', 'W', 'Z', 'G', 'H', 'Q'],
    ['R', 'N', 'C', 'L', 'D', 'Z', 'G']]

import re

file = open('day_5/input.txt', 'r')
lines = file.readlines()

cargo_plan = []
for line in lines:
    line = re.sub(r'move ', '', line)
    line = re.sub(r' from ', ',', line)
    line = re.sub(r' to ', ',', line)
    line = re.sub(r'\n', '', line)
    line = line.split(',')
    line = [int(i)-1 for i in line]
    cargo_plan.append(line)

def pick_up_crates(order, configuration):
    crates = configuration[order[1]][:order[0]+1]
    # print(f"Crates: {order[0]+1}")
    print(f"config: {configuration[order[1]]}")
    configuration[order[1]] = configuration[order[1]][order[0]+1:]
    print(f"config: {configuration[order[1]]}")

    return crates, configuration

def place_down_crates(crates, configuration, order):
    # crates.reverse()
    configuration[order[2]] = crates + configuration[order[2]]
    return configuration

configuration = input_start
print(configuration)
for order in cargo_plan:
    print(order)
    crates_to_move, configuration = pick_up_crates(order, configuration)
    print(f"Crates to move: {crates_to_move}")
    print(f"Config: {configuration}")
    configuration = place_down_crates(crates_to_move, configuration, order)
    print(f"Configuartion: {configuration}")
    print("____________________________________________________________________")

"""
[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3
"""
print(f"Final Config: {configuration}")

[['F', 'G', 'N', 'M', 'P', 'W', 'V', 'R'], 
['Z', 'Q', 'Z', 'G', 'B', 'S', 'S', 'P', 'L', 'L', 'Q', 'C', 'M', 'N', 'S', 'B', 'Q'], 
['C', 'B', 'F', 'N', 'T', 'Q', 'Q'], 
['M'], 
['J'], 
['C', 'F', 'D', 'Z'], 
['R', 'P', 'P', 'T', 'H', 'G', 'G', 'V', 'C', 'S', 'H', 'W', 'Q', 'G', 'L'], 
['H', 'N'], 
['Z']]

# Part Two
 [['J', 'P', 'L', 'F', 'C', 'M', 'Q', 'G'], 
 ['S', 'R', 'C', 'N', 'G', 'N', 'B', 'H', 'H', 'B', 'V', 'Q', 'T', 'W', 'V', 'Z', 'N'], 
 ['D', 'P', 'G', 'Q', 'G', 'R', 'P'], 
 ['H'], 
 ['Q'], 
 ['M', 'C', 'F', 'T'], 
 ['Z', 'L', 'Z', 'S', 'L', 'Q', 'B', 'S', 'C', 'M', 'P', 'S', 'Z', 'N', 'Q'], 
 ['G', 'W'], 
 ['F']]