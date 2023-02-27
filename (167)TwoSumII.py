nums = [1,3,4,5,7,11]
t = 9

def twoSum(numbers, target):
    l, r = 0, len(numbers) - 1
    while l<r:
        if numbers[l] + numbers[r] == target:
            return [l+1,r+1]
        if numbers[l] + numbers[r] > target:
            r -= 1
        if numbers[l] + numbers[r] < target:
            l += 1

print(twoSum(nums,t))