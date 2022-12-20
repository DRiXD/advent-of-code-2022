import re

class Monkey():

    inspections = 0

    def __init__(self, inventory, operation, test, throwing_dict):
        self.inventory = inventory
        self.operation = operation
        self.test = int(test)
        self.throwing_dict = throwing_dict

    def throw_item(self, monkey, item):
        print(self.inventory)
        self.inventory.pop(0)
        print(self.inventory)
        monkey.inventory.append(item)

    def update_worry_level(self, item):
        self.operation = re.sub(r'old', 'item', self.operation)
        return eval(self.operation)

    def inspect_item(self, item, monkeys, monkeymod):
        #print(f"ITEM: {item}")
        self.inspections += 1
        #print(f"Monkey inspects an item with a worry level of {item}.")
        worry_level = self.update_worry_level(item)
        #print(f"Worry level is multiplied by ? to {worry_level}.")

        if round == 1:
            worry_level = worry_level // 3
        else:
            worry_level = worry_level % monkeymod
        #print(f"Monkey gets bored with item. Worry level is divided by 3 to {worry_level}.")

        if worry_level % self.test == 0:
            index = self.throwing_dict["True"]
            self.throw_item(monkeys[index], worry_level)
            print(f"Item with worry level {worry_level} is thrown to monkey {index}.")
        else:
            index = self.throwing_dict["False"]
            self.throw_item(monkeys[index], worry_level)
            print(f"Item with worry level {worry_level} is thrown to monkey {index}.")


