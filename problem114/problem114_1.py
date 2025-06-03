D=int(input())
c=list(map(int,input().split()))
s=[list(map(int,input().split())) for i in range(D)]

t=[int(input())-1 for i in range(D)]

v=[]
S=0


last=[0]*27
for d in range(D):
    S+=s[d][t[d]]

    last[t[d]]=d+1

    for i in range(26):
        S-=c[i]*(d+1 - last[i])
    
    print(S)
