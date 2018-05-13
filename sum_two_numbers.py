def sum_numbers(num1, num2):
    l1 = map(int, num1.split()[::-1])
    l2 = map(int, num2.split()[::-1])

    if len(l1) < len(l2):
        l1.extend(0 * (len(l2) - len(l1)))
    elif len(l2) < len(l1):
        l2.extend(0 * (len(l1) - len(l2)))

    result = list()
    carry = 0
    for i in xrange(len(l1)):
        curr_sum = carry + l1[i] + l2[i]
        result.append(curr_sum % 10)
        carry = curr_sum / 10
    if carry > 0:
        result.append(carry)

    return "".join(map(str,result[::-1]))


def sum_numbers1(num1, num2):
    l1 = map(int, num1.split()[::-1])
    l2 = map(int, num2.split()[::-1])

    if len(l2) < len(l1):
        l1, l2 = l2, l1

    result = list()
    carry = 0
    for i in xrange(len(l1)):
        curr_sum = carry + l1[i] + l2[i]
        result.append(curr_sum % 10)
        carry = curr_sum / 10
    for i in range(len(l2) - len(l1), len(l2)):
        curr_sum = carry + l2[i]
        result.append(curr_sum % 10)
        carry = curr_sum / 10

    if carry > 0:
        result.append(carry)
        carry = curr_sum / 10

    return "".join(map(str,result[::-1]))

print sum_numbers1("12", '12')
print sum_numbers1("111", '22')
print sum_numbers1("11", '222')
print sum_numbers1("11", '99')
print sum_numbers1("11", '999')