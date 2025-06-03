import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
rbg = [-1, -1, -1]
ans = 1
mod = 10 ** 9 + 7

for A in a:
    ans *= rbg.count(A - 1)
    ans %= mod
    for i in range(3):
        if rbg[i] == A - 1:
            rbg[i] = A
            break

print(ans)
