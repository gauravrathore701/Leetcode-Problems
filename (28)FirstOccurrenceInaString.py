word = 'leetcode'
n = 'leeto'

def strStr(haystack, needle):
    if len(needle) > len(haystack):
        return -1
    l, h = 0, 0
    while h < len(haystack):
        if haystack[h] != needle[l]:
            h = h-l+1
            l = 0
        if haystack[h] == needle[l]:
            h += 1
            l += 1
            if l == len(needle):
                return h-l
    return -1

print(strStr(word,n))