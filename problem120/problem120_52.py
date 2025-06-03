n,k = map(int,input().split())
p = [int(x) for x in input().split()]
p.sort()
s = 0
for i in range(k):
    s+=p[i]
print(s)


