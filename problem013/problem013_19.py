import sys
n = int(raw_input())
R = [int(raw_input()) for i in xrange(n)]
minimum = sys.maxint
maximum = -sys.maxint - 1
for x in R:
    p = x - minimum
    if maximum < p:
        maximum = p

    if minimum > x:
        minimum = x
print maximum