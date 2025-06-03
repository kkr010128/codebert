n, x, y = map(int,input().split())

cnt = [0] * (n - 1)
for i in range(1, n):
    for j in range(i + 1, n + 1):
        temp1 = j - i
        temp2 = abs(i - x) + abs(j - y) + 1
        dis = min(temp1, temp2)
        cnt[dis - 1] += 1

print(*cnt, sep='\n')