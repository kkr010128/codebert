n = int(input())
a = list(sorted(map(int,input().split())))[::-1]
ans = 0
for x in range(1,n):
    ans += a[x//2]
print(ans)