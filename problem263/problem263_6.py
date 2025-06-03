#昔はtleの回答、今は通る？
import sys
input=sys.stdin.readline
n=int(input())
lists=list(map(int,input().split()))
aa=[0 for i in range(n)]
bb=[0 for i in range(n)]
length=61
use=[0 for i in range(61)]
for  j in range(n):
    k=format(lists[j],"0%ib"%length)
    k=k[::-1]
    aa[j]=k[:30]  
    bb[j]=k[30:]
for p in aa:    
    for some in range(30):
        use[some]+=int(p[some])
for q in bb:    
    for some in range(31):
        use[some+30]+=int(q[some])
answer=0

for j in range(61):
    answer+=(2**j)*use[j]*(n-use[j])%(10**9+7)
print(answer%(10**9+7))
