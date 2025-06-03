N,K=map(int,input().split())

R,S,P=map(int,input().split())
T =input()

com = [0]*N

for i in range(N):
    if i>=K and T[i]==T[i-K] and com[i-K]!=0:
        continue
    
    elif T[i] =="r":
        com[i] =P
    elif T[i] =="s":
        com[i] =R
    else:
        com[i] =S

print(sum(com))
        
        
