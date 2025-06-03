l = []
a,b,c = map(int,input().split())
for i in range(a,b+1):
    if c % i == 0:
        l.append(i)
ll = len(l)
print(str(ll))
