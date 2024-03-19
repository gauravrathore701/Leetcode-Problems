p, l = [3,2,2,1], 3

def numRescueBoats(people, limit):
    people.sort()
    boats = 0
    l, r = 0, len(people) - 1
    while l <= r:
        diff = limit - people[r]
        r -= 1
        boats += 1
        if l <= r and diff >= people[l]:
            l+=1
    return boats
print(numRescueBoats(p,l))