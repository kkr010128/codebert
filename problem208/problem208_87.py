import sys
N,M = map(int,input().split())
s = []
c = []
for i in range(M):
    S,C = map(int,input().split())
    s.append(S)
    c.append(C)
    

for i in range(10**(N+1)):
    st = str(i)

    if  len(st) == N and all([st[s[j]-1] == str(c[j]) for j in range(M)]):
        print(st)
        sys.exit()
        
print(-1)