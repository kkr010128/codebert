from sys import stdin

input = stdin.readline

N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
res = a[0]
cnt = N - 2
cur = 1
while cnt:
    if cnt == 1:
        res += a[cur]
        break
    else:
        res += a[cur] * 2
        cur += 1
        cnt -= 2

print(res)