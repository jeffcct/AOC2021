def binary_to_decimal(binary):
    decimal = 0
    length = len(binary)
    for i in range(len(binary)):
        if binary[length - i - 1] != "0":
            decimal += 2**i
    return decimal
        

# get inputs
input_file = open("day_3/input.txt", "r")
contents = input_file.read().split("\n")
input_file.close()
output = []

# interpret
for number in contents:
    if len(number) > len(output):
        for i in range(len(number) - len(output)):
            output.append(0)
    for i in range(len(number)):
        if number[i] == "0":
            output[i] -= 1
        else:
            output[i] += 1
            
# calculations
gamma_bin = ""
epsilon_bin = ""
for number in output:
    if number > 0:
        gamma_bin += "0"
        epsilon_bin += "1"
    else:
        gamma_bin += "1"
        epsilon_bin += "0"
gamma = binary_to_decimal(gamma_bin)
epsilon = binary_to_decimal(epsilon_bin)

# outputs
power = gamma * epsilon
print(power, gamma, epsilon)