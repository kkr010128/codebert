X,Y=map(int,input().split())
S=[0,3e5,2e5,1e5]+[0]*205
if X==Y==1:
    print(round(1e6))
else:
    print(round(S[X]+S[Y]))