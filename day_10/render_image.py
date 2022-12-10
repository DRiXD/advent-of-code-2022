file = open('day_10/input.txt', 'r')
lines = file.readlines()


def print_screen(screen):
    i = 1
    current_row = []
    for pixel in screen:
        if i % 40 == 0:
            current_row.append(pixel)
            print_row = ''.join(current_row)
            print(print_row)
            current_row = []
        else:
            current_row.append(pixel)
        i = i+1
    print('')


def manage_cycle(cycle, register, line, crt_row, operation, addx_part=1, number=0):
    crt_pos = cycle - 1
    print(f"Start cycle {cycle}: begin executing {line}")
    print(f"During cycle  {cycle}: CRT draws pixel in position {crt_pos} ")

    print(f"REGISTER: {register}, CRT_POS: {crt_pos}")
    if register == crt_pos or register+1 == crt_pos or register-1==crt_pos:
        crt_row.append('#')
    else:
        crt_row.append('.')

    print(f"Current crt_row: {''.join(crt_row)}")

    if addx_part == 2 or operation == 'noop':
        register = register + int(number)
        print(f"End of cycle  {cycle}: finish executing {line} (Register X is now {register})")
        screen_row[register] = '#'
        screen_row[register+1] = '#'
        screen_row[register-1] = '#'
        print(f"Sprite position: {''.join(screen_row)}")
        screen_row[register] = '.'
        screen_row[register+1] = '.'
        screen_row[register-1] = '.'
    print(' ')
    
    if cycle % 40 == 0:
        register = register + 40

    return cycle + 1, register



signal_strengths = []
register = 1
cycle = 1
cycle_condition = 20
crt_row = []
rendered_screen = []

print(f"Sprite position: ###.....................................")
screen_row = []
for x in range (1,240):
    screen_row.append('.')

for line in lines:
    line = str(line).strip()

    
    if line.startswith('noop'):
        cycle, register = manage_cycle(cycle, register, line, crt_row, 'noop')
        iterator = 1
    elif line.startswith('addx'):
        number = line.split(' ')[1]
        cycle, register = manage_cycle(cycle, register, line, crt_row, 'addx', 1)
        cycle, register = manage_cycle(cycle, register, line, crt_row, 'addx', 2, number)
        iterator = 2

print_screen(crt_row)