n = int(input())
a = list(map(int,input().split()))
ans = {}
for i in range(n):
    ans[a[i]] = i + 1
s = [ans[i+1] for i in range(n)]
print(*s)