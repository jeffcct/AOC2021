def show(grid, x, y):
    grid[y][x] += 1
    if grid[y][x] == 2:
        return True
    return False
    




# initialisation
input_file = open("day_5/input.txt", "r")
contents = input_file.read().split("\n")
input_file.close()
max_x = 0
max_y = 0

for index in range(len(contents)):
    contents[index] = contents[index].split("->")
    for i in range(2):
        contents[index][i] = contents[index][i].strip().split(",")
        contents[index][i][0] = int(contents[index][i][0])
        if contents[index][i][0] > max_x:
            max_x = contents[index][i][0]
        contents[index][i][1] = int(contents[index][i][1])
        if contents[index][i][1] > max_y:
            max_y = contents[index][i][1]

grid = [[0 for i in range(max_x + 1)] for j in range(max_y + 1)]

total = 0
for line in contents:
    if line[0][0] == line[1][0]:
        if line[0][1] < line[1][1]:
            for y in range(line[0][1], line[1][1] + 1):
                x = line[0][0]
                if show(grid, x, y):
                    total += 1
        else:
            for y in range(line[1][1], line[0][1] + 1):
                x = line[0][0]
                if show(grid, x, y):
                    total += 1
                    
    elif line[0][1] == line[1][1]:
        if line[0][0] < line[1][0]:
            for x in range(line[0][0], line[1][0] + 1):
                y = line[0][1]
                if show(grid, x, y):
                    total += 1
        else:
            for x in range(line[1][0], line[0][0] + 1):
                y = line[0][1]
                if show(grid, x, y):
                    total += 1
                   
    elif line[0][0] < line[1][0]:
        x, y = line[0]
        if line[0][1] < line[1][1]:
            for i in range(line[1][0] - x + 1):
                if show(grid, x + i, y + i):
                    total += 1
        else:
            for i in range(line[1][0] - x + 1):
                if show(grid, x + i, y - i):
                    total += 1
    
    else:
        x, y = line[1]
        if line[0][1] < line[1][1]:
            for i in range(line[0][0] - x + 1):
                if show(grid, x + i, y - i):
                    total += 1
        else:
            for i in range(line[0][0] - x + 1):
                if show(grid, x + i, y + i):
                    total += 1

for line in grid:
    print(line)
print(total)
            
            
        




