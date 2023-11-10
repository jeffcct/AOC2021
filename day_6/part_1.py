input_file = open("day_6/input.txt", "r")
lanternfish = input_file.read().split(",")
input_file.close()
for index in range(len(lanternfish)):
    lanternfish[index] = int(lanternfish[index])

num_days = 80
for day in range(num_days):
    for index in range(len(lanternfish) - 1, -1, -1):
        if lanternfish[index] == 0:
            lanternfish[index] = 6
            lanternfish.append(8)
            
        else:
            lanternfish[index] = lanternfish[index] - 1
print(lanternfish)    
print(len(lanternfish))
