from collections import Counter


def intersect(nums1, nums2):
    c = Counter(nums1)
    output = []
    for n in nums2:
        if c[n]>0:
            output.append(n)
            c[n]-=1
    return output


n1 = [1,2,3,4]
n2 = [1,1]

print(intersect(n1, n2))