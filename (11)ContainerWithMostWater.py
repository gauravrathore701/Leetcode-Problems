h = [1,8,6,2,5,4,8,3,7]

def maxArea(height):
    l, r, area = 0, len(height) - 1, 0
    while l < r:
        res = (r-l) * min(height[l], height[r])
        area = max(res, area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return area

print(maxArea(h))