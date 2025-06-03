import sys , math
from bisect import bisect
N=int(input())
alp="abcdefghijklmnopqrstuvwxyz"

R=[]
i=1
tot = 0
while tot < 1000000000000001:
    tar = 26**i
    tot+=tar
    R.append(tot+1)
    i+=1
keta = bisect(R , N)+1

if keta == 1:
    print(alp[N-1])
    sys.exit()

ans = ""
M = N - R[keta - 1]
for i in range(keta):
    j = keta - i - 1
    ind = M // (26**j)
    M -= ind * (26**j)
    ans+=alp[ind]
print(ans)