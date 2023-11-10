position = [0, 0] # [depth, forwards] are positive
input_file = open("day_2/input.txt", "r")
contents = input_file.read().split("\n")
input_file.close()

for line in contents:
    line = line.split()
    if line[0] == "down":
        position[0] += int(line[1])
    elif line[0] == "up":
        position[0] -= int(line[1])
    elif line[0] == "forward":
        position[1] += int(line[1])
    else:
        position[1] -= int[line[1]]

print(position, position[0] * position[1])
    