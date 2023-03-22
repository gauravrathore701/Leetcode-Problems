n1 = [1,2,2,1]
n2 = [2,2]

def intersection(nums1, nums2):
    z = []
    for i in nums1:
        if i in nums2 and i not in z:
            z.append(i)
    return z

print(intersection(n1, n2))