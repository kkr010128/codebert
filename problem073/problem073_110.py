N = int(input())
ans = 0

for a in range(1,N):
    ans += N // a
    if N%a == 0:
        ans -= 1
print(ans)