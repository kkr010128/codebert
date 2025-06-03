n, k = map(int, input().split())
a = [int(x) for x in input().split()]

for i in range(min(k, 450)):
    tmp = [0] * (n + 1)
    for j in range(n):
        tmp[max(0, j - a[j])] += 1
        tmp[min(n, j + a[j] + 1)] -= 1
    
    cnt = 0
    for j in range(n):
        cnt += tmp[j]
        a[j] = cnt

for i in range(n):
    print(a[i], end=' ')