file = open('day_1/input.txt', 'r')
Lines = file.readlines()

elves = []
elf = []
for line in Lines:
    if line == '\n':
        elves.append(sum(elf))
        elf = []
    else:
        elf.append(int(line))
elves.append(sum(elf))

print(f"Elf number {elves.index(max(elves))+1} has the most calories with a total of {max(elves)}")

# Part Two

unsorted_elves = elves.copy()

elves.sort()
elves.reverse()
most_calories = elves[0]
print(f"Elf number {unsorted_elves.index(most_calories)+1} has the most calories with a total of {most_calories}")
second_most_calories = elves[1]
print(f"Elf number {unsorted_elves.index(second_most_calories)+1} has the second most calories with a total of {second_most_calories}")
third_most_calories = elves[2]
print(f"Elf number {unsorted_elves.index(third_most_calories)+1} has the most calories with a total of {third_most_calories}")
print(f"Total calories by top three: {most_calories+second_most_calories+third_most_calories}")