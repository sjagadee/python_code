numbers = [4, 9, 3, 6, 2]

print(numbers)

for i in range(len(numbers) - 1):
    min_index = i
    for j in range(i+1, len(numbers)):
        if numbers[j] < numbers[min_index]:
            min_index = j
    
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

print(numbers)
