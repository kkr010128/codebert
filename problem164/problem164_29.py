#B
A, B, C, D=map(int, input().split())

A_survive=0
C_survive=0

while A>0:
    A-=D
    A_survive+=1
while C>0:
    C-=B
    C_survive+=1
if A_survive >= C_survive:
    print('Yes')
else:
    print('No')