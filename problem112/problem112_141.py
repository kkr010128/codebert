
import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def solve(a,k):
    a.sort()
    I = (np.abs(a)).argsort()
    a = a[I][::-1]
    if ( len(a) == k ): 
        return a
    if np.all( a<0 ):
        if ( k % 2 == 0 ):
            return a[:k]
        else:
            return a[-k:]
    p = a[a>=0]
    n = a[a<0]
    nums = [1]
    if k & 1:
        nums = [p[0]]
        p = p[1:]
        k -= 1
    if len(p) & 1:
        p = p[:-1]
    if len(n) & 1:
        n = n[:-1]
    p = p[::2] * p[1::2]
    n = n[::2] * n[1::2]
    a = np.concatenate([p,n])
    a.sort()
    a = a[::-1]
    return np.concatenate([nums,a[:k // 2]])

def main():
    n, k = map(int, readline().split())
    a = np.array(read().split(), np.int64)
    mod = 10**9 + 7
    b = solve(a,k).tolist()
    ans = 1
    for x in b:
        ans = ans * x % mod
    print(ans)

main()

