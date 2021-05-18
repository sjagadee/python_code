nums = [4, 9, 3, 6, 2]
print(nums)

for index in range(len(nums)):
    smallest = index
    for nextElement in range(index+1, len(nums)):
        if nums[smallest] > nums[nextElement]:
            smallest = nextElement

    nums[index], nums[smallest] = nums[smallest], nums[index]

print(nums)
        
    
