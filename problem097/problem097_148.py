K = int(input())

ans = -1
tmp = 0
for i in range(1, K + 1):
    tmp = (tmp*10%K + 7) % K
    if tmp == 0:
        ans = i
        break

print(ans)