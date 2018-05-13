message = "hello world"
d = {}
letters = set(message)
for l in letters:
    d[message.count(l)] = l

print d[d.keys()[-1]], d.keys()[-1]


import collections
s = "helloworld"
print(collections.Counter(s).most_common(1)[0])




d = collections.defaultdict(int)
for c in s:
    d[c] += 1
print(sorted(d.items(), key=lambda x: x[1], reverse=True)[0])

# Python program to return the maximum occuring character in the input string
ASCII_SIZE = 256


def getMaxOccuringChar(str):
    # Create array to keep the count of individual characters
    # Initialize the count array to zero
    count = [0] * ASCII_SIZE

    # Utility variables
    max = -1
    c = ''

    # Traversing through the string and maintaining the count of
    # each character
    for i in str:
        count[ord(i)] += 1;

    for i in str:
        if max < count[ord(i)]:
            max = count[ord(i)]
            c = i

    return c


# Driver program to test the above function
str = "sample string"
print "Max occurring character is " + getMaxOccuringChar(str)

# Although this program can be written in atmost 3 lines in Python
# the above program has been written for a better understanding of
# the reader

# Shorter version of the program
# import collections
# str = "sample string"
# print "Max occurring character is " +
#        collections.Counter(str).most_common(1)[0][0]
