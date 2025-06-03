import sys
readline = sys.stdin.buffer.readline
read = sys.stdin.buffer.read

import numpy as np


#N = 2 * 10 ** 5
#X = np.random.randint(0, 2, N)
#Y = int('0b' + ''.join(X.astype(str).tolist()), 0)

N = int(input())
X = input()
Y = int('0b' + X, 0)
X = np.array(list(X), int)

p = int(X.sum())
m1 = Y % (p + 1)
m2 = Y % max(1, p - 1)


count = np.zeros((N + 1, ))
for n in range(1, N):
    i = np.array(list(bin(n))[2:], int).sum()
    count[n] = 1 + count[n % i]

ans = [0] * N
for n in range(1, N + 1):
    flag = 0
    if X[n - 1]:
        z = m2 - pow(2, N - n, max(1, p - 1))
        z %= max(1, p - 1)
        if p - 1 == 0:
            flag = 1
    else:
        z = pow(2, N - n, p + 1) + m1
        z %= p + 1
        if p == 0:
            z = 0

    ans[n - 1] = int(count[z] + 1)
    if z == 0 and flag:
        ans [n - 1] = 0

print('\n'.join(map(str, ans)))