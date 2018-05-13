def find_first(a, n):
    low = 0
    high = len(a) -1
    result = -1
    while low <= high:
        mid = (high + low) / 2
        if a[mid] == n:
            result = mid
            high = mid -1
        elif n < a[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return result

def find_last(a, n):
    low = 0
    high = len(a) -1
    result = -1
    while low <= high:
        mid = (high + low) / 2
        if a[mid] == n:
            result = mid
            low = mid + 1
        elif n < a[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return result

def find_count(a, n):
    first = find_first(a, n)
    last = find_last(a, n)
    return last - first + 1
