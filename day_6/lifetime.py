import random
def update_birthrate(lanternfish):
    for birth_left in range(birthtime + at_birth):
        for life_left in range(1, lifetime):
            lanternfish[birth_left][life_left - 1] = lanternfish[birth_left][life_left]
        lanternfish[birth_left][lifetime - 1] = 0
            


lifetime = 10
birthtime = 4
at_birth = 2

input_file = open("day_6/input.txt", "r")
numbers = input_file.read().split(",")
input_file.close()
lanternfish = [[0 for i in range(lifetime)] for i in range(birthtime + at_birth + 1)]
for number in numbers:
    lanternfish[int(number)][random.randint(birthtime, lifetime - 1)] += 1
    
    
num_days = 10000
for day in range(num_days):
    update_birthrate(lanternfish)
    new = lanternfish[0]
    for birth_index in range(1, len(lanternfish)):
        lanternfish[birth_index - 1] = lanternfish[birth_index]
    lanternfish[birthtime + at_birth] = [0 for i in range(lifetime)]
    for life_left in range(lifetime):
        lanternfish[birthtime + at_birth][lifetime - 1] += new[life_left]
        lanternfish[birthtime][life_left] += new[life_left]

total = 0
for birth_time in lanternfish:
    for life_left in birth_time:
        total += life_left
print(total)
