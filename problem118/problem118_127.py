import sys
read = sys.stdin.readline

N = int(read())
ans = 0
for i in range(1, N+1):
    n = N // i
    ans += 0.5 * n * (2*i + i * (n-1))
print(int(ans))
