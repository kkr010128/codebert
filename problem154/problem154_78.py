n, k = map(int, input().split())
a = [0] * n
for i in range(k):
    d = int(input())
    for l in list(map(int, input().split())):
        a[l-1] = 1

cnt = 0
for i in range(n):
    if a[i] == 0:
        cnt += 1
print(cnt)