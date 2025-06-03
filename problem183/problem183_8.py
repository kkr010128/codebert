#F
import math
N = int(input())

m = int(math.sqrt(N-1))
Myaku = []
for i in range(1,m+1):
    if (N-1)%i == 0:
        if i != 1:
            Myaku.append(i)
        if (N-1)//i != i:
            Myaku.append((N-1)//i)
            
ans = len(Myaku)

n = int(math.sqrt(N))
Nyaku = []
for i in range(1,n+1):
    if N%i == 0:
        if i != 1:
            Nyaku.append(i)
        if N//i != i:
            Nyaku.append(N//i)
            
for ny in Nyaku:
    X = N
    while X%ny == 0:
        X //= ny
    if X%ny == 1:
        ans+=1
        
print(ans)
#print(Myaku,Nyaku)


