word = 'leetcode'
n = 'leeto'

def strStr(haystack, needle):
    for i in range(len(haystack) +1 -len(needle)):
        if haystack[i: i+len(needle)] == needle:
            return i
    return -1

print(strStr(word,n))