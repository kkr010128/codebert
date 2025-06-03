n=int(input())
a=[int(i) for i in input().split()]
a.sort()
prod=1
for i in a:
    prod*=i
    if prod>10**18:
        break
if prod>10**18:
    print(-1)
else:
    print(prod)
