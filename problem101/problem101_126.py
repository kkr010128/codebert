a, b, c = map(int, input().split())
k = int(input())

ans = 0
for i in range(10**5):
    if a < b*(2**i):
        b = b*(2**i)
        break
    ans += 1
for i in range(10**5):
    if b < c*(2**i):
        break
    ans += 1
if ans <= k:
    print('Yes')
else:
    print('No')