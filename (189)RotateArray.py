nums = [1,2,3,4,5,6,7]
k = 3

def rotate(nums, k):
    def reverse(l,r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1,r-1
            return nums

    k = k % len(nums)

    reverse(0,len(nums)-1)
    reverse(0,k-1)
    reverse(k, len(nums)-1)
    return nums

    

print(rotate(nums, k))