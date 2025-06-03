import bisect
n,d,a = map(int,input().split())
lst = []
x = []
for i in range(n):
    xi,hi = map(int,input().split())
    lst.append([xi,hi,0])
    x.append(xi)
lst.sort()
x.sort()
count = 0
cur = 0
for i in range(n):
    if lst[i][1]-cur > 0:
        num = -(-(lst[i][1]-cur)//a)
        count += num
        damage = a * num
        cur += damage
        index = bisect.bisect(x,x[i]+2*d)
        if index != n:
            lst[index-1][2] += damage
    cur -= lst[i][2]
print(count)