def compare_windows(width, numbers):
    total = 0
    for i in range(len(numbers) - width):
        if numbers[i] < numbers[i + width]:
            total += 1
    return total

input_file = open("input.txt", "r")
contents = [int(num) for num in input_file.read().split("\n")]
input_file.close()
print(compare_windows(3, contents))