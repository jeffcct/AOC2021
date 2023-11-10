import math
def quickselect(data, mid, left, right):
    if left == right:
        return data[left]
    pivot = data[left]
    pivotIndex = partition(data, left, right)
    if mid == pivotIndex:
        return pivot
    elif pivotIndex > mid:
        right = pivotIndex - 1
    else:
        left = pivotIndex + 1
    return quickselect(data, mid, left, right)
    
def quicksort(data, left, right):
    if left < right:
        pivot = partition(data, left, right)
        quicksort(data, left, pivot - 1)
        quicksort(data, pivot + 1, right)

def partition(data, left, right):
    pivot = data[right]
    i = left
    for j in range(left, right):
          
        if data[j] <= pivot:
            data[i], data[j] = data[j], data[i]
            i += 1
              
    data[i], data[right] = data[right], data[i]
    return i
                
def find_next(data, val):
    min = data[0] - val
    for element in data[1:]:
        if element > val and element - val < min:
            min = element - val
    return min + val
    
    
data = [int(x) for x in open("day_7/input.txt", "r").read().split(",")]
median = quickselect(data, len(data)// 2 - 1, 0, len(data) - 1)
total = 0
for element in data:
    total += abs(element - median)
print(total)

         
                
"""data = [int(x) for x in open("day_7/input.txt", "r").read().split(",")]
quicksort(data, 0, len(data) - 1)
print(data[len(data) // 2])
""" 

