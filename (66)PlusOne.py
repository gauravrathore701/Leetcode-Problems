d = [1,2,3]

def plusOne(digits):
    total, z = '', []
    for i in digits:
        total = total + str(i)
    res = int(total) + 1
    for i in str(res):
        z.append(int(i))
    return z

print(plusOne(d))