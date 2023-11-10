input_file = open("input.txt", "r")
contents = input_file.read().split("\n")
input_file.close()
print(contents)
prev = int(contents[0])
total = 0
for number in contents[1:]:
    number = int(number)
    if number > prev:
        total+=1
    prev = number
print(total)