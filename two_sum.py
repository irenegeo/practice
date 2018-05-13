# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
def two_sum(a, target):
    for i in xrange(len(a) -1):
        for j in range(i +1, len(a)):
            if a[i] + a[j] == target:
                return i, j
    return None

def two_sum_dict(a, target):
    d = {x: i for i, x in enumerate(a)}
    for x in d:
        if target -x in d:
            return d[x], d[target-x]
    return None

print two_sum(a=[2, 7, 11, 15], target = 9)
print two_sum_dict(a=[2, 7, 11, 15], target = 9)