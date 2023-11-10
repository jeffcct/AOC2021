#inputs
position = [0, 0, 0] # [aim, depth, forwards] are positive
input_file = open("day_2/input.txt", "r")
contents = input_file.read().split("\n")
input_file.close()

#switch
for line in contents:
    line = line.split()
    if line[0] == "down":
        position[0] += int(line[1]) #increase aim
    elif line[0] == "up":
        position[0] -= int(line[1]) #decrease aim
    elif line[0] == "forward":
        position[2] += int(line[1]) #increase forwards
        position[1] += int(line[1]) * position[0] #increases depth by aim * new horizontal change

#display
print(position, position[1] * position[2])