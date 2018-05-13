

def multiply(num1, num2):
    n1 = num1[::-1]
    n2 = num2[::-1]
    d = (len(n1) + len(n2)) * [0]
    print num1
    print num2
    print n1
    print n2
    for i in xrange(len(n1)):
        for j in xrange(len(n2)):
            # print n1[i]
            # print n2[j]
            d[i+j] += int(n1[i]) * int(n2[j])
    print d
    result = ''
    for i in xrange(len(d)):
        print d
        print result
        result += str(d[i] % 10)
        carry = d[i] / 10
        if i + 1 < len(d):
            d[i+1] += carry
    return result[::-1].lstrip("0")



print multiply("23", "14")

# 345
#  12
#
#
# 345 * 2 =   2 * 5 , 2 * 4, 2 * 3
# 345 * 10 =         1 * 5, 1 * 4, 1*3

# 2
# 5
# [10, 0, 0, 0, 0]
# 2
# 4
# [10, 8, 0, 0, 0]
# 2
# 3
# [10, 8, 6, 0, 0]
# 1
# 5
# [10, 13, 6, 0, 0]
# 1
# 4
# [10, 13, 10, 0, 0]
# 1
# 3
# [10, 13, 10, 3, 0]
# [10, 13, 10, 3, 0]
#
# [10, 14, 10, 3, 0]
# 0
# [10, 14, 11, 3, 0]
# 04
# [10, 14, 11, 4, 0]
# 041
# [10, 14, 11, 4, 0]
# 0414
# 4140


