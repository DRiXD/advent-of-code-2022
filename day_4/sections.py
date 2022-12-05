import re

file = open('day_4/input.txt', 'r')
lines = file.readlines()

sections = []
for line in lines:
    line = re.sub(r'-', ',', line)
    line = re.sub(r'\n', '', line)
    line = line.split(',')
    line = [int(i) for i in line]

    sections.append(line)

duplicates = 0
for section in sections:
    if section[0] <= section[2] and section[1] >= section[3]:
        duplicates = duplicates +1
    elif section[2] <= section[0] and section[3] >= section[1]:
        duplicates = duplicates+1
    else:
        pass
        

print(f"Final duplicates: {duplicates}")

# Part Two

overlaps = 0
for section in sections:
    if section[2] <= section[0] <= section[3]:
        print("OVERLAP")
        overlaps = overlaps +1
    elif section[2] <= section[1] <= section[3]:
        print("OVERLAP")
        overlaps = overlaps +1
    elif section[0] <= section[2] <= section[1]:
        print("OVERLAP")
        overlaps = overlaps +1
    elif section[0] <= section[3] <= section[1]:
        print("OVERLAP")
        overlaps = overlaps +1
    else:
        pass
        

print(f"Final overlaps: {overlaps}")

