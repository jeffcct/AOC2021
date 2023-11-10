contents = [k.split("|") for k in open("day_8/input.txt", "r").read().split("\n")]
for i in range(len(contents)):
    for j in range(len(contents[0])):
        contents[i][j] = contents[i][j].strip().split()
print(contents)

print(contents)
ones = 0
fours = 0
sevens = 0
eights = 0
for line in contents:
    for number in line[1]:
        length = len(number)
        if length == 2:
            ones += 1
        elif length == 4:
            ones += 1
        elif length == 3:
            sevens += 1
        elif length == 7:
            eights += 1
            
print(ones + fours + sevens + eights)
