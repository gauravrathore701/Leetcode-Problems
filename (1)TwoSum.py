def twoSum(nums, target):
    m = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in m:
            return [m[diff], n]
        m[n] = i