N=int(input())

c=list(input())

minimum=len(c)
W=0
R=c.count('R')

for i in range(0,len(c)):
    if c[i]=='W':
        W += 1
    else :
        R -= 1
    min_i=max(W,R)
    if min_i < minimum:
        minimum=min_i

if c.count('R')==0:
    minimum=0

print(minimum)