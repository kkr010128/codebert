import numpy as np

n = int(input())

a = []
b = []


for i in range(n):
    ae, be = map(int, input().split())
    a.append(ae)
    b.append(be)

a_med = np.median(a)
b_med = np.median(b)

if n % 2 == 0:
    print(int(2*b_med - 2*a_med + 1))
else:
    print(int(b_med - a_med + 1))
