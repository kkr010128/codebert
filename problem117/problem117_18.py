def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())

n,m,k=sep()
a=lis()
b=lis()
from bisect import bisect_right
a_c=[a[0]]
b_c=[b[0]]
for i in range(1,n):
    a_c.append(a_c[-1]+ a[i])
for i in range(1,m):
    b_c.append(b_c[-1] + b[i])

m=-1
m=max(m,bisect_right(b_c,k))
for i in range(n):
    if a_c[i]<=k:
        t=k-a_c[i]
        t2=bisect_right(b_c,t)
        m=max(i+1+t2,m)
    else:
        break
print(max(0,m))











