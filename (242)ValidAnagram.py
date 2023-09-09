def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
    return True
    
"""
Another Solution is:
counter(s) == counter(t)

Counter is a python fuction which create a hashmap with a key value pair of each element.

Another:
Sorting could be another answer but some sorting methods take too much time and space. Ask interviwer before implementing.

"""

print(isAnagram('rat','car'))