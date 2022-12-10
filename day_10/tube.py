file = open('day_10/input.txt', 'r')
lines = file.readlines()

signal_strengths = []
def increase_cycle(cycle, register, cycle_condition):
    if cycle == cycle_condition:
        print(cycle)
        signal_strength = register * cycle
        signal_strengths.append(signal_strength)
    
    return cycle + 1

register = 1
cycle = 1
cycle_condition = 20
for line in lines:
    line = str(line)
    # print(f'line: {line}, {register=}, {cycle=}')

    if line.startswith('noop'):
         cycle = increase_cycle(cycle, register, cycle_condition)
    
    elif line.startswith('addx'):
        number = line.split(' ')[1]
        cycle = increase_cycle(cycle, register, cycle_condition)
        cycle = increase_cycle(cycle, register, cycle_condition)
        register = register + int(number)
    
    if cycle > cycle_condition:
        cycle_condition = cycle_condition + 40


print(signal_strengths)
print(f"The final signal strentgh is: {sum(signal_strengths)}")