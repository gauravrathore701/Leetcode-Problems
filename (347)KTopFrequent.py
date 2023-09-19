def topKFrequent(nums, k):
    a = {}
    f = [[] for i in range(len(nums)+1)]
    for i in range(len(nums)):
        a[nums[i]] = 1 + a.get(nums[i], 0)
    for n, c in a.items():
        f[c].append(n)
    res = []
    for i in range(len(f) - 1,0,-1):
        for n in f[i]:
            res.append(n)
            if len(res) == k:
                return res

print(topKFrequent([1,1,1,2,2,3],2))