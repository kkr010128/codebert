N = int(input())
S,T=input().split()
retsu = ""
for i in range(0,N):
    mozi = S[i]+T[i]
    retsu += mozi
print(retsu)