st = ['h','e','l','l','o']

def reverseString(s):
    l, r = 0, len(s) - 1
    while l<r:
        z = s[l]
        s[l] = s[r]
        s[r] = z
        l += 1
        r -= 1
    return s

print(reverseString(st))