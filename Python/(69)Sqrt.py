z = 16

def mysqrt(x):
    y, m = 0, 1
    while x >= m:
        x = x - m
        m = m + 2
        y = y + 1
    return y

print(mysqrt(z))

