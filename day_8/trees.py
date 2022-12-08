file = open('day_8/input.txt', 'r')
lines = file.readlines()

tree_grid = []
for line in lines:
    line = [int(x) for x in line if x!='\n']
    tree_grid.append(line)

print(tree_grid)

height = len(tree_grid)
width = len(tree_grid[0])
print(f"Height: {height}, width: {width}")

num_outer_trees = 2 * width + 2 * (height-2)
print(f"{num_outer_trees=}")

def get_list_of_trees_in_one_direction(current_x, current_y, direction):
    print(f"--------------------------------{direction}----------------------------------")
    x_iterator = 0
    y_iterator = 0

    if direction == 'up':
        y_iterator = -1
    elif direction == 'down':
        y_iterator = 1
    elif direction == 'left':
        x_iterator = -1
    elif direction == 'right':
        x_iterator = 1
    
    trees = []
    while(True):
        current_x = current_x + x_iterator
        current_y = current_y + y_iterator
    	
        print(f"{current_x=}, {current_y=}")
        next_tree = tree_grid[current_y][current_x]
        print(f"Tree iam looking at: {next_tree}")
        trees.append(next_tree)

        if current_x == 0 or current_x == width-1 or current_y == 0 or current_y == height-1:
            break
    return trees


middle_trees_visible = 0
for y in range(1, (width-1)):
    for x in range(1, (height-1)):
        print(f"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$${x=}, {y=}, tree_grid element {tree_grid[y][x]}$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

        current_tree = tree_grid[y][x]
        upper = get_list_of_trees_in_one_direction(x, y, 'up')
        lower = get_list_of_trees_in_one_direction(x, y, 'down')
        left = get_list_of_trees_in_one_direction(x, y, 'left')
        right = get_list_of_trees_in_one_direction(x, y, 'right')

        if all(item < current_tree for item in upper):
            print(f"Direction up is free: {upper}")
            middle_trees_visible = middle_trees_visible +1
        elif all(item < current_tree for item in lower):
            print(f"Direction down is free: {lower}")
            middle_trees_visible = middle_trees_visible +1
        elif all(item < current_tree for item in left):
            print(f"Direction left is free: {left}")
            middle_trees_visible = middle_trees_visible +1
        elif all(item < current_tree for item in right):
            print(f"Direction right is free: {right}")
            middle_trees_visible = middle_trees_visible +1
        

print(f"Final answer is: {num_outer_trees + middle_trees_visible}")
