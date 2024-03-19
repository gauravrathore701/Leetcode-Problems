n = [1,1,1,2,2,3]
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 3:
        return len(nums)
    n, l = 2, len(nums)
    for i in range(2,l):
        if nums[i] != nums[n-2]:
            nums[n] = nums[i]
            n += 1
    return nums,n

print(removeDuplicates(n))