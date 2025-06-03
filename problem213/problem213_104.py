n = int(input())
x = list(map(int,input().split()))
ans = 10 ** 12
for i in range(1,101):
    p = 0
    for j in x:
        p += (j - i) ** 2
    ans = min(ans,p)
print(ans)