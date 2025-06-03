n = int(input())
lis = list(map(int, input().split()))

lis = sorted(lis, reverse=True)

ans = lis[0]
t = 0
for i in range(1,n-1):
    if i % 2 != 0:
        t += 1
    ans += lis[t]
        

print(ans)