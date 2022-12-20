from monkey import Monkey
import re

file = open('day_11/input.txt', 'r')
lines = file.readlines()

def get_inventory(line):
    line = line.strip()
    line = re.sub(r',', '', line)
    line = line.split(" ")
    inventory = [int(x) for x in line[2:]]
    return inventory

def get_operation(line):
    line = line.strip()
    operation = line[17:]
    return operation

def get_test_value(line):
    line = line.strip()
    line = line.split(" ")
    test_value = line[3]
    return test_value

def get_throwing_dict(true_line, false_line):
    throwing_dict = {}
    true_line = true_line.strip()
    true_line = true_line.split(" ")
    true_throw = true_line[5]

    false_line = false_line.strip()
    false_line = false_line.split(" ")
    false_throw = false_line[5]

    throwing_dict["True"] = int(true_throw)
    throwing_dict["False"] = int(false_throw)
    return throwing_dict

monkeys = []
monkeymod = 1
round = 2
for index, line in enumerate(lines):
    if line.startswith('  Starting items:'):
        inventory = get_inventory(line)
    elif line.startswith('  Operation:'):
        operation = get_operation(line)
    elif line.startswith('  Test:'):
        test_value = get_test_value(line)
        throwing_dict = get_throwing_dict(lines[index+1], lines[index+2])
        monkeymod *= int(test_value)
    elif line == '\n':
        monkey = Monkey(inventory=inventory, operation = operation, test = test_value, throwing_dict = throwing_dict)
        monkeys.append(monkey)


for j in range(0,10000):
    for index, monkey in enumerate(monkeys):
        inv = monkey.inventory.copy()
        for item in inv:
            print(item)
            monkey.inspect_item(item, monkeys, monkeymod)

inspections = []
for monkey in monkeys:
    inspections.append(monkey.inspections)
print(inspections)