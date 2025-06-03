s,t=input().split()
S,T=map(int,input().split())
dis=input()
if s==dis:
    print(S-1,T)
else:
    print(S,T-1)