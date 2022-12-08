import json
import re

with open('day_7/test.txt', 'r') as myFile:
    text = myFile.read()
puzzle_input = text.split('$')
puzzle_input = list(filter(None, puzzle_input))
print(puzzle_input)

def handle_cd(command):
    if command == " cd ..\n":
        print("Step up")
    else:
        command = command[3:len(command)]
        command = re.sub(r'\n', '', command)
        print(f"Step down into {command}")

        directory_tree[command] = {}

def handle_ls(command):
    command = re.sub(r' ls\n', '', command)
    ls = command.split('\n')
    ls = list(filter(None, ls))
    print(ls)

    current_ls = {}
    for x in ls:
        if x[0:3] == 'dir':
            directory_tree['/'][a]

    directory_tree['/'] = ls


directory_tree = {}
current_path = []
i = 0
for command in puzzle_input:
    if command == '':
        print("EMPTY STRING")
    elif command[0:3] == ' cd':
        handle_cd(command)
    elif command[0:3] == ' ls':
        print("We have ls")
        handle_ls(command)
    else:
        print("output")

    i = i +1
    if i == 3:
        break


with open('day_7/output_dir.json', 'w') as output_file:
     output_file.write(json.dumps(directory_tree))
