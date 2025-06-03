n = int(input())
a = list(map(int,input().split()))
c = [0,0,0]
count = 1
for i in range(n):
    match = (a[i]==c[0])+(a[i]==c[1])+(a[i]==c[2])
    if match==0:
        count = 0
        break
    elif match==1 or a[i]==0:
        c[c.index(a[i])] += 1
    else:
        c[c.index(a[i])] += 1
        count = (count*match)%(1e+9+7)
               
if count != 0:
    c = sorted(c,reverse=True)
    while 0 in c:
        c.pop()
    memory = set()
    kinds = 0
    for x in c:
        if not x in memory:
            kinds += 1
    for i in range(3,3-kinds,-1):
        count = (count*i)%(1e+9+7)

print(int(count))