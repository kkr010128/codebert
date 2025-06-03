n, x, y = map(int, input().split())

ans = [0 for i in range(n-1)]

for i in range(1, n):
    for j in range(i+1, n+1):
        t = min(abs(j-i), abs(x-i)+1+abs(y-j))
        ans[t-1] += 1

for a in ans:
    print(a)
