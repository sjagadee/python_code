
nums = [5,2,6, 1, 4, 8,3]

for i in range(len(nums)):
    for j in range(len(nums)-1, i, -1):
        if nums[j] < nums[j-1]:
            nums[j], nums[j-1] = nums[j-1], nums[j]

print(nums)