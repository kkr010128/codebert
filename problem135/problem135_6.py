import math

A, B = input().split()
A = int(A)
B = float(B)
B = int(B * 100 + 1e-5)

res = int(math.floor((A * B) // 100))
print(res)
