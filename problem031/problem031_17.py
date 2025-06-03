import math
sigma=[]
while(True):
    N=int(input())
    if N==0:
        break
    s=[int(i) for i in input().split()]
    av=sum(s)/N
    sg=math.sqrt(sum([(s[i]-av)**2 for i in range(N)])/N)
    sigma.append(sg)
for sg in sigma:
    print(sg)

