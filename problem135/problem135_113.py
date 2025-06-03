import math
A, B = [i for i in input().split()]
A = int(A)
tmp = B.split('.')
B = 100 * int(tmp[0]) + int(tmp[1])
print((A*B)//100)