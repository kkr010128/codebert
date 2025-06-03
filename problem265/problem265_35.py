n = int(input())
ans = -1
for k in range(n, 0, -1):
    if n == k * 108 // 100:
        ans = k
        break
if ans > 0: print(ans)
else: print(':(')