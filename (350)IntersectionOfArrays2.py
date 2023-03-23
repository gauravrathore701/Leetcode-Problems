class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = Counter(nums1)
        output = []
        for n in nums2:
            if c[n]>0:
                output.append(n)
                c[n]-=1
        return output


n1 = [1,2,3]
n2 = [1,1]
print(intersect(n1, n2))