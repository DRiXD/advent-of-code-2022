file = open('day_8/input.txt', 'r')
lines = file.readlines()

tree_grid = []
for line in lines:
    line = [int(x) for x in line if x!='\n']
    tree_grid.append(line)

height = len(tree_grid)
width = len(tree_grid[0])

def get_scenic_score_of_direction(current_x, current_y, direction, current_tree):
    # print(f"--------------------------------{direction}----------------------------------")
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
    	
        # print(f"{current_x=}, {current_y=}")
        next_tree = tree_grid[current_y][current_x]
        # print(f"Tree iam looking at: {next_tree}")
        
        trees.append(1)

        if next_tree >= current_tree:
            break
        elif current_x == 0 or current_x == width-1 or current_y == 0 or current_y == height-1:
            break

    return sum(trees)

scenic_scores = []
for y in range(1, (width-1)):
    for x in range(1, (height-1)):
        # print(f"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$${x=}, {y=}, tree_grid element {tree_grid[y][x]}$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        scenic_score = 1

        current_tree = tree_grid[y][x]
        scenic_score = scenic_score * get_scenic_score_of_direction(x, y, 'up', current_tree)
        scenic_score = scenic_score * get_scenic_score_of_direction(x, y, 'down', current_tree)
        scenic_score = scenic_score * get_scenic_score_of_direction(x, y, 'left', current_tree)
        scenic_score = scenic_score * get_scenic_score_of_direction(x, y, 'right', current_tree)

        # print(f"Scenic Score of {x}, {y} is: {scenic_score}")
        scenic_scores.append(scenic_score)
       
highest_score = max(scenic_scores)
print(f"Highest possible scenic score is: {highest_score}")
