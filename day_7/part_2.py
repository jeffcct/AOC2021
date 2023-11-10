import math
def sum_1_to_n(n):
    total = 0
    for i in range(n, 0, -1):
        total += i
    return total
    
def mean(data):
    total = 0
    for element in data:
        total += element
    return total / len(data)

def find_gas(data, pos):
    total = 0
    for element in data:
        total += sum_1_to_n(abs(element - pos))
    return total
    

data = [int(i) for i in open("day_7/input.txt", "r").read().split(",")]
mean = mean(data)
print(min(find_gas(data, math.floor(mean)), find_gas(data, math.ceil(mean)))) 