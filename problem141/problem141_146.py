n = int(input())
a = list(map(int,input().split()))
import sys

lim = [0]*(n+1)
aa = 0
for i in range(n+1):
    aa += a[n-i]
    lim[n-i] = aa
    
if n == 0:
    if a[0] != 1:
        print(-1)
        sys.exit()
    else:
        print(1)
        sys.exit()
        
if a[0] != 0:
    print(-1)
    sys.exit()
    
ha = [[0]*(n+1) for i in range(2)]
ha[0][0] = 1
ha[1][0] = 1
for i in range(n):
    ha[1][i+1] = min(ha[0][i]*2 , lim[i+1])
    ha[0][i+1] = ha[1][i+1] - a[i+1]
    if ha[0][i+1] <= 0 and i != n-1:
        print(-1)
        sys.exit()
    if ha[0][i+1] < 0 and i == n-1:
        print(-1)
        sys.exit()
        
print(sum(ha[1]))