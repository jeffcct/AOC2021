input_file = open("day_6/input.txt", "r")
numbers = input_file.read().split(",")
input_file.close()
lanternfish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for number in numbers:
    lanternfish[int(number)] += 1
    
    
num_days = 1000
for day in range(num_days):
    new = lanternfish[0]
    for i in range(1, len(lanternfish)):
        lanternfish[i - 1] = lanternfish[i]
    lanternfish[8] = new
    lanternfish[6] += new
    
print(lanternfish)    
total = 0
for number in lanternfish:
    total += number
print(total)
