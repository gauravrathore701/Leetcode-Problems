def topKFrequent(nums, k):
    count = {}     # defining the HashMap
    freq = [[] for i in range(len(nums)+1)] # same number of empty array as len of nums to count each repition
    # loop to count the number of times every value has occured
    for n in nums:
        count[n] = 1 + count.get(n, 0)
    # going through each value we counted
    for n, c in count.items(): #count.items() return key: value pairs that's been added to the dict
        freq[c].append(n)
    res = []
    # going through the frequency array in reverse order to return the number of k most frequent elements
    for i in range(len(freq) - 1,0,-1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

print(topKFrequent([1,1,1,2,2,3],2))