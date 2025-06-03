def is_prime(x):
    if x == 1:
        return 0
    l = x ** 0.5
    n = 2
    while n <= l:
        if x % n == 0:
            return 0
        n += 1
    return 1

import sys

def solve():
    N = int(input())
    cnt = 0
    for i in range(N):
        cnt += is_prime(int(input()))
    print(cnt)

solve()