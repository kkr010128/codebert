a,b,c,d = map(int,input().split())

l1 = [a,b]
l2 = [c,d]

if(a<0 and 0<b):
    l1.append(0)
if(c<0 and 0<d):
    l2.append(0)

l = []
for x in l1:
    for y in l2:
        l.append(x*y)

print(max(l))


