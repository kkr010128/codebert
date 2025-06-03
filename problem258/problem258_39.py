import sys
N = int(input())
if N % 2 != 0:
    print(0)
    sys.exit()
N //= 2
ans = 0
while N != 0:
    ans += N//5
    N //= 5

print(ans)
