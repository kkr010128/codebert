n = int(input())

a = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    temp = 0 if a[i][0] - a[i][1] < 0 else a[i][0] - a[i][1]
    a[i][1] = a[i][0]+a[i][1]
    a[i][0] = temp

a.sort(key = lambda x:x[1])

ans = n
right = 0
for j in a:
    if right > j[0]:
        ans -= 1
    else:
        right = j[1]

print(ans)