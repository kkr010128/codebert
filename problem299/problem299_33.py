import numpy
N = int(input())
A = [int(x) for x in input().split()]
a = numpy.argsort(A)
a += 1
print(*a)