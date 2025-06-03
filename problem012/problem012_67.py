def is_prime(x):
    if x == 2:
        return 1
    elif x % 2 == 0:
        return 0
    l = x ** 0.5
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return 0
    return 1

import sys

def solve():
    file_input = sys.stdin
    N = file_input.readline()
    cnt = 0
    for l in file_input:
        cnt += is_prime(int(l))
    print(cnt)

solve()