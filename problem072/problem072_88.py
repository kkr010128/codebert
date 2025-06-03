N = int(input())
zoro = 0
ans = 'No'
for i in range(N):
    D1, D2 = map(int, input().split())
    if D1 == D2:
        zoro += 1
    else:
        zoro = 0

    if zoro == 3:
        ans = 'Yes'
        break

print(ans)