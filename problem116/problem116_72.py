S=input()
T=input()
N=len(S)
c=0
for i in range(N):
    if S[i]!=T[i]:
        c=c+1
print(c)
