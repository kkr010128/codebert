n = int(input())
a = list(map(int, input().split()))
num = [0]*(10**6+1)
for x in a:
    if num[x] != 0:
        num[x] = 2
        continue
    for i in range(x, 10**6+1, x):
        num[i] += 1

ans = 0
for x in a:
    if num[x] == 1:
        ans += 1

print(ans)