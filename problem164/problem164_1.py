A,B,C,D=map(int,input().split())
nT = 0
nA = 0
while C-B>0:
    C -= B
    nT += 1
while A-D>0:
    A -= D
    nA += 1
if nT <= nA:
    print('Yes')
else:
    print('No')
