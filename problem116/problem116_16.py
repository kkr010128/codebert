S=str(input())
T=str(input())
c=len(S)
for i in range(len(S)):
    if S[i]==T[i]: c=c-1

print(c)