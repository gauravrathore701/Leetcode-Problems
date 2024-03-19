def missingNumber(nums):
    sol = len(nums)
    for i in range(len(nums)):
        sol += (i - nums[i])
    return sol

print(missingNumber([0,1,3]))