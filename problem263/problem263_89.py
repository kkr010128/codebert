import sys
N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
mod = 10**9 + 7

cnt_one = [0] * 60
cnt_zero = [0] * 60

def count_bin(a):
    base = 1
    for i in range(60):
        if a % (base * 2) > 0:
            cnt_one[i] += 1
            a -= base
        else:
            cnt_zero[i] += 1
        base *= 2

for a in A:
    count_bin(a)

base = 1
ans = 0
for one, zero in zip(cnt_one, cnt_zero):
    ans += one * zero * base
    ans %= mod
    base *= 2
    base %= mod
print(ans)