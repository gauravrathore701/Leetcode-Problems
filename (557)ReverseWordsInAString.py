s = "Let's take LeetCode contest"

def reverseWords(s):
    s = s.split(" ")
    l = []
    for word in s:
        l.append(word[::-1])
    return " ".join(l)
    

print(reverseWords(s))