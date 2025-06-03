A,B,C=map(int,input().split())
if C-A-B>0 and (C-A-B)**2>4*A*B:
    print('Yes')
else:
    print('No')