def twoSum(nums, target):
    # Initializing the Hash Map in python also known as Dictionary
    m = {}
    # loop to count 
    for i, n in enumerate(nums):
        diff = target - n
        if diff in m:
            return [m[diff], n]
        m[n] = i