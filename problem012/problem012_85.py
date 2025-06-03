def is_prime(x):
    if x == 1:
        return False
    l = x ** 0.5
    n = 2
    while n <= l:
        if x % n == 0:
            return False
        n += 1
    return True

import sys

def solve():
    file_input = sys.stdin
    N = file_input.readline()
    cnt = 0
    for l in file_input:
        x = int(l)
        if is_prime(x):
            cnt += 1
    print(cnt)

solve()