n = [0,0,1]

def moveZeroes(nums):
    z = 0
    for i in range(len(nums)):
        if nums[z] == 0:
            nums.append(0)
            del nums[z]
        else:
            z += 1
    return nums

print(moveZeroes(n))