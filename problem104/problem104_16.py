ans = 0
l,r,d = [int(x) for x in input().split()]
for i in range(l,r+1):
    if i % d == 0:
        ans = ans + 1
print(ans)

