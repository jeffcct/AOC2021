def binary_to_decimal(binary):
    decimal = 0
    length = len(binary)
    for i in range(len(binary)):
        if binary[length - i - 1] != "0":
            decimal += 2**i
    return decimal
        
        
def main(contents):
    zeroes, ones = [], []
    total = 0
    for number in contents:
        if number[0] == "0":
            zeroes.append(number)
            total-=1
        else:
            ones.append(number)
            total+=1
            
    if total > -1:
        oxygen = get_frequent(ones, 1)
        co2 = get_infrequent(zeroes, 1)
    else:
        oxygen = get_frequent(zeroes, 1)
        co2 = get_infrequent(ones, 1)
    print(oxygen, co2)
    return binary_to_decimal(oxygen) * binary_to_decimal(co2)
        
        
def get_frequent(nums, i):
    if len(nums) == 1:
        return nums[0]
    
    zeroes, ones = [], []
    total = 0
    for number in nums:
        if number[i] == "0":
            zeroes.append(number)
            total-=1
        else:
            ones.append(number)
            total+=1
    if total >= 0:
        return get_frequent(ones, i+1)
    else:
        return get_frequent(zeroes, i+1)
     
     
def get_infrequent(nums, i):
    if len(nums) == 1:
        return nums[0]
    
    zeroes, ones = [], []
    total = 0
    for number in nums:
        if number[i] == "0":
            zeroes.append(number)
            total-=1
        else:
            ones.append(number)
            total+=1
    if total >= 0:
        return get_infrequent(zeroes, i+1)
    else:
        return get_infrequent(ones, i+1)
    

# get inputs
input_file = open("day_3/input.txt", "r")
contents = input_file.read().split("\n")
input_file.close()
print(main(contents))
